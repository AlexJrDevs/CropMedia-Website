<!-- Navigation Section HTML Start -->
<section id="Header">
    <div class="navigation-wrapper">
        <nav>
            <div class="navigation-container">
                <div class="navigation-right">
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
                        <hr class="nav-line-splitter">
                        <li><a href="#">Resources</a></li>
                        <hr class="nav-line-splitter">
                        <li><a href="index.php#pricing-section">Pricing</a></li>
                    </ul>
                </div>
                

                <!-- Auth Buttons -->
                <div class="auth-buttons">
                    <ul>
                        <!-- Dashboard and Sign Out (hidden by default) -->
                        <li id="dashboard-li"><a class="dashboard-btn" href="dashboard.php" id="dashboard-link" style="display: none;">Dashboard</a></li>
                        <li id="sign-out-li"><button class="sign-out-btn" id="sign-out-btn" style="display: none;" onclick="signOut()">Sign Out</button></li>

                        <!-- Sign In and Sign Up (visible by default) -->
                        <li id="sign-in-li"><a class="sign-in-btn" href="sign-in.php" id="sign-in-link">Sign In</a></li>
                        <li id="sign-up-li"><a class="sign-up-btn" href="sign-up.php" id="sign-up-link">Sign Up</a></li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
</section>
<!-- Navigation Section HTML End -->