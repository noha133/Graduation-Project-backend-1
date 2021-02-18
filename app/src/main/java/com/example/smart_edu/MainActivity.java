package com.example.smart_edu;

import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.smart_edu.model.Login;
import com.example.smart_edu.model.User;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class MainActivity extends AppCompatActivity {

    EditText username, password;
    Button loginBttn;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login);

        username = findViewById(R.id.username_text);
        password = findViewById(R.id.Password_text);
        loginBttn = findViewById(R.id.login_button);
        loginBttn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(TextUtils.isEmpty(username.getText().toString()) || TextUtils.isEmpty(password.getText().toString())){
                    Toast.makeText(MainActivity.this, "Username / password Required",Toast.LENGTH_LONG).show();
                }else{
                    login();
                }

            }
        });
    }
    public void login(){
        Login loginrequest = new Login(username.getText().toString(), password.getText().toString());

        Call <User> userresponse = ApiClient.getPostAPI().login(loginrequest);
        userresponse.enqueue(new Callback<User>() {
            @Override
            public void onResponse(Call<User> call, Response<User> response) {
                if(response.isSuccessful()){
                    Toast.makeText(MainActivity.this,"Login success", Toast.LENGTH_LONG).show();
                }else {
                    Toast.makeText(MainActivity.this,"Login failed", Toast.LENGTH_LONG).show();
                }
            }

            @Override
            public void onFailure(Call<User> call, Throwable t) {
                Toast.makeText(MainActivity.this,"Failed "+t.getLocalizedMessage(), Toast.LENGTH_LONG).show();
            }
        });
    }
}