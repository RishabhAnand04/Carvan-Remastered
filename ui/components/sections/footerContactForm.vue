<template>
  <v-form>
    <v-text-field label="Name" dense outlined></v-text-field>
    <v-text-field label="Email" dense outlined></v-text-field>
    <v-text-field label="Subject" dense outlined></v-text-field>
    <v-textarea
      dense
      label="Your Message"
      auto-grow
      outlined
      rows="8"
      row-height="20"
    ></v-textarea>
    <v-btn @click="snackbar = true" outlined block color="primary"
      >SEND MESSAGE</v-btn
    >
    <v-snackbar
      v-model="snackbar"
      :timeout="-1"
      :dark="$vuetify.theme.dark"
      :light="!$vuetify.theme.dark"
    >
      {{ text }}
      <template v-slot:action="{ attrs }">
        <v-btn
          color="primary ml-3"
          small
          v-bind="attrs"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-form>
</template>

<script>
export default {
    data() {
    return {
      snackbar: false,
      text: `Succesfully Sent`,
    }
  },
  components: {
  },
};
</script>