<template>
  <section>
    <v-row no-gutters>
      <v-col cols="12">
        <SectionsHeroAlt :hero-alt="heroAlt" />
        <v-container>
          <v-row class="py-16">
            <v-col cols="12">
              <h2
                class="text-h4 text-md-h3 text-center font-weight-black text-capitalize"
              >
                Tourist Places to Visit in Chandigarh
              </h2>
              <!-- <h3
                class="text-h4 text-uppercase font-weight-thin text-center my-8"
              >
                Lorem ipsum dolor sit amet, consectetur adipisicing elit
              </h3> -->
            </v-col>
            <!-- <v-col cols="12" md="6">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat.
              </p>
              <blockquote class="text-h4 pa-5 my-4 font-weight-thin">
                …Lorem Ipsum proin gravida nibh vel velit auctor aliquet. Aenean
                sollicitudin, lorem quis
              </blockquote>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat.
              </p>
            </v-col>
            <v-col cols="12" md="6">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum.
                Sed ut perspiciatis unde omnis iste natus error sit voluptatem
                accusantium. Doloremque laudantium, totam rem aperiam, eaque
                ipsa quae ab illo inventore veritatis et quasi architecto beatae
                vitae dicta sunt explicabo. emo enim ipsam voluptatem quia
                voluptas sit aspernatur aut odit aut fugit, sed quia
                consequuntur magni dolores eos qui ratione voluptatem sequi
                nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor
                sit amet, consectetur, adipisci velit, sed quia non numquam eius
                modi tempora incidunt ut labore et dolore magnam aliquam quaerat
                voluptatem. Nemo enim ipsam voluptatem quia voluptas sit
                aspernatur aut odit aut fugit
              </p>
            </v-col> -->
          </v-row>
        </v-container>
        <!-- <SectionsTeam :our-team="ourTeam" /> -->

        <v-row no-gutters>
          <v-col cols="8" md="6" align-self="center">
            <v-img
              max-height="500"
              src="rock-garden.jpg"
              lazy-src="rock-garden.jpg"
            >
            </v-img>
          </v-col>
          <v-col cols="12" md="6" align-self="center">
            <div class="px-8 py-2">
              <h2 class="text-h3 text-center font-weight-black">Rock Garden</h2>
              <h3
                class="text-h5 text-uppercase font-weight-thin text-center my-8"
              >
                Location: Rock Garden of Chandigarh, Sector 1, Chandigarh,
                160001
              </h3>
              <p>
                Started as a hobby by the founder Nek Chand Saini in 1957, the
                Rock Garden of Chandigarh has now become one of the best tourist
                places in Chandigarh. Spread in more than 40 acres of seamlessly
                designed and decorated land, Rock Garden is embellished with
                more than 5,000 illustrations sculptures. What's more amazing is
                the fact that everything the place holds is made out of various
                industrial and urban waste.
              </p>
            </div>
          </v-col>
        </v-row>

        <v-row no-gutters class="flex-row-reverse">
          <v-col cols="12" md="6" align-self="center">
            <v-img
              max-height="500"
              src="rose-garden.jpg"
              lazy-src="rose-garden.jpg"
            >
            </v-img>
          </v-col>
          <v-col cols="12" md="6" align-self="center">
            <div class="px-8 py-2">
              <h2 class="text-h3 text-center font-weight-black">
                Zakir Hussain Rose Garden
              </h2>
              <h3
                class="text-h5 text-uppercase font-weight-thin text-center my-8"
              >
                Location: Zakir Hussain Rose Garden, Jan Marg, 16B, Sector 16,
                Chandigarh, 160016
              </h3>
              <p>
                Spread across an area of more than 30 acres of land, Zakir
                Hussain Rose Garden in Chandigarh holds some of the most elegant
                and fascinating collections of roses from India and the world.
                The garden is named and formed in the memory of India's former
                president, Zakir Hussain. Migrating from various parts of the
                country, a collection of more than 16,00 species of 50,00 rose
                plantations can be found here.
              </p>
            </div>
          </v-col>
        </v-row>

        <v-row no-gutters>
          <v-col cols="8" md="6" align-self="center">
            <v-img
              max-height="500"
              src="goverment-museum.jpg"
              lazy-src="goverment-museum.jpg"
            >
            </v-img>
          </v-col>
          <v-col cols="12" md="6" align-self="center">
            <div class="px-8 py-2">
              <h2 class="text-h3 text-center font-weight-black">
                Government Museum & Art Gallery
              </h2>
              <h3
                class="text-h5 text-uppercase font-weight-thin text-center my-8"
              >
                Location: Government Museum & Art Gallery, 502 sector, 10C,
                Chandigarh, 160011
              </h3>
              <p>
                Encapsulating an alluring history to it, Government Museum & Art
                Gallery was brought into existence along with the partition of
                India in 1947. Before partition, the properties inside the
                museum were decorated in the Central Museum. However, post
                partition, up to 6% of all the properties in Central Museum was
                adopted by Pakistan, others shifted to Government Museum & Art
                Gallery of Chandigarh.
              </p>
            </div>
          </v-col>
        </v-row>

        <v-row no-gutters class="flex-row-reverse">
          <v-col cols="12" md="6" align-self="center">
            <v-img
              max-height="500"
              src="sukhna-lake.jpg"
              lazy-src="sukhna-lake.jpg"
            >
            </v-img>
          </v-col>
          <v-col cols="12" md="6" align-self="center">
            <div class="px-8 py-2">
              <h2 class="text-h3 text-center font-weight-black">Sukhna Lake</h2>
              <h3
                class="text-h5 text-uppercase font-weight-thin text-center my-8"
              >
                Location: Sukhna Lake, Sector 1, Chandigarh 160001, India
              </h3>
              <p>
                The gorgeous Sukhna Lake, found in Chandigarh, was brought into
                existence by damming the Sukhna Chole in 1958. Strearched in 3
                km, the lake is encompassed with sparkling water, boats and
                serves as home for a number of birds including the Siberian duck
                and the crane.
              </p>
            </div>
          </v-col>
        </v-row>

        <!-- <SectionsTimeline /> -->
      </v-col>
    </v-row>
  </section>
</template>

<script>
export default {
  data() {
    return {
      heroAlt: [
        {
          src: "pexels-moose-photos-1036641.jpg",
          heading: " Chandigarh ",
          subHeading: "The most affordable pricing",
          description: "lorem about",
        },
      ],
      ourTeam: [
        {
          name: "John Churchill",
          position: "Marketing Director",
          phone: "+1 (987) 1625346",
          email: "john@example.com",
          photo: "person-1.jpg",
        },
        {
          name: "Fiona	Ross",
          position: "Project Manager",
          phone: "+1 (987) 5894684",
          email: "fiona@example.com",
          photo: "person-2.jpg",
        },
        {
          name: "Justin	Rees",
          position: "VP Marketing",
          phone: "+1 (987) 6982456",
          email: "justin@example.com",
          photo: "person-3.jpg",
        },
        {
          name: "Amelia	Ogden",
          position: "Communication Manager",
          phone: "+1 (987) 6982456",
          email: "amelia@example.com",
          photo: "person-4.jpg",
        },
        {
          name: "Sebastian Bailey",
          position: "Advertising Director",
          phone: "+1 (987) 6982456",
          email: "sebastian@example.com",
          photo: "person-5.jpg",
        },
        {
          name: "Eric Sutton",
          position: "Advertising Executive",
          phone: "+1 (987) 6982456",
          email: "audrey@example.com",
          photo: "person-6.jpg",
        },
        {
          name: "Xia Yen",
          position: "Advertising Manager",
          phone: "+1 (987) 6982456",
          email: "christian@example.com",
          photo: "person-7.jpg",
        },
        {
          name: "Bernadette	Springer",
          position: "Employee Relations Manager",
          phone: "+1 (987) 6982456",
          email: "bernadette@example.com",
          photo: "person-8.jpg",
        },
        {
          name: "Elizabeth Newman",
          position: "Project Manager",
          phone: "+1 (987) 6982456",
          email: "elizabeth@example.com",
          photo: "person-9.jpg",
        },
      ],
    };
  },
  head() {
    return {
      title: "About Us",
      meta: [
        {
          hid: "description",
          name: "description",
          content:
            "Infographic hypotheses influencer user experience Long madel ture gen-z paradigm shift client partner network product seilans solve management influencer analytics leverage virality. incubator seed round massmarket. buyer agile development growth hacking business-to-consumer ecosystem",
        },
      ],
    };
  },
};
</script>
