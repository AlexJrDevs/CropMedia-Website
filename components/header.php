<!-- Navigation Section HTML Start -->

<section id="Header">
                
    <div class="navigation-wrapper">
        <nav>

            <div class="navigation-container">
                
                <!-- Dropdown button for smaller screens -->
                <div class="dropdown-button">
                    <button onclick="toggleMenu()">☰</button>
                </div>

                <div class="header-logo">
                    <a href="index.php">
                        <img src="../assets/images/DM_Logo.svg" alt="logo" />
                    </a>
                    <a href="index.php">
                        <span>CropMedia</span>
                    </a>
                </div>

                <div class="nav-menu">
                    <div class="nav-menu-header">
                        <div class="dropdown-logo">
                            <a href="index.php">
                                <img src="../assets/images/DM_Logo.svg" alt="logo" />
                            </a>
                        </div>
                        <div class="dropdown-close-button">
                            <button onclick="toggleMenu()">✖</button>
                        </div>
                    </div>
                    <ul>
                        <li><a href="#">Product</a></li>
                        <hr class="line-splitter">
                        <li><a href="#">Resources</a></li>
                        <hr class="line-splitter">
                        <li><a href="#">Pricing</a></li>
                    </ul>
                </div>

                <div class="auth-buttons">
                    <ul>
                        <li><a class="sign-in-btn" href="sign-in.php">Sign In</a></li>
                        <li><a class="sign-up-btn" href="sign-up.php">Sign Up</a></li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
</section>

<!-- Bootstrap JavaScript -->
<script src="../assets/js/bootstrap.bundle.min.js"></script>

<!-- Custom JavaScript -->
<script src="../assets/js/script.js"></script>