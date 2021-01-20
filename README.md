
<h1>Question Answer API</h1>


<h1>Functionalities Includes</h1>

<p>This application would have the following high level entities</p>
<ul>
  <li><strong>Question:</strong> Core Entity of the platform.</li>
  <li><strong>Answer:</strong> A question can have multiple answers.</li>
  <li><strong>Answer:</strong> Only staff user can give answers to a question.</li>
   <li><strong>Users:</strong> And finally the list of users who is posting Questions and Answers</li>
</ul>

## Various APIs

<ul>
  <li><strong>CRUD APIs</strong> for all master data, which includes following entities/tables.


  <li><strong>/POST </strong>Questions
    <ul>
      <li>Input
        <ul>
          <li>Question Text- Mandatory, Min length 50 char, max length 500 char.</li>
          <li>Attachement</li>
          <li>UserId - the ID of user submitting the question.</li>
        </ul>
      </li>
      <li>Output
        <ul>
          <li>ID- id of the question saved in database.</li>
        </ul>
      </li>
    </ul>
  </li>

  <li><strong>/POST </strong>Answers
    <ul>
      <li>Input
        <ul>
          <li>Question ID - Question for which answer is being submitted</li>
          <li>Answer text - Mandatory, Min length 50 char, Max length 500 char.</li>
          <li>User ID - the IS of the user submitting answer.</li>
        </ul>
      </li>
      <li>Output
        <ul>
          <li>ID - ID of answer saved in database</li>
        </ul>
      </li>
    </ul>
  </li>


  <li><strong>/GET Question </strong>Get following details of a question for a given question id.
    <ul>
      <li>Question Text</li>
      <li>List of Answers for the given question with following details.
        <ul>
          <li>Answer Text</li>
          <li>User Id of user who answered the question</li>
        </ul>
      </li>

    </ul>
  </li>
</ul>
