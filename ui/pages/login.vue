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
              <input type="password" id="login-password" v-model="loginPassword" placeholder="Enter your password" required>
            </div>
            <button type="submit" class="toggle-button">Login</button>
          </form>
          <p class="instruction">Fill in the login details to access your account.</p>
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
              <input type="password" id="signup-password" v-model="signupPassword" placeholder="Enter your password" required>
            </div>
            <button type="submit" class="toggle-button">Sign Up</button>
          </form>
          <p class="instruction">Don't have an account? Click "Create Account" below.</p>
        </div>

        <!-- Site Info -->
        <div class="site-info" :class="{ active: !isLoginFormActive }">
          <p>Welcome to Our Site! Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod justo a est facilisis, non facilisis dui ultricies.</p>
        </div>

        <!-- Buttons -->
        <div class="buttons-container">
          <button class="toggle-button" @click="toggleForm">
            {{ isLoginFormActive ? 'Create Account' : 'Back to Login' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLoginFormActive: true,
      loginEmail: "",
      loginPassword: "",
      signupName: "",
      signupEmail: "",
      signupPassword: "",
    };
  },
  methods: {
    login() {
      // Handle login using this.loginEmail and this.loginPassword
    },
    createAccount() {
      // Handle creating an account using this.signupName, this.signupEmail, and this.signupPassword
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
  margin-bottom: 20px;
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
  cursor: pointer;
  transition: background-color 0.3s;
}

.toggle-button:hover {
  background-color: #0056b3;
}

/* Site Info styles */
.site-info {
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
  text-align: center;
  color: #fff;
  background: linear-gradient(135deg, #1a0da3, #056632);
}

.site-info.active {
  display: block;
}
</style>