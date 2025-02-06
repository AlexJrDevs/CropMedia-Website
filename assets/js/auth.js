// Initialize Firebase
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.2.0/firebase-app.js";
import {
  getAuth,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signInWithPopup,
  GoogleAuthProvider,
  FacebookAuthProvider,
  onAuthStateChanged,
  signOut,
  linkWithPopup,
} from "https://www.gstatic.com/firebasejs/11.2.0/firebase-auth.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.2.0/firebase-analytics.js";

// Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBt1c2S_ojI9MAUCli1RYbntRBFA1ANAWU",
  authDomain: "cropmedia-23804.firebaseapp.com",
  projectId: "cropmedia-23804",
  storageBucket: "cropmedia-23804.appspot.com",
  messagingSenderId: "755811110158",
  appId: "1:755811110158:web:84d3b20700604677759b5f",
  measurementId: "G-35MXPD06VB",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const analytics = getAnalytics(app);

// Define the current page
const currentPage = window.location.pathname.split("/").pop();

// Listen for authentication state changes
onAuthStateChanged(auth, (user) => {
  const authButtons = document.querySelector(".auth-buttons");

  if (user) {
    // User is signed in
    const userEmail = user.email;

    const dashboardLink = document.getElementById("dashboard-link");
    const signOutBtn = document.getElementById("sign-out-btn");
    const signInLink = document.getElementById("sign-in-link");
    const signUpLink = document.getElementById("sign-up-link");

    // Display email inside the specific <p> element in dashboard.php
    const emailDisplayElement = document.getElementById("user-email-display");
    if (emailDisplayElement) {
      emailDisplayElement.textContent = userEmail;
    }

    // If on sign-in or sign-up page, redirect to dashboard
    if (currentPage === "sign-in.php" || currentPage === "sign-up.php") {
      window.location.href = "/Pages/dashboard.php";
    }
  
    if (user) {
      // User is signed in
      dashboardLink.style.display = "block";
      signOutBtn.style.display = "block";
      signInLink.style.display = "none";
      signUpLink.style.display = "none";
    } else {
      // User is signed out
      dashboardLink.style.display = "none";
      signOutBtn.style.display = "none";
      signInLink.style.display = "block";
      signUpLink.style.display = "block";
    }

    // Update social media connection buttons
    updateSocialMediaButtons(user);
  } else {

    // Only redirect to sign-in if on dashboard page
    if (currentPage === "dashboard.php") {
      window.location.href = "/Pages/sign-in.php";
    }
  }
});

// Function to update social media connection buttons
function updateSocialMediaButtons(user) {
  const googleConnectButton = document.getElementById("google-connect");
  const facebookConnectButton = document.getElementById("facebook-connect");

  if (user) {
    let isGoogleConnected = false;
    let isFacebookConnected = false;

    // Check which providers are connected
    user.providerData.forEach((profile) => {
      if (profile.providerId === GoogleAuthProvider.PROVIDER_ID) {
        isGoogleConnected = true;
      }
      if (profile.providerId === FacebookAuthProvider.PROVIDER_ID) {
        isFacebookConnected = true;
      }
    });

    // Update Google button
    if (googleConnectButton) {
      if (isGoogleConnected) {
        googleConnectButton.textContent = "Disconnect Google";
        googleConnectButton.classList.remove("enabled", "connect");
        googleConnectButton.classList.add("disconnect");
      } else {
        googleConnectButton.textContent = "Connect Google";
        googleConnectButton.classList.remove("disconnect");
        googleConnectButton.classList.add("enabled", "connect");
      }
    }

    // Update Facebook button
    if (facebookConnectButton) {
      if (isFacebookConnected) {
        facebookConnectButton.textContent = "Disconnect Facebook";
        facebookConnectButton.classList.remove("enabled", "connect");
        facebookConnectButton.classList.add("disconnect");
      } else {
        facebookConnectButton.textContent = "Connect Facebook";
        facebookConnectButton.classList.remove("disconnect");
        facebookConnectButton.classList.add("enabled", "connect");
      }
    }
  }
}

// Sign out function
window.signOut = async () => {
  try {
    await signOut(auth);
    window.location.href = "/Pages/index.php";
  } catch (error) {
    console.error("Error signing out:", error);
  }
};

// Wait for DOM to load
document.addEventListener("DOMContentLoaded", () => {
  // Handle sign-up form if it exists
  const signUpForm = document.querySelector('form#sign-up-form');
  if (signUpForm) {
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirm-password");

    signUpForm.addEventListener("submit", async (e) => {
      e.preventDefault();

      // Get form values
      const email = emailInput.value;
      const password = passwordInput.value;
      const confirmPassword = confirmPasswordInput.value;

      // Basic validation
      if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return;
      }

      try {
        // Create user with email and password
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;
        console.log("User created:", user);

        // Redirect to dashboard
        window.location.href = "/Pages/dashboard.php";
      } catch (error) {
        console.error("Error creating user:", error);
        alert(error.message);
      }
    });
  }

  // Handle sign-in form if it exists
  const signInForm = document.querySelector('form#sign-in-form');
  if (signInForm) {
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");

    signInForm.addEventListener("submit", async (e) => {
      e.preventDefault();

      // Get form values
      const email = emailInput.value;
      const password = passwordInput.value;

      try {
        // Sign in with email and password
        const userCredential = await signInWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;
        console.log("User signed in:", user);

        // Redirect to dashboard
        window.location.href = "/Pages/dashboard.php";
      } catch (error) {
        console.error("Error signing in:", error);
        alert(error.message);
      }
    });
  }

  // Setup Google Sign In
  const googleBtn = document.getElementById("google-connect");
  if (googleBtn) {
    googleBtn.addEventListener("click", async (e) => {
      e.preventDefault();
      const provider = new GoogleAuthProvider();

      console.log("CLICKED GOOGLE");

      try {
        const user = auth.currentUser;

        if (user) {
          // Link Google provider to the existing account
          const result = await linkWithPopup(user, provider);
          console.log("Google provider linked:", result.user);
          alert("Google account linked successfully!");
          updateSocialMediaButtons(result.user); // Update UI
        } else {
          // If no user is signed in, sign in with Google
          const result = await signInWithPopup(auth, provider);
          console.log("Google sign in successful:", result.user);
          window.location.href = "/Pages/dashboard.php";
        }
      } catch (error) {
        console.error("Google link error:", error);

        if (error.code === "auth/credential-already-in-use") {
          alert("This Google account is already linked to another user.");
        } else {
          alert(error.message);
        }
      }
    });
  }

  // Setup Facebook Sign In
  const facebookBtn = document.getElementById("facebook-connect");
  if (facebookBtn) {
    facebookBtn.addEventListener("click", async (e) => {
      e.preventDefault();
      const provider = new FacebookAuthProvider();

      try {
        const user = auth.currentUser;

        if (user) {
          // Link Facebook provider to the existing account
          const result = await linkWithPopup(user, provider);
          console.log("Facebook provider linked:", result.user);
          alert("Facebook account linked successfully!");
          updateSocialMediaButtons(result.user); // Update UI
        } else {
          // If no user is signed in, sign in with Facebook
          const result = await signInWithPopup(auth, provider);
          console.log("Facebook sign in successful:", result.user);
          window.location.href = "/Pages/dashboard.php";
        }
      } catch (error) {
        console.error("Facebook link error:", error);

        if (error.code === "auth/credential-already-in-use") {
          alert("This Facebook account is already linked to another user.");
        } else {
          alert(error.message);
        }
      }
    });
  }
});