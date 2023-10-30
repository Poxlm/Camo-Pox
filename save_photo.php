<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $content = file_get_contents('php://input');
    $data = json_decode($content, true);
    $imageDataURL = $data['imageDataURL'];
    $base64Data = substr($imageDataURL, strpos($imageDataURL, ',') + 1);
    $imageData = base64_decode($base64Data);
    $filename = 'photo_' . uniqid() . '.jpg';
    file_put_contents($filename, $imageData);
    echo json_encode(['status' => 'success', 'filename' => $filename]);
} else {
    echo 'Invalid request';
}
?>
