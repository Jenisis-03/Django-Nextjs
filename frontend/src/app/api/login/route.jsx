"use server";
import { cookies } from "next/headers";
import { NextResponse } from "next/server";

const DJANGO_LOGIN_URL = "http://127.0.0.1:8001/api/token/pair";

export async function POST(request) {
  // Get the auth token from cookies
  const myAuthToken = cookies().get('auth-token');
  console.log(myAuthToken);

  // Parse the incoming request data
  const requestData = await request.json();
  console.log(requestData); // Fixed variable name here

  const jsonData = JSON.stringify(requestData);

  // Prepare request options for the API call
  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: jsonData,
  };

  try {
    // Make the API request
    const response = await fetch(DJANGO_LOGIN_URL, requestOptions);

    if (response.ok) {
      const responseData = await response.json();
      console.log("Login Successful");

      // Get the authentication token from the response
      const authToken = responseData.access; // Make sure this matches the API response

      // Set the new cookie
      cookies().set({
        name: "abc",
        value: authToken,
        httpOnly: true,
        sameSite: "strict",
        secure: process.env.NODE_ENV !== "development",
        maxAge: 3600, // 1 hour
      });

      return NextResponse.json({ message: "Login successful", authToken }, { status: 200 });
    } else {
      console.error("Login failed");
      return NextResponse.json({ message: "Login failed" }, { status: response.status });
    }
  } catch (error) {
    console.error("An error occurred", error);
    return NextResponse.json({ message: "An error occurred" }, { status: 500 });