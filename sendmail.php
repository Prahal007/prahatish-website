<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];
    
    // Email details
    $to = "prahatish0711@gmail.com";
    $subject = "New Contact Form Submission from $name";
    
    // Create email message
    $email_message = "Name: $name\n";
    $email_message .= "Email: $email\n\n";
    $email_message .= "Message:\n$message";
    
    // Headers
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion();
    
    // Send email
    if(mail($to, $subject, $email_message, $headers)) {
        echo "<script>
            alert('Thank you for your message. We will get back to you soon!');
            window.location.href = 'Contact.html';
        </script>";
    } else {
        echo "<script>
            alert('Sorry, there was an error sending your message. Please try again.');
            window.location.href = 'Contact.html';
        </script>";
    }
}
?>
