<template>
  <p>Score :{{cardScore}}</p>
</template>

<script>
export default {
  name: 'ScoreLabel',
  props: {
    cardScore: Number
  }
}
</script>

<style scoped>
</style>