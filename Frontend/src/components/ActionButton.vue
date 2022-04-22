<template>
  <div class="btnVote">
    <button @click="updateScore">{{label}}</button>
  </div>
</template>

<script>
export default {
  name: 'ActionButton',
  props: {
    label: String
  },
  methods:{
    updateScore:function(){
        if(this.label==='+1'){
            this.result = 1
        }
        else if(this.label==='-1'){
            this.result = -1
        }
        this.emitResult()
    },
    emitResult() {
        this.$emit('btnAction', this.result)
    },
  },
  data(){
      return{
          result:0
      }
  }
}
</script>

<style scoped>
.btnVote {
  display: inline-block;
  margin: 15px;
}

button {
  padding: 12px 23px;
  border-radius: 25px;
}
</style>
