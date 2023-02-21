<template>
  <div class="btnVote">
    <button @click="updateScore" :disabled="isSubmitting">{{label}}</button>
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
        this.isSubmitting = true;
        setTimeout(() => {
        this.isSubmitting = false;
      }, 8000);
    },
    emitResult() {
        this.$emit('btnAction', this.result)
    },
  },
  data(){
      return{
          result:0,
          isSubmitting: false
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

button:disabled {
  background-color: #ccc;
  color: #666;
  cursor: not-allowed;
}
</style>
