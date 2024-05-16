$(document).ready(function () {
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var formData = $('form').serialize(); // Ensure this form is the correct one, possibly add an id to the form if multiple forms exist
        $.ajax({
            url: '/jobs?' + formData,
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
                                                <p><b>${d.company}</b></p>
                                                <p>${d.name}</p>
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
                console.error(error);
            }
        });
    });

    $(document).ready(function () {
        console.log('Document ready!');
        $('#filterForm').submit(function (e) {
            console.log('Apply filters clicked.');
            e.preventDefault();
            var formData = $(this).serialize(); // Serialize the form data containing the checkboxes

            $.ajax({
                url: '/jobs?' + formData,
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
                                                    <p><b>${d.company}</b></p>
                                                    <p>${d.name}</p>
                                                </div>
                                            </div>
                                            <p>Job offer expires: ${d.expires}</p>
                                        </a>
                                    </div>
                                </div>`;
                    });
                    $('.jobs').html(newHtml.join(''));
                    $('#filterModal').modal('hide'); // Close the modal
                },
                error: function () {
                    alert('Error applying filters.');
                }
            });
        });
    });
});
