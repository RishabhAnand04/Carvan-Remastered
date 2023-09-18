<template>
  <section id="hero">
    <v-carousel
      height="calc(100vh - 64px)"
      dark
      cycle
      show-arrows-on-hover
      draggable="true"
      hide-delimiter-background
      interval="15000"
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
            <v-combobox
              :x-large="$vuetify.breakpoint.smAndUp"
              outlined
              dark
              label="Search Destination"
              :items="[
                'Chandigarh',
                'Shimla',
                'Manali',
                'Amritsar',
                'Kasauli',
                'Dharamshala',
              ]"
            ></v-combobox>
            <v-btn :x-large="$vuetify.breakpoint.smAndUp" class="my-3 primary"
              >Go</v-btn
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
      placesData: null,
      error: null, 
      carouselsData: [
        {
          src: "carousel4.jpg",
          heading: "Explore Exotic Destinations",
          subHeading:
            "Embark on a Journey of Discovery and Uncover the World's Hidden Treasures",
        },
        {
          src: "carousel3.jpg",
          heading: "Plan Your Dream Vacation",
          subHeading:
            "Let Our Experts Turn Your Dream Vacation Into a Seamless, Unforgettable Reality",
        },
        {
          src: "carousel2.jpg",
          heading: "Discover Local Culture",
          subHeading:
            "Immerse Yourself in Authentic Experiences, From Culinary Delights to Meeting Locals",
        },
        {
          src: "carousel1.jpg",
          heading: "Adventure of a Lifetime",
          subHeading:
            "Get Ready for Unforgettable Thrills and Explore Nature's Wonders in the Most Thrilling Expeditions",
        },
      ],
    };
  },
};
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