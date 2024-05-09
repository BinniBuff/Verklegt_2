$(document).ready(function () {
   $('#search-btn').on('click', function (e) {
       e.preventDefault();
       var searchText = $('#search-box').val();
       $.ajax({
           url: '/jobs?search_filter=' + searchText,
           type: 'GET',
           success: function (resp) {
               var new_html = resp.data.map(d => {
                   return '<div class="well job">
                       <a href="/jobs/${d.id}">
                            <h1>${d.name}</h1>
                            <h4>${d.company}</h4>
                            <p>${d.description}</p>
                            <p>${d.date_expired}</p>
                       </a>
                       </div>'
               });
               $('.jobs').html(newHtml.join(''));
               $('#search-box').val('');
           },
           error: function (xhr, status, error) {
               console.error(error)
           }
       })
   });
});