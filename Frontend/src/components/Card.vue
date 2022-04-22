<template v-if="cards">
  <div class="card">
    <img alt="images" :src="require(`@/assets/${cards.image_name}`)"/>
    <div class="container grid">
      <div class="item">
        <ActionButton label="+1" @btnAction="action"></ActionButton>
        <ActionButton label="-1" @btnAction="action"></ActionButton>
      </div>
      <div>
        <ScoreLabel :cardScore="score"></ScoreLabel>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ActionButton from './ActionButton.vue'
import ScoreLabel from './Score.vue'

export default {
  name: 'CardComponent',
  components: {
    ActionButton,
    ScoreLabel
  },
  props:{
      cards: {
        card_id:String,
        image_name:String,
        score:Number
      }
  },
  methods:{
    action(value){
      this.score = this.score + value;
      const payload = {
        score: this.score,
      };
      const path =  `${process.env.VUE_APP_URL}/score/${this.cards.card_id}`;
      axios.put(path, payload)
      .catch((error) => {
        console.error(error);
      });
    }
  },
  data(){
      return{
          score: 0
      }
  },
  created(){
       this.score = this.cards.score
  }
}
</script>

<style scoped>
.card {
  width: 300px;
  height: 300px;
  display: inline-block;
  margin: 40px;
}

.item {
  width: 200px;
}

.grid {
  display: grid;
  grid-template-columns: 100px 100px;
}

.container {
  justify-content: space-between;
  align-content: space-between;
  align-items: center;
}

img {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  padding: 20px;
}
</style>
