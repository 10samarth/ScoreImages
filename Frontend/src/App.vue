<template >
  
  <div v-if="cards">
    <h1>Vote your favourite framework!</h1>
    <div>
      <Card :cards="cards[0]" v-if="cards[0]"></Card>
      <Card :cards="cards[1]" v-if="cards[1]"></Card>
    </div>
    <div>
      <Card :cards="cards[2]" v-if="cards[2]"></Card>
      <Card :cards="cards[3]" v-if="cards[3]"></Card>
    </div>
  </div>
  <div v-else>Loading data....</div>
</template>

<script>
import axios from 'axios';
import Card from './components/Card.vue'

export default {
  name: 'App',
  components: {
    Card
  },
  methods: {
    getScore() {
      const path = `${process.env.VUE_APP_URL}/cards`;
      axios.get(path)
        .then((res) => {
          this.cards = res.data.cards;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getScore();
  },
  data() {
    return {
      cards:null,
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
