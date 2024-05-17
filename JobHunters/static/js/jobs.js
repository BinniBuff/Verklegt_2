$(document).ready(function () {
    console.log('Document ready!');

    // Search button click event
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        console.log('Search button clicked');

        var formData = $('#searchForm').serialize();
        console.log('Search form data:', formData);

        $.ajax({
            url: '/jobs?' + formData,
            type: 'GET',
            dataType: 'json',
            success: function (resp) {
                console.log('Search success response:', resp);
                if (resp.data) {
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
                } else {
                    console.error('Unexpected response format:', resp);
                }
                $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                console.error('Search error:', error);
            }
        });
    });

    // Filter modal initialization
    $('#filterModal').modal();

    // Filter form submit event
    $('#filterForm').submit(function (e) {
        console.log('Apply filters clicked.');
        e.preventDefault();

        var formData = $(this).serialize();
        console.log('Filter form data:', formData);

        $.ajax({
            url: '/jobs?' + formData,
            type: 'GET',
            dataType: 'json',
            success: function (resp) {
                console.log('Filter success response:', resp);
                if (resp.data) {
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
                } else {
                    console.error('Unexpected response format:', resp);
                }
                $('#filterModal').modal('hide');
            },
            error: function (xhr, status, error) {
                console.error('Filter error:', error);
                alert('Error applying filters.');
            }
        });
    });

    $('#filterModalComp').modal();

    // Company filter form submit event
    $('#filterFormComp').submit(function (e) {
        console.log('Apply company filters clicked.');
        e.preventDefault();

        var formData = $(this).serialize();
        console.log('Filter form data:', formData);

        $.ajax({
            url: '/jobs?' + formData,
            type: 'GET',
            dataType: 'json',
            success: function (resp) {
                console.log('Filter success response:', resp);
                if (resp.data) {
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
                } else {
                    console.error('Unexpected response format:', resp);
                }
                $('#filterModalComp').modal('hide');
            },
            error: function (xhr, status, error) {
                console.error('Filter error:', error);
                alert('Error applying company filters.');
            }
        });
    });

    // Order buttons click event
    $('.order-buttons button').on('click', function (e) {
        e.preventDefault();
        var orderBy = $(this).data('order-by');
        console.log('Order by:', orderBy);

        var formData = $('#searchForm').serialize() + '&order_by=' + orderBy;
        console.log('Order form data:', formData);

        $.ajax({
            url: '/jobs?' + formData,
            type: 'GET',
            dataType: 'json',
            success: function (resp) {
                console.log('Order success response:', resp);
                if (resp.data) {
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
                } else {
                    console.error('Unexpected response format:', resp);
                }
            },
            error: function (xhr, status, error) {
                console.error('Order error:', error);
            }
        });
    });
});
