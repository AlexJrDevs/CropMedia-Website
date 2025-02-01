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

  <section id="hero-section">
    <div class="hero-wrapper">
      <div class="hero-texture">
        <img src="../assets/images/BG_texture.svg" alt="bg-texture" />
      </div>
      <div class="hero-container">
        <div class="hero-content">
          <h1>1 Long Video, Endless Clips. <br>All In One Click.</h1>
          <p>
            Long Videos Into Viral Clips, Effortlessly.
          </p>
          <div class="hero-upload-container">
            <div class="hero-upload-content">
              <a class="upload-text">Drop a long video file</a>
              <a href="sign-up.php" class="upload-button">Upload Video</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="features-section">
    <div class="features-wrapper">
      <div class="features-header">
        <h2><span class="features-header-underline">Instant</span> Clips, Ready to Share</h2>
      </div>
      <div class="features-container">
        <div class="features-card">
          <div class="features-card-icon">
            <img src="../assets/images/timeline.svg" alt="icon" />
          </div>
          <div class="features-card-content">
            <h3>Take Control</h3>
            <p>
              Have control over what sections of the video you want to cut to edit.
            </p>
          </div>
        </div>
        <div class="features-card">
          <div class="features-card-icon">
            <img src="../assets/images/AI_tracking.svg" alt="icon" />
          </div>
          <div class="features-card-content">
            <h3>AI Reframe</h3>
            <p>
              Our AI will automatically detect active speakers, re-framing them into focus.
            </p>
          </div>
        </div>
        <div class="features-card">
          <div class="features-card-icon">
            <img src="../assets/images/Auto_captions.svg" alt="icon" />
          </div>
          <div class="features-card-content">
            <h3>Create Captions</h3>
            <p>
              Edit, style, and customize your captions with 98% transcription precision and 99 supported languages.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</html>
<!-- end of base -->


<!-- start of footer -->
<?php
require_once(__DIR__ . "/../components/footer.php");
?>
<!-- end of footer -->
