<template>
    <section>
        <v-row no-gutters>
            <v-col cols="12">
                <!-- <SectionsHeroAlt :hero-alt="heroAlt" /> -->
                <v-container>
                    <v-row class="py-16">
                        <v-col cols="12">
                            <h2 class="text-h4 text-md-h3 text-center font-weight-black text-capitalize">
                                Tourist Places to Visit in {{ currentCityObj.name }}
                            </h2>
                        </v-col>
                    </v-row>
                </v-container>
                <v-row no-gutters v-for="(place, index) in cityData" :key="place.id"
                    :class="{ 'flex-row-reverse': index % 2 === 1 }">
                    <v-col cols="12" md="6" align-self="center">
                        <v-img max-height="500" :src="place.image_str" :lazy-src="place.image_str">
                        </v-img>
                    </v-col>
                    <v-col cols="12" md="6" align-self="center">
                        <div class="px-8 py-2">
                            <h2 class="text-h3 text-center font-weight-black">{{ place.name }}</h2>
                            <h3 class="text-h5 text-uppercase font-weight-thin text-center my-8">
                                {{ place.location }}
                            </h3>
                            <p>
                                {{ place.description }}
                            </p>
                        </div>
                    </v-col>
                </v-row>

            </v-col>
        </v-row>
    </section>
</template>

<script>
export default {
    props: {
        cityData: Array,
        currentCityObj: Object,
    },
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
    computed: {
    },
    head() {
        return {
            title: "About Us",
        };
    },
};
</script>
<style lang="scss" scoped>

</style>
