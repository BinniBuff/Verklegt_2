$(document).ready(function () {
   $('#search-btn').on('click', function (e) {
       e.preventDefault();
       var searchText = $('#search-box').val();
       $.ajax({
           url: '/jobs?search_filter=' + searchText,
           type: 'GET',
           success: function (resp) {
               var newHtml = resp.data.map(d => {
                   return `<div class="col-md-5" id="single_job_div">
                               <div class="well-job">
                                   <a href="/jobs/${d.id}" id="link_to_job">
                                       <div class="row">
                                           <div class="col-md-4">
                                               <p>${d.category}</p>
                                           </div>
                                           <div class="col-md-8 text-end">
                                               <p><b>${d.full_part_time}</b></p>
                                           </div>
                                       </div>
                                       <div class="row">
                                           <div class="col-md-8">
                                               <div class="row">
                                                   <p><b>${d.company}</b></p>
                                               </div>
                                               <div class="row">
                                                   <p>${d.name}</p>
                                               </div>
                                           </div>
                                           <div class="col-md-4">
                                               <!-- Image may need a URL or path -->
                                           </div>
                                       </div>
                                       <p>Job offer expires: ${d.expires}</p>
                                   </a>
                               </div>
                           </div>`;
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
