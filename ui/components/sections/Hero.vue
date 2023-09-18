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
  methods: {
    refreshPage() {
      window.location.reload();
    },
  },
};
</script>
New
7:23
<template>
  <section id="hero">
    <v-carousel
      height="calc(100vh - 64px)"
      dark
      cycle
      show-arrows-on-hover
      draggable="true"
      hide-delimiter-background
    >
      <v-carousel-item
        v-for="(carousel, carindex) in carouselsData"
        :key="carindex"
        :src="carousel.src"
        class="gradient-fill"
      >
        <v-container fill-height>
          <div style="max-width: 600px">
            <div
              class="text-md-h2 mb-3 text-sm-h3 text-h5 font-weight-black white--text"
            >
              {{ carousel.heading.toUpperCase() }}
            </div>
            <p class="mb-5 white--text">{{ carousel.subHeading }}</p>
            <v-btn :x-large="$vuetify.breakpoint.smAndUp" class="my-3 primary"
              >Get Started</v-btn
            >
            <span class="mx-2 my-4"></span>
            <v-btn
              :x-large="$vuetify.breakpoint.smAndUp"
              text
              class="my-3"
              outlined
              dark
              ><v-icon left large color="primary">mdi-play</v-icon>Learn
              More</v-btn
            >
          </div>
        </v-container>
      </v-carousel-item>
    </v-carousel>
  </section>
</template>

<script>
export default {
  data() {
    return {
      carouselsData: [
        {
          src: 'carousel4.jpg',
          heading: 'Explore Exotic Destinations',
          subHeading:
            "Embark on a Journey of Discovery and Uncover the World's Hidden Treasures",
        },
        {
          src: 'carousel3.jpg',
          heading: 'Plan Your Dream Vacation',
          subHeading:
            'Let Our Experts Turn Your Dream Vacation Into a Seamless, Unforgettable Reality',
        },
        {
          src: 'carousel2.jpg',
          heading: 'Discover Local Culture',
          subHeading:
            'Immerse Yourself in Authentic Experiences, From Culinary Delights to Meeting Locals',
        },
        {
          src: 'carousel1.jpg',
          heading: 'Adventure of a Lifetime',
          subHeading:
            "Get Ready for Unforgettable Thrills and Explore Nature's Wonders in the Most Thrilling Expeditions",
        },
      ],
    }
  },
}
</script>

<style>
.gradient-fill .v-responsive__content {
  background: rgb(0, 0, 0);
  background: linear-gradient(
    to right,
    rgba(3, 12, 41, 0.75),
    rgba(5, 11, 31, 0.65)
  );
}
</style>