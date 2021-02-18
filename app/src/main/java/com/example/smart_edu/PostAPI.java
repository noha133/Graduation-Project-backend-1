package com.example.smart_edu;

import com.example.smart_edu.model.Login;
import com.example.smart_edu.model.User;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;
public interface PostAPI {


//    String root = "http://nohamagdy.pythonanywhere.com/";
////    String root = "http://127.0.0.1:8000/";
//
//
//    String base_local = root + "api/v1/";
//    String BASE_URL = base_local + "account/";
//    String POST_URL = base_local + "post/";
//    String API_URL = root + "api/v1/";



    @POST("dj-rest-auth/login/")
    Call<User> login(@Body Login login);
}

