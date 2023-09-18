<template>
    <div>
        <SectionsCity :city-data="cityData" :current-city-obj="currentCityObj"></SectionsCity>
    </div>
</template>

<script>
export default {
    data() {
        return {
            name: 'Chandigarh',
            cityData: null,
            allPlaces: [], 
            currentCityObj: {},
        };
    },
    created() {
        this.getPlaces();
        this.getCityData();
    },
    methods: {
        async getPlaces() {
            try {
                const response = await fetch('http://127.0.0.1:8000/api/Places');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                this.allPlaces = data;
                this.currentCityObj = this.allPlaces.find(city => city.name === 'Chandigarh');
            } catch (error) {
                console.error('Error fetching places:', error);
            }
        },
        async getCityData() {
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/Visiting`);
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                const data = await response.json();
                this.cityData = data;
            } catch (error) {
                console.error("Error fetching places:", error);
            }
        },
    },
};
</script>

<style></style>