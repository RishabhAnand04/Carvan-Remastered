<template>
  <div class="login-container">
    <div class="login-box">
      <div class="forms-container">
        <!-- Left Side: Login Form -->
        <div class="form-container login-form" :class="{ active: isLoginFormActive }">
          <h2>Login</h2>
          <form @submit.prevent="login">
            <div class="form-group">
              <label for="login-email">Email</label>
              <input type="email" id="login-email" v-model="loginEmail" placeholder="Enter your email" required>
            </div>
            <div class="form-group">
              <label for="login-password">Password</label>
              <input type="password" id="login-password" v-model="loginPassword" placeholder="Enter your password"
                required>
            </div>
            <button type="submit" class="toggle-button">Login</button>
          </form>
          <p class="instruction">Fill in the login details to access your account.</p>
          <button class="toggle-button" @click="toggleForm">Create Account</button>
        </div>

        <!-- Right Side: Sign-up Form -->
        <div class="form-container signup-form" :class="{ active: !isLoginFormActive }">
          <h2>Create Account</h2>
          <form @submit.prevent="createAccount">
            <div class="form-group">
              <label for="signup-name">Name</label>
              <input type="text" id="signup-name" v-model="signupName" placeholder="Enter your name" required>
            </div>
            <div class="form-group">
              <label for="signup-email">Email</label>
              <input type="email" id="signup-email" v-model="signupEmail" placeholder="Enter your email" required>
            </div>
            <div class="form-group">
              <label for="signup-password">Password</label>
              <input type="password" id="signup-password" v-model="signupPassword" placeholder="Enter your password"
                required>
            </div>
            <button type="submit" class="toggle-button">Sign Up</button>
          </form>
          <p class="instruction">Don't have an account? Create one by filling in the details below.</p>
          <button class="toggle-button" @click="toggleForm">Back to Login</button>
        </div>
      </div>
    </div>
    <v-snackbar v-model="snackbar" :color="snackbarColor" :timeout="3000" :dark="$vuetify.theme.dark" :light="!$vuetify.theme.dark">
  <div style="display: flex; align-items: center;">
      <span style="font-size: 24px; margin-right: 8px;">❌</span>
      <span class="text--white">{{ snackText }}</span>
    </div>
</v-snackbar>

  </div>
</template>

<script>
export default {
  data() {
    return {
      snackText: '',
      snackbar: false,
      snackbarColor: "white darken-2",
      isLoginFormActive: true,
      loginEmail: "",
      loginPassword: "",
      signupName: "",
      signupEmail: "",
      signupPassword: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(
            {
              email: this.loginEmail,
              password: this.loginPassword,
            }
          ),
        });

        if (response.status === 200) {
          // Successful login
          // Redirect or perform actions as needed
        } else {
          // Failed login
          this.snackbar = true;
          this.snackText = 'Error. Please provide correct credentials';
          console.error('Login failed');
        }
      }
      catch (error) {
        console.error('An error occurred:', error);
      }
    },
    createAccount() {
    },
    toggleForm() {
      this.isLoginFormActive = !this.isLoginFormActive;
    },
  },
};
</script>

<style scoped>
/* Container styles */
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #1a0da3, #056632);
}

.login-box {
  width: 100%;
  max-width: 800px;
  display: flex;
  justify-content: center;
}

/* Forms container styles */
.forms-container {
  display: flex;
  width: 100%;
  max-width: 800px;
  overflow: hidden;
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);
}

.form-container {
  flex: 1;
  padding: 40px;
  /* Increased padding for more spacious look */
  border-radius: 5px;
  background-color: #ffffff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transition: transform 0.5s ease-in-out, opacity 0.5s ease-in-out;
  transform: translateX(0%);
  opacity: 1;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.form-container.active {
  transform: translateX(100%);
  opacity: 0;
  pointer-events: none;
}

/* Heading styles */
h2 {
  text-align: center;
  color: #333;
  margin-bottom: 20px;
}

/* Instruction styles */
.instruction {
  text-align: center;
  margin-top: 10px;
  color: #666;
}

/* Form input styles */
.form-group {
  width: 100%;
  max-width: 400px;
  /* Increased max-width for text boxes */
  margin-bottom: 20px;
  /* Increased margin for spacing between form elements */
  text-align: left;
}

.form-group label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #333;
}

.form-group input {
  width: 100%;
  padding: 12px;
  /* Increased padding for text boxes */
  border: 1px solid #ccc;
  border-radius: 5px;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.form-group input:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0px 0px 8px rgba(0, 123, 255, 0.5);
}

/* Button styles */
.toggle-button {
  width: 100%;
  max-width: 200px;
  margin-top: 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 12px;
  /* Increased padding for buttons */
  cursor: pointer;
  transition: background-color 0.3s;
}

.toggle-button:hover {
  background-color: #0056b3;
}
</style>