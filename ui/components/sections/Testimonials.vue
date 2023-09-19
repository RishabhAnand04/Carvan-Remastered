<template>
  <section
    id="testimonials"
    :class="$vuetify.theme.dark ? 'black' : 'white'"
    class="py-16"
  >
    <h2 class="text-h4 text-md-h3 text-center font-weight-black mb-8 my-8">
      Customer Reviews
    </h2>
    <v-carousel
      cycle
      draggable="true"
      hide-delimiter-background
      hide-delimiters
    >
      <v-carousel-item v-for="(item, i) in testimonials" :key="i" class="">
        <v-container fill-height>
          <div style="max-width: 700px" class="mx-auto text-center">
            <v-avatar size="128" class="mb-7">
              <img
                :src="`/team/${item.avtar}`"
                alt="John"
                width="128"
                height="128"
              />
            </v-avatar>
            <h3
              :class="
                $vuetify.theme.dark
                  ? 'black'
                  : 'white grey--text text--darken-2'
              "
              class="mb-1 font-weight-black text-uppercase"
            >
              {{ item.name }}
            </h3>
            <div class="mb-10 font-weight-light grey--text text-uppercase">
              {{ item.post }}
            </div>
            <v-row>
              <v-col cols="1"
                ><v-icon x-large class="grey--text text--lighten-1"
                  >mdi-format-quote-open</v-icon
                ></v-col
              >
              <v-col cols="10">
                <div
                  :class="
                    $vuetify.theme.dark
                      ? 'black'
                      : 'white grey--text text--darken-2'
                  "
                  class="mb-5 font-italic"
                >
                  {{ item.review }}
                </div>
              </v-col>
              <v-col cols="1"
                ><v-icon x-large class="grey--text text--lighten-1"
                  >mdi-format-quote-close</v-icon
                ></v-col
              >
            </v-row>
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
      testimonials: [
        {
          avtar: 'sahil.png',
          name: 'Sahil Jaura',
          post: 'Student, PEC',
          review: "What an incredible resource! Your website made planning our family vacation a breeze. The comprehensive destination guides and personalized itineraries ensured we didn't miss a thing. Thank you for helping us create unforgettable memories!",
        },
        {
          avtar: 'rishabh.jpeg',
          name: 'Rishabh Anand',
          post: 'SDE-1 Amadeus Labs',
          review: "I'm a seasoned traveler, and I must say, your website is a gem. It's not just about the destinations; it's about the passion and expertise you bring to the table. The local culture insights and adventure recommendations added a whole new layer of excitement to our trips. Truly exceptional!",
        },
        {
          avtar: 'anshul.png',
          name: 'Anshul Banwala',
          post: 'PM India',
          review: "I stumbled upon your website while searching for off-the-beaten-path experiences, and I couldn't be happier. The 'Discover Local Culture' section is a treasure trove of unique activities and hidden gems. Thanks for inspiring me to explore new horizons and embrace the world's diversity!",
        },
        {
          avtar: 'adhiyyan.jpeg',
          name: 'Adhiyyan Kapoolia',
          post: 'STGI Employee',
          review: "Kudos to your team for curating such a diverse range of travel experiences. The 'Adventure of a Lifetime' section was a game-changer for me. From thrilling expeditions to serene nature escapes, your website has it all. I'm hooked and can't wait for my next adventure!",
        }
      ],
    }
  },
}
</script>