<template>
  <v-form>
    <v-row class="mb-n6">
      <v-col><v-text-field label="Name" dense outlined></v-text-field></v-col>
      <v-col><v-text-field label="Email" dense outlined></v-text-field></v-col>
    </v-row>

    <v-row class="mb-n6">
      <v-col
        ><v-text-field label="Subject" dense outlined></v-text-field
      ></v-col>
    </v-row>
    <v-row class="mb-n6">
      <v-col>
        <v-textarea
          dense
          label="Your Message"
          auto-grow
          outlined
          rows="8"
          row-height="20"
        ></v-textarea>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        ><v-btn @click="snackbar = true" class="my-2" color="primary">SEND MESSAGE</v-btn
        ><v-btn class="my-2 ml-3">clear</v-btn></v-col
      >
    </v-row>
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