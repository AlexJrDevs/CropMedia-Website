<!-- start of navigation -->
<?php
require_once(__DIR__ . '/../components/header.php');
?>
<!-- end of navigation -->


<!-- start of base -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CropMedia - AI Long Video Repurposed</title>

    <!-- Font Awesome CDN -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
    />

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="../assets/css/bootstrap.min.css" />

    <!-- Custom CSS -->
    <link rel="stylesheet" href="../assets/css/style.css" />

    <!-- Responsive CSS -->
    <link rel="stylesheet" href="../assets/css/responsive.css" />

    <!-- Custom JavaScript -->
    <script type="module" src="../assets/js/auth.js" defer></script>
  </head>

    <section id="sign-in-section">
        <div class="account-form-wrapper">
            <div class="account-form-container">
                <div class="account-form-header">
                    <h1>Welcome Back!</h1>
                </div>
                <div class="account-form">
                    <form action="" method="POST">
                        <div class="form-group">
                            <label for="email">Email</label>
                            <input type="email" name="email" id="email" placeholder="Enter your email" required />
                        </div>
                        <div class="form-group">
                            <label for="password">Password</label>
                            <input type="password" name="password" id="password" placeholder="Enter your password" required />
                            <div class="form-forgot-password">
                                <a href="forgot-pass.php">Forgot your password?</a>
                            </div>
                        </div>
                        <div class="form-group">
                            <button type="submit" class="sign-up-button">Log In</button>
                            <div class="form-sign-in">
                                <p>Create an account? <a href="sign-up.php">Sign Up</a></p>
                            </div>
                        </div>


                        <div class="form-social-media">
                            <div class="form-social-media-split">
                                <hr class="form-social-media-line">
                                <p>OR</p>
                                <hr class="form-social-media-line">
                            </div>
                        </div>
                    </form>
                </div>

                <div class="social-media-icons">
                    <a href="#">
                        <img src="../assets/images/icon_google.svg"></i>
                        <p id="google-connect">Google</p>
                    </a>
                    <a href="#">
                        <img src="../assets/images/icon_facebook.svg"></i>
                        <p id="facebook-connect">Facebook</p>
                    </a>
                </div>
            </div>
            <div class="texture-wrapper">
                <img src="../assets/images/BG_texture_brighter.svg" alt="Texture Image">
            </div>
        </div>
    </section>
</html>


<!-- start of footer -->
<?php
require_once(__DIR__ . "/../components/footer.php");
?>
<!-- end of footer -->