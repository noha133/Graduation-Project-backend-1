package com.example.smartedu;

import com.example.smartedu.model.Admin_info;
import com.example.smartedu.model.Login;
import com.example.smartedu.model.Student_info;
import com.example.smartedu.model.Teacher_info;
import com.example.smartedu.model.User;
import com.example.smartedu.model.Users;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.Header;
import retrofit2.http.POST;
import retrofit2.http.Url;

public interface PostAPI {

    @POST("dj-rest-auth/login/")
    Call<User> login(@Body Login login);

    @GET("dj-rest-auth/user/")
    Call<Users> getPost(@Header("Authorization")  String djangoToken);

    @GET// dynamic url
    Call<UserTypeChecker> gettype(
            @Url String url
    );

    @GET// dynamic url
    Call<Student_info> getStudentInfo(
        @Url String url
        );

    @GET// dynamic url
    Call<Teacher_info> getTeacherInfo(
            @Url String url
    );

    @GET// dynamic url
    Call<Admin_info> getadminInfo(
            @Url String url
    );
}
