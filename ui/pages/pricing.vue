<template>
  <section>
    <v-row no-gutters>
      <v-col cols="12">
        <SectionsHeroAlt :hero-alt="heroAlt" />
        <SectionsPricing />
        <SectionsBrands />
        <SectionsTestimonials />
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
          src: "pexels-andrea-piacquadio-3884440.jpg",
          heading: " Packages and Deals ",
          subHeading: "The Best in Travel: Packages and Exclusive Deals Await",
          description: "Experience the epitome of wanderlust with our handpicked travel packages and exclusive deals. From exotic getaways to thrilling adventures, embark on unforgettable journeys tailored just for you. Your dream vacation is just a click away.",
        },
      ],
    };
  },
  head() {
    return {
      title: "Pricing",
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
