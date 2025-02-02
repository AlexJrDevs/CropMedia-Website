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

  <section id="first-features-section">
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


  <section id="second-features-section">
    <div class="features-wrapper">
      <div class="features-header">
        <h2>Personalize With<br> Dual Video, Fonts & More</h2>
      </div>
      <div class="features-container">
        <div class="features-card">
          <div class="features-card-icon">
            <img src="../assets/images/dual_video.svg" alt="icon" />
          </div>
          <div class="features-card-content">
            <h3>Dual Video</h3>
            <p>
              Choose if you would like to add a video at the bottom of your clips, to increase attention.
            </p>
          </div>
        </div>
        <div class="features-card">
          <div class="features-card-icon">
            <img src="../assets/images/load_bar.svg" alt="icon" />
          </div>
          <div class="features-card-content">
            <h3>Create Locally</h3>
            <p>
              No waiting times, all done on your device, from transcription to editing.
            </p>
          </div>
        </div>
        <div class="features-card">
          <div class="features-card-icon">
            <img src="../assets/images/customize.svg" alt="icon" />
          </div>
          <div class="features-card-content">
            <h3>Customize</h3>
            <p>
              Powerful editing tools, with text and time line features.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="pricing-section">
    <div class="pricing-wrapper">
      <div class="pricing-header">
        <h2>Choose a plan</h2>
      </div>
      <div class="pricing-toggle">
          <button class="toggle-button active">Monthly</button>
          <button class="toggle-button">Annually</button>
      </div>
      <div class="pricing-plans">
        <div class="pricing-container">
          <div class="pricing-card">
            
            <p>Pro Package</p>
            <h3 class="pro-price">$4.99/month</h3>
            <p class="pro-description">Best for startups, etc.</p>
            <hr class="pro-line-splitter">
            <ul class="pro-features-list">
                <li>Unlimited Transcription</li>
                <li>Unlimited Clips</li>
                <li>Powerful Editor</li>
                <li>Dual Video Choice</li>
                <li>Priority support</li>
            </ul>
            <a href="#" class="pro-get-started-button">Get Started</a>
          </div>
        </div>

        <!-- add more pricing cards here -->
         
      </div>
    </div>
  </section>

  <section id="faq-section">
    <div class="faq-wrapper">
        <div class="faq-header">
            <h2>Frequently Asked Questions</h2>
        </div>
        <div class="faq-content">
            <!-- First Column -->
            <div class="faq-column">
                <div role="button" class="faq-card">
                    <div class="faq-card-title">
                        <img src="../assets/images/icon_add.svg" alt="icon" />
                        <h3>How does CropMedia work?</h3>
                    </div>
                    <div class="faq-card-content">
                        <hr class="faq-line-splitter">
                        <p>Details about how cropmedia works.</p>
                    </div>
                </div>
                <div role="button" class="faq-card">
                    <div class="faq-card-title">
                        <img src="../assets/images/icon_add.svg" alt="icon" />
                        <h3>Which languages are supported?</h3>
                    </div>
                    <div class="faq-card-content">
                        <hr class="faq-line-splitter">
                        <p>Details about supported languages.</p>
                    </div>
                </div>
                <div role="button" class="faq-card">
                    <div class="faq-card-title">
                        <img src="../assets/images/icon_add.svg" alt="icon" />
                        <h3>How do I gain access?</h3>
                    </div>
                    <div class="faq-card-content">
                        <hr class="faq-line-splitter">
                        <p>Details about gaining access.</p>
                    </div>
                </div>
            </div>


            <!-- Second Column -->
            <div class="faq-column">
                <div role="button" class="faq-card">
                    <div class="faq-card-title">
                        <img src="../assets/images/icon_add.svg" alt="icon" />
                        <h3>What types of videos can I upload?</h3>
                    </div>
                    <div class="faq-card-content">
                        <hr class="faq-line-splitter">
                        <p>Details about supported video types.</p>
                    </div>
                </div>
                <div role="button" class="faq-card">
                    <div class="faq-card-title">
                        <img src="../assets/images/icon_add.svg" alt="icon" />
                        <h3>I have more questions!</h3>
                    </div>
                    <div class="faq-card-content">
                        <hr class="faq-line-splitter">
                        <p>Details on how to get more help.</p>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </section>


    <section id="cta-section">
      <div class="cta-wrapper">
        <div class="cta-container">
          <h2>Cut, Edit and Share.</h2>
          <div class="cta-buttons">
            <a href="#" class="cta-get-started-button">Get Started</a>
            <a href="#" class="cta-sign-in-button">Sign In</a>
          </div>
        </div>
        <div class="cta-texture">
          <img src="../assets/images/BG_texture.svg" alt="bg-texture" />
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
