$("#completed_lessons").click(function () {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    var user_profile_id, course_slug, last_lesson;
    user_profile_id = $(this).attr("data-user_profile_id");
    course_slug = $(this).attr("data-course_slug");
    last_lesson = $(this).attr("data-last_lesson");

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            // if not safe, set csrftoken
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/lesson_complete/",
        data: {
            'user_profile_id': user_profile_id,
            'course_slug': course_slug,
            'last_lesson': last_lesson,
        },
        dataType: 'text',
        success: function (data) {
            if (data == 'complete'){
                console.log('lesson complete')
            }
            else if (data == 'uncomplete'){
                console.log('uncomplete')
            }
        },
        error: function () {
            console.log("bad post");
        }
    });
});