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
  </head>
  <body>

    <section id="dashboard-section">
        <div class="dashboard-wrapper">
            <div class="dashboard-container">

              <div class="dashboard-header">
                <h1 class="dashboard-title">Manage Profile</h1>
                <p class="dashboard-subtitle">Edit your profile and connected accounts</p>
              </div>


              <div class="dashboard-accounts">
                  <div class="connect-accounts-header">
                    <h3>Connected Accounts</h3>
                    <p>Connect your Facebook or Google accounts to use them to sign in to CropMedia.</p>
                  </div>

                  <hr class="dashboard-accounts-line">

                  <div class="connect-account">
                      <div class="account-info">
                          <img src="../assets/images/icon_google.svg" alt="Google Icon">
                          <h3>Google</h3>
                      </div>
                      <button class="social-media-connect">Connect Google</button>
                  </div>
                  
                  <hr class="dashboard-accounts-line">

                  <div class="connect-account">
                      <div class="account-info">
                          <img src="../assets/images/icon_facebook.svg" alt="Google Icon">
                          <h3>Facebook</h3>
                      </div>
                      <button class="social-media-connect">Disconnect Facebook</button>
                  </div>

                  <hr class="dashboard-accounts-line">
              </div>

              <div class="account-section">

                <h2>Account details</h2>

                <hr class="dashboard-accounts-line">

                <div class="profile-details">

                    <div class="detail-row">
                        <h3>Email</h3>
                        <p>CropMedia@cropmedia.pro</p>
                    </div>

                    <hr class="dashboard-accounts-line">

                    <div class="detail-row">
                        <h3>Membership</h3>
                        <div class="membership-details">
                          <p>Free Plan - <a href="#">UPGRADE</a></p>
                          <p>Expire: 26/02/2025</p>
                        </div>
                    </div>

                    <hr class="dashboard-accounts-line">

                </div>
              </div>

            </div>
        </div>
    </section>

  </body>
</html>

<!-- start of footer -->
<?php
require_once(__DIR__ . "/../components/footer.php");
?>
<!-- end of footer -->
