// -> url -> /login

export default function Page() {
  return (
    <div className="h-[95vh]">
      <div className="max-w-md mx-auto py-5">
        <h1>Login Here</h1>
        <form onClick>
          <input type="text" name="username" placeholder="Your Username" />
          <input type="password" name="password" placeholder="Your password" />



          <button type="submit">Login</button>
        </form>
      </div>
    </div>
  );
}
