<template>
  <section class="primary darken-1 white--text py-16">
    <v-container>
      <v-row>
        <v-col class="text-center">
          <h2 class="text-h4 text-md-h3 text-center font-weight-black mb-2">
            Our top visited destinations
          </h2>
        </v-col>
      </v-row>
      <v-row>
        <v-col
          v-for="(card, index) in cards"
          :key="index"
          cols="12"
          sm="4"
          class="text-center"
        >
          <v-avatar size="128" class="mb-7">
              <img
                :src="`${card.img}`"
                alt="John"
                width="128"
                height="128"
              />
            </v-avatar>
          <div class="title text-uppercase mt-1 mb-4" v-text="card.title"></div>

          <p v-text="card.text"></p>
          <v-row no-gutters>
            <v-col cols="12"> </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<script>
export default {
  data() {
    return {
      cards: [
        {
          title: 'Chandigarh',
          subtitle: 'Best Productivity',
          text: 'Chandigarh, known for its meticulously planned architecture and lush green gardens, offers tourists a serene blend of urban sophistication and natural beauty.',
          callout: '01',
          img: 'Chandigarh image.jpg'
        },
        {
          title: 'Shimla',
          subtitle: 'Special Offers',
          text: 'Shimla, nestled in the Himalayas, is a captivating hill station known for its scenic beauty, colonial architecture, and a serene escape for tourists seeking cool climate and breathtaking vistas.',
          callout: '02',
          img: 'shimla 2.jpeg'
        },
        {
          title: 'Manali',
          subtitle: 'Income Flow',
          text: 'Manali, nestled in the Himalayas, is a popular tourist destination known for its stunning landscapes, adventurous activities, and vibrant culture.',
          callout: '03',
          img: 'manali 1.jpg'
        },
      ],
    }
  },
}
</script>
