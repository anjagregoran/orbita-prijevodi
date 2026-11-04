<?php
// Quote form for orbitaprijevodi.com: sends the enquiry and attached documents to both offices.
// Runs on the TotoHost (cPanel) hosting with PHP's mail(); works on PHP 7.4 and 8.x.

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

$TO = ['info@orbitaprijevodi.com', 'zagreb@orbitaprijevodi.com'];
$FROM = 'web-obrazac@orbitaprijevodi.com';
$MAX_FILES = 10;
$MAX_BYTES = 20 * 1024 * 1024;
$ALLOWED = ['pdf', 'jpg', 'jpeg', 'png', 'heic', 'webp', 'doc', 'docx', 'odt', 'rtf', 'txt', 'xls', 'xlsx', 'ppt', 'pptx'];

if (!function_exists('mb_substr')) {
    function mb_substr($s, $start, $len) { return substr($s, $start, $len); }
}

function reply($ok, $error = '', $code = 200) {
    http_response_code($code);
    echo json_encode($ok ? ['ok' => true] : ['ok' => false, 'error' => $error], JSON_UNESCAPED_UNICODE);
    exit;
}
function field($name, $max = 2000) {
    $v = isset($_POST[$name]) ? trim((string)$_POST[$name]) : '';
    return mb_substr(str_replace("\0", '', $v), 0, $max);
}
function one_line($v) {
    return trim(preg_replace('/[\r\n]+/', ' ', $v));
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') reply(false, 'Neispravan zahtjev.', 405);
if (empty($_POST) && !empty($_SERVER['CONTENT_LENGTH'])) reply(false, 'Datoteke su prevelike. Pošaljite ih e-poštom na info@orbitaprijevodi.com.', 413);

// Bots fill the hidden field; pretend all went well
if (field('website') !== '') reply(true);

// At most 5 enquiries per 10 minutes from one address
$ip = isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : 'x';
$stamp = sys_get_temp_dir() . '/orbita_form_' . md5($ip);
$times = is_file($stamp) ? array_filter(explode(',', (string)@file_get_contents($stamp)), function ($t) { return $t > time() - 600; }) : [];
if (count($times) >= 5) reply(false, 'Poslali ste više upita zaredom. Pokušajte ponovno za nekoliko minuta ili nas nazovite.', 429);
$times[] = time();
@file_put_contents($stamp, implode(',', $times));

$name = one_line(field('name', 120));
$email = one_line(field('email', 200));
$phone = one_line(field('phone', 60));
if ($name === '') reply(false, 'Upišite ime i prezime.', 422);
if ($email === '' && $phone === '') reply(false, 'Upišite e-poštu ili broj telefona.', 422);
if ($email !== '' && !filter_var($email, FILTER_VALIDATE_EMAIL)) reply(false, 'Provjerite adresu e-pošte.', 422);

$services = [];
if (isset($_POST['svc']) && is_array($_POST['svc'])) {
    foreach ($_POST['svc'] as $s) $services[] = one_line(mb_substr((string)$s, 0, 80));
}
$service = one_line(field('service', 120));
if ($service !== '') $services[] = $service;
$office = field('office', 20) === 'Zagreb' ? 'Zagreb' : 'Rijeka';
$SOURCES = ['Google oglas', 'Google pretraživanje', 'Google karte', 'Preporuka', 'Facebook/Instagram', 'Već sam bio/la klijent', 'Drugo'];
$source = in_array(field('source', 60), $SOURCES, true) ? field('source', 60) : '/';

$lines = [
    'Novi upit s web stranice orbitaprijevodi.com',
    '',
    'Ime i prezime: ' . $name,
    'E-pošta: ' . ($email !== '' ? $email : '/'),
    'Telefon: ' . ($phone !== '' ? $phone : '/'),
    'Usluga: ' . ($services ? implode(', ', $services) : '/'),
    'S jezika: ' . (one_line(field('from', 80)) ?: '/'),
    'Na jezik: ' . (one_line(field('to', 80)) ?: '/'),
    'Rok: ' . (one_line(field('deadline', 120)) ?: '/'),
    'Ured: ' . $office,
    'Kako su saznali za nas: ' . $source,
    '',
    'Poruka:',
    field('msg', 5000) ?: '/',
];

// Attachments
$parts = [];
$total = 0;
if (!empty($_FILES['files']) && is_array($_FILES['files']['name'])) {
    $count = count($_FILES['files']['name']);
    if ($count > $MAX_FILES) reply(false, "Možete priložiti najviše $MAX_FILES datoteka.", 422);
    for ($i = 0; $i < $count; $i++) {
        $err = $_FILES['files']['error'][$i];
        if ($err === UPLOAD_ERR_NO_FILE) continue;
        if ($err === UPLOAD_ERR_INI_SIZE || $err === UPLOAD_ERR_FORM_SIZE) reply(false, 'Neka je datoteka prevelika. Pošaljite je e-poštom na info@orbitaprijevodi.com.', 413);
        if ($err !== UPLOAD_ERR_OK) reply(false, 'Datoteka se nije uspjela učitati. Pokušajte ponovno.', 422);
        $tmp = $_FILES['files']['tmp_name'][$i];
        if (!is_uploaded_file($tmp)) reply(false, 'Neispravna datoteka.', 422);
        $orig = basename((string)$_FILES['files']['name'][$i]);
        $ext = strtolower(pathinfo($orig, PATHINFO_EXTENSION));
        if (!in_array($ext, $ALLOWED, true)) reply(false, 'Vrsta datoteke nije podržana: ' . $orig, 422);
        $size = filesize($tmp);
        $total += $size;
        if ($total > $MAX_BYTES) reply(false, 'Datoteke su zajedno veće od 20 MB.', 413);
        $safe = preg_replace('/[^\w.\-]+/u', '_', $orig);
        $parts[] = ['name' => $safe, 'data' => file_get_contents($tmp)];
    }
}
$lines[] = '';
$lines[] = $parts ? 'Priloženo datoteka: ' . count($parts) : 'Bez priloženih datoteka.';

// Build the message
$boundary = 'orb_' . bin2hex(random_bytes(12));
$subject = 'Upit za ponudu: ' . $name . ($services ? ' (' . $services[0] . ')' : '');
$headers = [
    'From: =?UTF-8?B?' . base64_encode('Orbita web obrazac') . '?= <' . $FROM . '>',
    'MIME-Version: 1.0',
    'Content-Type: multipart/mixed; boundary="' . $boundary . '"',
];
if ($email !== '') $headers[] = 'Reply-To: ' . $email;

$body = "--$boundary\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: base64\r\n\r\n"
      . chunk_split(base64_encode(implode("\n", $lines))) . "\r\n";
foreach ($parts as $p) {
    $fname = '=?UTF-8?B?' . base64_encode($p['name']) . '?=';
    $body .= "--$boundary\r\nContent-Type: application/octet-stream; name=\"$fname\"\r\n"
           . "Content-Transfer-Encoding: base64\r\nContent-Disposition: attachment; filename=\"$fname\"\r\n\r\n"
           . chunk_split(base64_encode($p['data'])) . "\r\n";
}
$body .= "--$boundary--";

$sent = mail(implode(', ', $TO), '=?UTF-8?B?' . base64_encode($subject) . '?=', $body, implode("\r\n", $headers), '-f' . $FROM);
if (!$sent) reply(false, 'Slanje trenutačno nije uspjelo. Pošaljite nam dokument na info@orbitaprijevodi.com ili WhatsAppom na 098 163 19 30.', 500);
reply(true);
