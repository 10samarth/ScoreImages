<template>
  <div>
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

      <div class="gap">
        <form @submit.prevent="submitComment" class="container">
          <label for="comment">Leave a Comment:</label>
          <textarea
            id="comment"
            v-model="newComment"
            rows="4"
            cols="50"
          ></textarea>
          <br />
          <button type="submit">Submit</button>
        </form>

        <div v-if="comments.length" class="container">
          <h2>Comments:</h2>
          <ul class="comments">
            <li
              v-for="(comment, index) in comments"
              :key="index"
              class="comment"
            >
              <div class="comment-header">
                <span class="comment-author">Anonymous</span>
                <span
                  class="comment-date"
                  >{{ formatDateTime(comment.timestamp) }}</span
                >
              </div>
              <div class="comment-body">{{ comment.text }}</div>
            </li>
          </ul>
        </div>
      </div>

    </div>
    <div v-else>
      Loading data....!

      
    </div>
  </div>
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
    submitComment() {
      this.comments.push({
        text: this.newComment,
        timestamp: new Date()
      });
      this.newComment = '';
    },
    formatDateTime(timestamp) {
      const date = new Date(timestamp);
      const options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };
      return date.toLocaleString('en-US', options);
    }
  },
  created() {
    this.getScore();
  },
  data() {
    return {
      cards:null,
      newComment: '',
      comments: []
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
.container {
  justify-content: space-between;
  align-content: space-between;
  align-items: center;
}

label {
  display: block;
  font-size: 1.2em;
  margin-bottom: 10px;
}

textarea {
  display: block;
  width: 95%;
  padding: 10px;
  margin-bottom: 10px;
  font-size: 1em;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin: 0 auto;
}

button {
  display: block;
  padding: 10px 20px;
  background-color: #0077cc;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 1.2em;
  cursor: pointer;
  margin: 0 auto;
}

button:hover {
  background-color: #0055aa;
}

form {
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 5px;
  margin-top: 20px;
  margin: 0 auto;
  width: 50%;
}

.comments {
  list-style: none;
  padding: 0;
  margin: 0 auto;
  width: 50%;
}

.comment {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  margin-bottom: 10px;
}

.comment-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.comment-author {
  font-weight: bold;
}

.comment-date {
  font-style: italic;
}

.comment-body {
  font-size: 1.2em;
}

.gap{
  margin-top: 80px;
}
</style>
