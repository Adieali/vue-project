<template>
  <div class="container mt-3">
    <div class="row">
      <div class="col">
        <p class="h3 text-success fw-bold">Add Contact</p>
        <p class="fst-italic">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Deserunt explicabo quae minus mollitia, obcaecati sed quidem! Iure facere aspernatur blanditiis quam sed voluptate dolor esse incidunt delectus quos! Mollitia, voluptatem?</p>
      </div>
    </div>
  </div>
  <div class="container mt-3">
    <div class="row">
      <div class="col-md-4">
        <form @submit.prevent="submitCreate()">
          <div class="mb-2">
            <input v-model="contact.name" type="text" class="form-control" placeholder="Name" required="true">
          </div>
          <div class="mb-2">
            <input v-model="contact.photo" type="text" class="form-control" placeholder="Photo URL" required="true">
          </div>
          <div class="mb-2">
            <input v-model="contact.email" type="text" class="form-control" placeholder="Email" required="true">
          </div>
          <div class="mb-2">
            <input v-model="contact.mobile" type="number" class="form-control" placeholder="Mobile" required="true">
          </div>
          <div class="mb-2">
            <input v-model="contact.company" type="text" class="form-control" placeholder="Company" required="true">
          </div>
          <div class="mb-2">
            <input v-model="contact.title" type="text" class="form-control" placeholder="Title" required="true">
          </div>
          <div class="mb-2">
            <select v-model="contact.groupId" class="form-control" v-if="groups.length > 0" required="true">
              <option value="">Select Group</option>
              <option :value="group.id" v-for="group of groups" :key="group.id">{{group.name}}</option>
            </select>
          </div>
          <div class="mb-2">
            <input type="submit" class="btn btn-success" value="Create">
          </div>
        </form>
      </div>
      <div class="col-md-4">
        <img :src="contact.photo" alt="" class="contact-img">
      </div>
    </div>
  </div>
</template>
  
<script>
import { ContactService } from '@/services/ContactService';

    export default {
      name: 'AddContact',
      data: function (){
        return {
          contact : {
            name : '',
            photo : '',
            email : '',
            company : '',
            title : '',
            groupId : '',
          },
          groups : []
        }
      },
      created : async function (){
        try {
          let response = await ContactService.getAllGroups();
          this.groups = response.data;
        } catch (error) {
            console.log(error);
        }
      },
      methods : {
        submitCreate : async function (){
          try {
            let response = await ContactService.createContact(this.contact);
            if(response){
              return this.$router.push('/');
            }
            else{
              return this.$router.push('/contacts/add');
            }
          } catch (error) {
              console.log(error);
          }
        }
      }
    }
</script>

<style scoped>
    
</style>
  