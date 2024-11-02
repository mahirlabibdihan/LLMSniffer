public class MainActivity extends AppCompatActivity {  private EditText mNameInput;  private EditText mLocationInput;  private EditText mAboutInput;  private EditText mContact;    private ImageView mAvatarImage;  private ImageView mCoverImage;    @Override  protected void onCreate(Bundle savedInstanceState) {    super.onCreate(savedInstanceState);    setContentView(R.layout.activity_main);        mNameInput = (EditText) findViewById(R.id.input_name);    mLocationInput = (EditText) findViewById(R.id.input_location);    mAboutInput = (EditText) findViewById(R.id.input_about);    mContact = (EditText) findViewById(R.id.input_contact);        mAvatarImage = (ImageView) findViewById(R.id.avatar);    mCoverImage = (ImageView) findViewById(R.id.cover);            saveProfileAccount();  }    private void saveProfileAccount() {            String url = "http:    VolleyMultipartRequest multipartRequest = new VolleyMultipartRequest(Request.Method.POST, url, new Response.Listener<NetworkResponse>() {      @Override      public void onResponse(NetworkResponse response) {        String resultResponse = new String(response.data);        try {          JSONObject result = new JSONObject(resultResponse);          String status = result.getString("status");          String message = result.getString("message");          if (status.equals(Constant.REQUEST_SUCCESS)) {                        Log.i("Messsage", message);          } else {            Log.i("Unexpected", message);          }        } catch (JSONException e) {          e.printStackTrace();        }      }    }, new Response.ErrorListener() {      @Override      public void onErrorResponse(VolleyError error) {        NetworkResponse networkResponse = error.networkResponse;        String errorMessage = "Unknown error";        if (networkResponse == null) {          if (error.getClass().equals(TimeoutError.class)) {            errorMessage = "Request timeout";          } else if (error.getClass().equals(NoConnectionError.class)) {            errorMessage = "Failed to connect server";          }        } else {          String result = new String(networkResponse.data);          try {            JSONObject response = new JSONObject(result);            String status = response.getString("status");            String message = response.getString("message");                        Log.e("Error Status", status);            Log.e("Error Message", message);            if (networkResponse.statusCode == 404) {              errorMessage = "Resource not found";            } else if (networkResponse.statusCode == 401) {              errorMessage = message+" Please login again";            } else if (networkResponse.statusCode == 400) {              errorMessage = message+ " Check your inputs";            } else if (networkResponse.statusCode == 500) {              errorMessage = message+" Something is getting wrong";            }          } catch (JSONException e) {            e.printStackTrace();          }        }        Log.i("Error", errorMessage);        error.printStackTrace();      }    }) {      @Override      protected Map<String, String> getParams() {        Map<String, String> params = new HashMap<>();        params.put("api_token", "gh659gjhvdyudo973823tt9gvjf7i6ric75r76");        params.put("name", mNameInput.getText().toString());        params.put("location", mLocationInput.getText().toString());        params.put("about", mAboutInput.getText().toString());        params.put("contact", mContactInput.getText().toString());        return params;      }      @Override      protected Map<String, DataPart> getByteData() {        Map<String, DataPart> params = new HashMap<>();                        params.put("avatar", new DataPart("file_avatar.jpg", AppHelper.getFileDataFromDrawable(getBaseContext(), mAvatarImage.getDrawable()), "image/jpeg"));        params.put("cover", new DataPart("file_cover.jpg", AppHelper.getFileDataFromDrawable(getBaseContext(), mCoverImage.getDrawable()), "image/jpeg"));        return params;      }    };    VolleySingleton.getInstance(getBaseContext()).addToRequestQueue(multipartRequest);  }      }