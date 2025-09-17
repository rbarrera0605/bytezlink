<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to = "your-email@example.com"; // 👈 Replace this with your email address
    $subject = "New Contact Form Submission";

    // Sanitize inputs
    $name = htmlspecialchars(trim($_POST["name"]));
    $email = htmlspecialchars(trim($_POST["email"]));
    $message = htmlspecialchars(trim($_POST["message"]));

    // Compose email
    $body = "You received a new message from your website:\n\n";
    $body .= "Name: $name\n";
    $body .= "Email: $email\n\n";
    $body .= "Message:\n$message\n";

    // Set headers
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";

    // Send email
    if (mail($to, $subject, $body, $headers)) {
        echo "<h2>Thank you! Your message has been sent.</h2>";
    } else {
        echo "<h2>Sorry, something went wrong. Please try again later.</h2>";
    }
} else {
    header("Location: contact.php");
    exit;
}
?>
