# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class 3WCity(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=765)
    region = models.CharField(max_length=765)
    country = models.CharField(max_length=765)
    last_updated = models.IntegerField()
    class Meta:
        db_table = u'3w_city'

class 3WCityWether(models.Model):
    city_id = models.IntegerField()
    date = models.IntegerField()
    hour = models.IntegerField()
    cloud = models.IntegerField()
    tmin = models.IntegerField()
    tmax = models.IntegerField()
    pmin = models.IntegerField()
    pmax = models.IntegerField()
    windmin = models.IntegerField()
    windmax = models.IntegerField()
    windrumb = models.IntegerField()
    hmidmin = models.IntegerField()
    hmidmax = models.IntegerField()
    wpi = models.IntegerField()
    class Meta:
        db_table = u'3w_city_wether'

class CpDescription(models.Model):
    cp_id = models.IntegerField(primary_key=True)
    cp_title = models.CharField(max_length=765)
    cp_type = models.CharField(max_length=150)
    cp_date = models.IntegerField()
    cp_path = models.TextField()
    cp_meet = models.TextField()
    cp_start = models.IntegerField()
    cp_kilometrage = models.CharField(max_length=765, blank=True)
    cp_finish_time = models.IntegerField()
    cp_finish_place = models.CharField(max_length=765, blank=True)
    cp_asphalt_ratio = models.CharField(max_length=765, blank=True)
    cp_speed = models.CharField(max_length=765, blank=True)
    cp_kit = models.CharField(max_length=765, blank=True)
    cp_connection = models.CharField(max_length=765, blank=True)
    cp_other = models.TextField(blank=True)
    cp_owner = models.IntegerField(null=True, blank=True)
    cp_status = models.IntegerField(null=True, blank=True)
    cp_post_id = models.IntegerField(null=True, blank=True)
    cp_weather = models.TextField(blank=True)
    cp_weather_checked = models.IntegerField(null=True, blank=True)
    cp_last_modified = models.IntegerField()
    cp_commercial = models.IntegerField()
    cp_only_to_friends = models.IntegerField()
    class Meta:
        db_table = u'cp_description'

class CpTypes(models.Model):
    cp_type_id = models.IntegerField(primary_key=True)
    cp_type_title = models.CharField(max_length=765)
    cp_type_title_short = models.CharField(max_length=165)
    cp_post_forum = models.IntegerField()
    cp_show_title = models.IntegerField()
    cp_show_type = models.IntegerField()
    cp_show_type_short = models.IntegerField()
    cp_show_date = models.IntegerField()
    cp_show_path = models.IntegerField()
    cp_show_meet = models.IntegerField()
    cp_show_start = models.IntegerField()
    cp_show_kilometrage = models.IntegerField()
    cp_show_finish_time = models.IntegerField()
    cp_show_finish_place = models.IntegerField()
    cp_show_asphalt_ratio = models.IntegerField()
    cp_show_speed = models.IntegerField()
    cp_show_kit = models.IntegerField()
    cp_show_connection = models.IntegerField()
    cp_show_other = models.IntegerField()
    cp_show_commercial = models.IntegerField()
    class Meta:
        db_table = u'cp_types'

class CpUsers(models.Model):
    cp_users_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    cp_id = models.IntegerField(null=True, blank=True)
    cp_role = models.IntegerField(null=True, blank=True)
    user_date = models.IntegerField()
    additional_p = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'cp_users'

class Dual(models.Model):
    x = models.CharField(max_length=3)
    class Meta:
        db_table = u'dual'

class Mappoint(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    descriptions = models.CharField(max_length=765)
    cx = models.CharField(max_length=30)
    cy = models.CharField(max_length=30)
    user = models.CharField(max_length=765)
    view = models.IntegerField()
    class Meta:
        db_table = u'mappoint'

class PhpbbAclGroups(models.Model):
    group_id = models.IntegerField()
    forum_id = models.IntegerField()
    auth_option_id = models.IntegerField()
    auth_role_id = models.IntegerField()
    auth_setting = models.IntegerField()
    class Meta:
        db_table = u'phpbb_acl_groups'

class PhpbbAclOptions(models.Model):
    auth_option_id = models.IntegerField(primary_key=True)
    auth_option = models.CharField(unique=True, max_length=150)
    is_global = models.IntegerField()
    is_local = models.IntegerField()
    founder_only = models.IntegerField()
    class Meta:
        db_table = u'phpbb_acl_options'

class PhpbbAclRoles(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=765)
    role_description = models.TextField()
    role_type = models.CharField(max_length=30)
    role_order = models.IntegerField()
    class Meta:
        db_table = u'phpbb_acl_roles'

class PhpbbAclRolesData(models.Model):
    role_id = models.IntegerField(primary_key=True)
    auth_option_id = models.IntegerField()
    auth_setting = models.IntegerField()
    class Meta:
        db_table = u'phpbb_acl_roles_data'

class PhpbbAclUsers(models.Model):
    user_id = models.IntegerField()
    forum_id = models.IntegerField()
    auth_option_id = models.IntegerField()
    auth_role_id = models.IntegerField()
    auth_setting = models.IntegerField()
    class Meta:
        db_table = u'phpbb_acl_users'

class PhpbbAttachments(models.Model):
    attach_id = models.IntegerField(primary_key=True)
    post_msg_id = models.IntegerField()
    topic_id = models.IntegerField()
    in_message = models.IntegerField()
    poster_id = models.IntegerField()
    is_orphan = models.IntegerField()
    physical_filename = models.CharField(max_length=765)
    real_filename = models.CharField(max_length=765)
    download_count = models.IntegerField()
    attach_comment = models.TextField()
    extension = models.CharField(max_length=300)
    mimetype = models.CharField(max_length=300)
    filesize = models.IntegerField()
    filetime = models.IntegerField()
    thumbnail = models.IntegerField()
    class Meta:
        db_table = u'phpbb_attachments'

class PhpbbBanlist(models.Model):
    ban_id = models.IntegerField(primary_key=True)
    ban_userid = models.IntegerField()
    ban_ip = models.CharField(max_length=120)
    ban_email = models.CharField(max_length=300)
    ban_start = models.IntegerField()
    ban_end = models.IntegerField()
    ban_exclude = models.IntegerField()
    ban_reason = models.CharField(max_length=765)
    ban_give_reason = models.CharField(max_length=765)
    class Meta:
        db_table = u'phpbb_banlist'

class PhpbbBbcodes(models.Model):
    bbcode_id = models.IntegerField(primary_key=True)
    bbcode_tag = models.CharField(max_length=48)
    bbcode_helpline = models.CharField(max_length=765)
    display_on_posting = models.IntegerField()
    bbcode_match = models.TextField()
    bbcode_tpl = models.TextField()
    first_pass_match = models.TextField()
    first_pass_replace = models.TextField()
    second_pass_match = models.TextField()
    second_pass_replace = models.TextField()
    class Meta:
        db_table = u'phpbb_bbcodes'

class PhpbbBookmarks(models.Model):
    topic_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'phpbb_bookmarks'

class PhpbbBots(models.Model):
    bot_id = models.IntegerField(primary_key=True)
    bot_active = models.IntegerField()
    bot_name = models.CharField(max_length=765)
    user_id = models.IntegerField()
    bot_agent = models.CharField(max_length=765)
    bot_ip = models.CharField(max_length=765)
    class Meta:
        db_table = u'phpbb_bots'

class PhpbbCaptchaAnswers(models.Model):
    question_id = models.IntegerField()
    answer_text = models.CharField(max_length=765)
    class Meta:
        db_table = u'phpbb_captcha_answers'

class PhpbbCaptchaQuestions(models.Model):
    question_id = models.IntegerField(primary_key=True)
    strict = models.IntegerField()
    lang_id = models.IntegerField()
    lang_iso = models.CharField(max_length=90)
    question_text = models.TextField()
    class Meta:
        db_table = u'phpbb_captcha_questions'

class PhpbbConfig(models.Model):
    config_name = models.CharField(max_length=765, primary_key=True)
    config_value = models.CharField(max_length=765)
    is_dynamic = models.IntegerField()
    class Meta:
        db_table = u'phpbb_config'

class PhpbbConfirm(models.Model):
    confirm_id = models.CharField(max_length=96, primary_key=True)
    session_id = models.CharField(max_length=96, primary_key=True)
    confirm_type = models.IntegerField()
    code = models.CharField(max_length=24)
    seed = models.IntegerField()
    attempts = models.IntegerField()
    class Meta:
        db_table = u'phpbb_confirm'

class PhpbbDisallow(models.Model):
    disallow_id = models.IntegerField(primary_key=True)
    disallow_username = models.CharField(max_length=765)
    class Meta:
        db_table = u'phpbb_disallow'

class PhpbbDrafts(models.Model):
    draft_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    topic_id = models.IntegerField()
    forum_id = models.IntegerField()
    save_time = models.IntegerField()
    draft_subject = models.CharField(max_length=765)
    draft_message = models.TextField()
    class Meta:
        db_table = u'phpbb_drafts'

class PhpbbExtensionGroups(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=765)
    cat_id = models.IntegerField()
    allow_group = models.IntegerField()
    download_mode = models.IntegerField()
    upload_icon = models.CharField(max_length=765)
    max_filesize = models.IntegerField()
    allowed_forums = models.TextField()
    allow_in_pm = models.IntegerField()
    class Meta:
        db_table = u'phpbb_extension_groups'

class PhpbbExtensions(models.Model):
    extension_id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    extension = models.CharField(max_length=300)
    class Meta:
        db_table = u'phpbb_extensions'

class PhpbbForums(models.Model):
    forum_id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    left_id = models.IntegerField()
    right_id = models.IntegerField()
    forum_parents = models.TextField()
    forum_name = models.CharField(max_length=765)
    forum_desc = models.TextField()
    forum_desc_bitfield = models.CharField(max_length=765)
    forum_desc_options = models.IntegerField()
    forum_desc_uid = models.CharField(max_length=24)
    forum_link = models.CharField(max_length=765)
    forum_password = models.CharField(max_length=120)
    forum_style = models.IntegerField()
    forum_image = models.CharField(max_length=765)
    forum_rules = models.TextField()
    forum_rules_link = models.CharField(max_length=765)
    forum_rules_bitfield = models.CharField(max_length=765)
    forum_rules_options = models.IntegerField()
    forum_rules_uid = models.CharField(max_length=24)
    forum_topics_per_page = models.IntegerField()
    forum_type = models.IntegerField()
    forum_status = models.IntegerField()
    forum_posts = models.IntegerField()
    forum_topics = models.IntegerField()
    forum_topics_real = models.IntegerField()
    forum_last_post_id = models.IntegerField()
    forum_last_poster_id = models.IntegerField()
    forum_last_post_subject = models.CharField(max_length=765)
    forum_last_post_time = models.IntegerField()
    forum_last_poster_name = models.CharField(max_length=765)
    forum_last_poster_colour = models.CharField(max_length=18)
    forum_flags = models.IntegerField()
    display_subforum_list = models.IntegerField()
    display_on_index = models.IntegerField()
    enable_indexing = models.IntegerField()
    enable_icons = models.IntegerField()
    enable_prune = models.IntegerField()
    prune_next = models.IntegerField()
    prune_days = models.IntegerField()
    prune_viewed = models.IntegerField()
    prune_freq = models.IntegerField()
    forum_options = models.IntegerField()
    topic_list_order = models.CharField(max_length=3)
    topic_list_dir = models.CharField(max_length=3)
    user_sort_override = models.IntegerField()
    forum_sponsor = models.TextField()
    forum_sponsor_html = models.IntegerField()
    forum_sponsor_uid = models.CharField(max_length=24)
    forum_sponsor_bitfield = models.CharField(max_length=765)
    forum_sponsor_options = models.IntegerField()
    forum_subforumslist_type = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'phpbb_forums'

class PhpbbForumsAccess(models.Model):
    forum_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(primary_key=True)
    session_id = models.CharField(max_length=96, primary_key=True)
    class Meta:
        db_table = u'phpbb_forums_access'

class PhpbbForumsTagcategories(models.Model):
    forum_id = models.IntegerField()
    category_id = models.IntegerField()
    class Meta:
        db_table = u'phpbb_forums_tagcategories'

class PhpbbForumsTrack(models.Model):
    user_id = models.IntegerField(primary_key=True)
    forum_id = models.IntegerField(primary_key=True)
    mark_time = models.IntegerField()
    class Meta:
        db_table = u'phpbb_forums_track'

class PhpbbForumsWatch(models.Model):
    forum_id = models.IntegerField()
    user_id = models.IntegerField()
    notify_status = models.IntegerField()
    class Meta:
        db_table = u'phpbb_forums_watch'

class PhpbbGroups(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_type = models.IntegerField()
    group_founder_manage = models.IntegerField()
    group_name = models.CharField(max_length=765)
    group_desc = models.TextField()
    group_desc_bitfield = models.CharField(max_length=765)
    group_desc_options = models.IntegerField()
    group_desc_uid = models.CharField(max_length=24)
    group_display = models.IntegerField()
    group_avatar = models.CharField(max_length=765)
    group_avatar_type = models.IntegerField()
    group_avatar_width = models.IntegerField()
    group_avatar_height = models.IntegerField()
    group_rank = models.IntegerField()
    group_colour = models.CharField(max_length=18)
    group_sig_chars = models.IntegerField()
    group_receive_pm = models.IntegerField()
    group_message_limit = models.IntegerField()
    group_max_recipients = models.IntegerField()
    group_legend = models.IntegerField()
    group_skip_auth = models.IntegerField()
    class Meta:
        db_table = u'phpbb_groups'

class PhpbbIcons(models.Model):
    icons_id = models.IntegerField(primary_key=True)
    icons_url = models.CharField(max_length=765)
    icons_width = models.IntegerField()
    icons_height = models.IntegerField()
    icons_order = models.IntegerField()
    display_on_posting = models.IntegerField()
    class Meta:
        db_table = u'phpbb_icons'

class PhpbbLang(models.Model):
    lang_id = models.IntegerField(primary_key=True)
    lang_iso = models.CharField(max_length=90)
    lang_dir = models.CharField(max_length=90)
    lang_english_name = models.CharField(max_length=300)
    lang_local_name = models.CharField(max_length=765)
    lang_author = models.CharField(max_length=765)
    class Meta:
        db_table = u'phpbb_lang'

class PhpbbLog(models.Model):
    log_id = models.IntegerField(primary_key=True)
    log_type = models.IntegerField()
    user_id = models.IntegerField()
    forum_id = models.IntegerField()
    topic_id = models.IntegerField()
    reportee_id = models.IntegerField()
    log_ip = models.CharField(max_length=120)
    log_time = models.IntegerField()
    log_operation = models.TextField()
    log_data = models.TextField()
    class Meta:
        db_table = u'phpbb_log'

class PhpbbModeratorCache(models.Model):
    forum_id = models.IntegerField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=765)
    group_id = models.IntegerField()
    group_name = models.CharField(max_length=765)
    display_on_index = models.IntegerField()
    class Meta:
        db_table = u'phpbb_moderator_cache'

class PhpbbModules(models.Model):
    module_id = models.IntegerField(primary_key=True)
    module_enabled = models.IntegerField()
    module_display = models.IntegerField()
    module_basename = models.CharField(max_length=765)
    module_class = models.CharField(max_length=30)
    parent_id = models.IntegerField()
    left_id = models.IntegerField()
    right_id = models.IntegerField()
    module_langname = models.CharField(max_length=765)
    module_mode = models.CharField(max_length=765)
    module_auth = models.CharField(max_length=765)
    class Meta:
        db_table = u'phpbb_modules'

class PhpbbPollOptions(models.Model):
    poll_option_id = models.IntegerField()
    topic_id = models.IntegerField()
    poll_option_text = models.TextField()
    poll_option_total = models.IntegerField()
    class Meta:
        db_table = u'phpbb_poll_options'

class PhpbbPollVotes(models.Model):
    topic_id = models.IntegerField()
    poll_option_id = models.IntegerField()
    vote_user_id = models.IntegerField()
    vote_user_ip = models.CharField(max_length=120)
    class Meta:
        db_table = u'phpbb_poll_votes'

class PhpbbPosts(models.Model):
    post_id = models.IntegerField(primary_key=True)
    topic_id = models.IntegerField()
    forum_id = models.IntegerField()
    poster_id = models.IntegerField()
    icon_id = models.IntegerField()
    poster_ip = models.CharField(max_length=120)
    post_time = models.IntegerField()
    post_approved = models.IntegerField()
    post_reported = models.IntegerField()
    enable_bbcode = models.IntegerField()
    enable_smilies = models.IntegerField()
    enable_magic_url = models.IntegerField()
    enable_sig = models.IntegerField()
    post_username = models.CharField(max_length=765)
    post_subject = models.CharField(max_length=765)
    post_text = models.TextField()
    post_checksum = models.CharField(max_length=96)
    post_attachment = models.IntegerField()
    bbcode_bitfield = models.CharField(max_length=765)
    bbcode_uid = models.CharField(max_length=24)
    post_postcount = models.IntegerField()
    post_edit_time = models.IntegerField()
    post_edit_reason = models.CharField(max_length=765)
    post_edit_user = models.IntegerField()
    post_edit_count = models.IntegerField()
    post_edit_locked = models.IntegerField()
    class Meta:
        db_table = u'phpbb_posts'

class PhpbbPrivmsgs(models.Model):
    msg_id = models.IntegerField(primary_key=True)
    root_level = models.IntegerField()
    author_id = models.IntegerField()
    icon_id = models.IntegerField()
    author_ip = models.CharField(max_length=120)
    message_time = models.IntegerField()
    enable_bbcode = models.IntegerField()
    enable_smilies = models.IntegerField()
    enable_magic_url = models.IntegerField()
    enable_sig = models.IntegerField()
    message_subject = models.CharField(max_length=765)
    message_text = models.TextField()
    message_edit_reason = models.CharField(max_length=765)
    message_edit_user = models.IntegerField()
    message_attachment = models.IntegerField()
    bbcode_bitfield = models.CharField(max_length=765)
    bbcode_uid = models.CharField(max_length=24)
    message_edit_time = models.IntegerField()
    message_edit_count = models.IntegerField()
    to_address = models.TextField()
    bcc_address = models.TextField()
    message_reported = models.IntegerField()
    class Meta:
        db_table = u'phpbb_privmsgs'

class PhpbbPrivmsgsFolder(models.Model):
    folder_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    folder_name = models.CharField(max_length=765)
    pm_count = models.IntegerField()
    class Meta:
        db_table = u'phpbb_privmsgs_folder'

class PhpbbPrivmsgsRules(models.Model):
    rule_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    rule_check = models.IntegerField()
    rule_connection = models.IntegerField()
    rule_string = models.CharField(max_length=765)
    rule_user_id = models.IntegerField()
    rule_group_id = models.IntegerField()
    rule_action = models.IntegerField()
    rule_folder_id = models.IntegerField()
    class Meta:
        db_table = u'phpbb_privmsgs_rules'

class PhpbbPrivmsgsTo(models.Model):
    msg_id = models.IntegerField()
    user_id = models.IntegerField()
    author_id = models.IntegerField()
    pm_deleted = models.IntegerField()
    pm_new = models.IntegerField()
    pm_unread = models.IntegerField()
    pm_replied = models.IntegerField()
    pm_marked = models.IntegerField()
    pm_forwarded = models.IntegerField()
    folder_id = models.IntegerField()
    class Meta:
        db_table = u'phpbb_privmsgs_to'

class PhpbbProfileFields(models.Model):
    field_id = models.IntegerField(primary_key=True)
    field_name = models.CharField(max_length=765)
    field_type = models.IntegerField()
    field_ident = models.CharField(max_length=60)
    field_length = models.CharField(max_length=60)
    field_minlen = models.CharField(max_length=765)
    field_maxlen = models.CharField(max_length=765)
    field_novalue = models.CharField(max_length=765)
    field_default_value = models.CharField(max_length=765)
    field_validation = models.CharField(max_length=60)
    field_required = models.IntegerField()
    field_show_on_reg = models.IntegerField()
    field_show_profile = models.IntegerField()
    field_hide = models.IntegerField()
    field_no_view = models.IntegerField()
    field_active = models.IntegerField()
    field_order = models.IntegerField()
    field_show_on_vt = models.IntegerField()
    class Meta:
        db_table = u'phpbb_profile_fields'

class PhpbbProfileFieldsData(models.Model):
    user_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'phpbb_profile_fields_data'

class PhpbbProfileFieldsLang(models.Model):
    field_id = models.IntegerField(primary_key=True)
    lang_id = models.IntegerField(primary_key=True)
    option_id = models.IntegerField(primary_key=True)
    field_type = models.IntegerField()
    lang_value = models.CharField(max_length=765)
    class Meta:
        db_table = u'phpbb_profile_fields_lang'

class PhpbbProfileLang(models.Model):
    field_id = models.IntegerField(primary_key=True)
    lang_id = models.IntegerField(primary_key=True)
    lang_name = models.CharField(max_length=765)
    lang_explain = models.TextField()
    lang_default_value = models.CharField(max_length=765)
    class Meta:
        db_table = u'phpbb_profile_lang'

class PhpbbQaConfirm(models.Model):
    session_id = models.CharField(max_length=96)
    confirm_id = models.CharField(max_length=96)
    lang_iso = models.CharField(max_length=90)
    question_id = models.IntegerField()
    attempts = models.IntegerField()
    confirm_type = models.IntegerField()
    class Meta:
        db_table = u'phpbb_qa_confirm'

class PhpbbRanks(models.Model):
    rank_id = models.IntegerField(primary_key=True)
    rank_title = models.CharField(max_length=765)
    rank_min = models.IntegerField()
    rank_special = models.IntegerField()
    rank_image = models.CharField(max_length=765)
    class Meta:
        db_table = u'phpbb_ranks'

class PhpbbReports(models.Model):
    report_id = models.IntegerField(primary_key=True)
    reason_id = models.IntegerField()
    post_id = models.IntegerField()
    user_id = models.IntegerField()
    user_notify = models.IntegerField()
    report_closed = models.IntegerField()
    report_time = models.IntegerField()
    report_text = models.TextField()
    pm_id = models.IntegerField()
    class Meta:
        db_table = u'phpbb_reports'

class PhpbbReportsReasons(models.Model):
    reason_id = models.IntegerField(primary_key=True)
    reason_title = models.CharField(max_length=765)
    reason_description = models.TextField()
    reason_order = models.IntegerField()
    class Meta:
        db_table = u'phpbb_reports_reasons'

class PhpbbReputation(models.Model):
    reputation_id = models.IntegerField(primary_key=True)
    post_id = models.IntegerField()
    user_id = models.IntegerField()
    poster_id = models.IntegerField()
    poster_ip = models.CharField(max_length=120)
    reputation_time = models.IntegerField()
    comment_text = models.TextField()
    change_rep = models.IntegerField()
    class Meta:
        db_table = u'phpbb_reputation'

class PhpbbSearchResults(models.Model):
    search_key = models.CharField(max_length=96, primary_key=True)
    search_time = models.IntegerField()
    search_keywords = models.TextField()
    search_authors = models.TextField()
    class Meta:
        db_table = u'phpbb_search_results'

class PhpbbSearchWordlist(models.Model):
    word_id = models.IntegerField(primary_key=True)
    word_text = models.CharField(unique=True, max_length=765)
    word_common = models.IntegerField()
    word_count = models.IntegerField()
    class Meta:
        db_table = u'phpbb_search_wordlist'

class PhpbbSearchWordmatch(models.Model):
    post_id = models.IntegerField()
    word_id = models.IntegerField()
    title_match = models.IntegerField(unique=True)
    class Meta:
        db_table = u'phpbb_search_wordmatch'

class PhpbbSessions(models.Model):
    session_id = models.CharField(max_length=96, primary_key=True)
    session_user_id = models.IntegerField()
    session_forum_id = models.IntegerField()
    session_last_visit = models.IntegerField()
    session_start = models.IntegerField()
    session_time = models.IntegerField()
    session_ip = models.CharField(max_length=120)
    session_browser = models.CharField(max_length=450)
    session_forwarded_for = models.CharField(max_length=765)
    session_page = models.CharField(max_length=765)
    session_viewonline = models.IntegerField()
    session_autologin = models.IntegerField()
    session_admin = models.IntegerField()
    class Meta:
        db_table = u'phpbb_sessions'

class PhpbbSessionsKeys(models.Model):
    key_id = models.CharField(max_length=96, primary_key=True)
    user_id = models.IntegerField(primary_key=True)
    last_ip = models.CharField(max_length=120)
    last_login = models.IntegerField()
    class Meta:
        db_table = u'phpbb_sessions_keys'

class PhpbbSitelist(models.Model):
    site_id = models.IntegerField(primary_key=True)
    site_ip = models.CharField(max_length=120)
    site_hostname = models.CharField(max_length=765)
    ip_exclude = models.IntegerField()
    class Meta:
        db_table = u'phpbb_sitelist'

class PhpbbSmilies(models.Model):
    smiley_id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=150)
    emotion = models.CharField(max_length=150)
    smiley_url = models.CharField(max_length=150)
    smiley_width = models.IntegerField()
    smiley_height = models.IntegerField()
    smiley_order = models.IntegerField()
    display_on_posting = models.IntegerField()
    class Meta:
        db_table = u'phpbb_smilies'

class PhpbbStyles(models.Model):
    style_id = models.IntegerField(primary_key=True)
    style_name = models.CharField(unique=True, max_length=765)
    style_copyright = models.CharField(max_length=765)
    style_active = models.IntegerField()
    template_id = models.IntegerField()
    theme_id = models.IntegerField()
    imageset_id = models.IntegerField()
    class Meta:
        db_table = u'phpbb_styles'

class PhpbbStylesImageset(models.Model):
    imageset_id = models.IntegerField(primary_key=True)
    imageset_name = models.CharField(unique=True, max_length=765)
    imageset_copyright = models.CharField(max_length=765)
    imageset_path = models.CharField(max_length=300)
    class Meta:
        db_table = u'phpbb_styles_imageset'

class PhpbbStylesImagesetData(models.Model):
    image_id = models.IntegerField(primary_key=True)
    image_name = models.CharField(max_length=600)
    image_filename = models.CharField(max_length=600)
    image_lang = models.CharField(max_length=90)
    image_height = models.IntegerField()
    image_width = models.IntegerField()
    imageset_id = models.IntegerField()
    class Meta:
        db_table = u'phpbb_styles_imageset_data'

class PhpbbStylesTemplate(models.Model):
    template_id = models.IntegerField(primary_key=True)
    template_name = models.CharField(unique=True, max_length=765)
    template_copyright = models.CharField(max_length=765)
    template_path = models.CharField(max_length=300)
    bbcode_bitfield = models.CharField(max_length=765)
    template_storedb = models.IntegerField()
    template_inherits_id = models.IntegerField()
    template_inherit_path = models.CharField(max_length=765)
    class Meta:
        db_table = u'phpbb_styles_template'

class PhpbbStylesTemplateData(models.Model):
    template_id = models.IntegerField()
    template_filename = models.CharField(max_length=300)
    template_included = models.TextField()
    template_mtime = models.IntegerField()
    template_data = models.TextField()
    class Meta:
        db_table = u'phpbb_styles_template_data'

class PhpbbStylesTheme(models.Model):
    theme_id = models.IntegerField(primary_key=True)
    theme_name = models.CharField(unique=True, max_length=765)
    theme_copyright = models.CharField(max_length=765)
    theme_path = models.CharField(max_length=300)
    theme_storedb = models.IntegerField()
    theme_mtime = models.IntegerField()
    theme_data = models.TextField()
    class Meta:
        db_table = u'phpbb_styles_theme'

class PhpbbTagcategories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=300)
    class Meta:
        db_table = u'phpbb_tagcategories'

class PhpbbTopics(models.Model):
    topic_id = models.IntegerField(primary_key=True)
    forum_id = models.IntegerField()
    icon_id = models.IntegerField()
    topic_attachment = models.IntegerField()
    topic_approved = models.IntegerField()
    topic_reported = models.IntegerField()
    topic_title = models.CharField(max_length=765)
    topic_poster = models.IntegerField()
    topic_time = models.IntegerField()
    topic_time_limit = models.IntegerField()
    topic_views = models.IntegerField()
    topic_replies = models.IntegerField()
    topic_replies_real = models.IntegerField()
    topic_status = models.IntegerField()
    topic_type = models.IntegerField()
    topic_first_post_id = models.IntegerField()
    topic_first_poster_name = models.CharField(max_length=765)
    topic_first_poster_colour = models.CharField(max_length=18)
    topic_last_post_id = models.IntegerField()
    topic_last_poster_id = models.IntegerField()
    topic_last_poster_name = models.CharField(max_length=765)
    topic_last_poster_colour = models.CharField(max_length=18)
    topic_last_post_subject = models.CharField(max_length=765)
    topic_last_post_time = models.IntegerField()
    topic_last_view_time = models.IntegerField()
    topic_moved_id = models.IntegerField()
    topic_bumped = models.IntegerField()
    topic_bumper = models.IntegerField()
    poll_title = models.CharField(max_length=765)
    poll_start = models.IntegerField()
    poll_length = models.IntegerField()
    poll_max_options = models.IntegerField()
    poll_last_vote = models.IntegerField()
    poll_vote_change = models.IntegerField()
    class Meta:
        db_table = u'phpbb_topics'

class PhpbbTopicsPosted(models.Model):
    user_id = models.IntegerField(primary_key=True)
    topic_id = models.IntegerField(primary_key=True)
    topic_posted = models.IntegerField()
    class Meta:
        db_table = u'phpbb_topics_posted'

class PhpbbTopicsTopictags(models.Model):
    topic_id = models.IntegerField()
    tag_id = models.IntegerField()
    class Meta:
        db_table = u'phpbb_topics_topictags'

class PhpbbTopicsTrack(models.Model):
    user_id = models.IntegerField(primary_key=True)
    topic_id = models.IntegerField()
    forum_id = models.IntegerField()
    mark_time = models.IntegerField()
    class Meta:
        db_table = u'phpbb_topics_track'

class PhpbbTopicsWatch(models.Model):
    topic_id = models.IntegerField()
    user_id = models.IntegerField()
    notify_status = models.IntegerField()
    class Meta:
        db_table = u'phpbb_topics_watch'

class PhpbbTopictags(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    tag_category = models.IntegerField()
    tag_name = models.CharField(max_length=300)
    class Meta:
        db_table = u'phpbb_topictags'

class PhpbbUserGroup(models.Model):
    group_id = models.IntegerField()
    user_id = models.IntegerField()
    group_leader = models.IntegerField()
    user_pending = models.IntegerField()
    class Meta:
        db_table = u'phpbb_user_group'

class PhpbbUsers(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_type = models.IntegerField()
    group_id = models.IntegerField()
    user_permissions = models.TextField()
    user_perm_from = models.IntegerField()
    user_ip = models.CharField(max_length=120)
    user_regdate = models.IntegerField()
    username = models.CharField(max_length=765)
    username_clean = models.CharField(unique=True, max_length=765)
    user_password = models.CharField(max_length=120)
    user_passchg = models.IntegerField()
    user_pass_convert = models.IntegerField()
    user_email = models.CharField(max_length=300)
    user_email_hash = models.BigIntegerField()
    user_birthday = models.CharField(max_length=30)
    user_lastvisit = models.IntegerField()
    user_lastmark = models.IntegerField()
    user_lastpost_time = models.IntegerField()
    user_lastpage = models.CharField(max_length=600)
    user_last_confirm_key = models.CharField(max_length=30)
    user_last_search = models.IntegerField()
    user_warnings = models.IntegerField()
    user_last_warning = models.IntegerField()
    user_login_attempts = models.IntegerField()
    user_inactive_reason = models.IntegerField()
    user_inactive_time = models.IntegerField()
    user_posts = models.IntegerField()
    user_lang = models.CharField(max_length=90)
    user_timezone = models.DecimalField(max_digits=7, decimal_places=2)
    user_dst = models.IntegerField()
    user_dateformat = models.CharField(max_length=90)
    user_style = models.IntegerField()
    user_rank = models.IntegerField()
    user_colour = models.CharField(max_length=18)
    user_new_privmsg = models.IntegerField()
    user_unread_privmsg = models.IntegerField()
    user_last_privmsg = models.IntegerField()
    user_message_rules = models.IntegerField()
    user_full_folder = models.IntegerField()
    user_emailtime = models.IntegerField()
    user_topic_show_days = models.IntegerField()
    user_topic_sortby_type = models.CharField(max_length=3)
    user_topic_sortby_dir = models.CharField(max_length=3)
    user_post_show_days = models.IntegerField()
    user_post_sortby_type = models.CharField(max_length=3)
    user_post_sortby_dir = models.CharField(max_length=3)
    user_notify = models.IntegerField()
    user_notify_pm = models.IntegerField()
    user_notify_type = models.IntegerField()
    user_allow_pm = models.IntegerField()
    user_allow_viewonline = models.IntegerField()
    user_allow_viewemail = models.IntegerField()
    user_allow_massemail = models.IntegerField()
    user_options = models.IntegerField()
    user_avatar = models.CharField(max_length=765)
    user_avatar_type = models.IntegerField()
    user_avatar_width = models.IntegerField()
    user_avatar_height = models.IntegerField()
    user_sig = models.TextField()
    user_sig_bbcode_uid = models.CharField(max_length=24)
    user_sig_bbcode_bitfield = models.CharField(max_length=765)
    user_from = models.CharField(max_length=300)
    user_icq = models.CharField(max_length=45)
    user_aim = models.CharField(max_length=765)
    user_yim = models.CharField(max_length=765)
    user_msnm = models.CharField(max_length=765)
    user_jabber = models.CharField(max_length=765)
    user_website = models.CharField(max_length=600)
    user_occ = models.TextField()
    user_interests = models.TextField()
    user_actkey = models.CharField(max_length=96)
    user_newpasswd = models.CharField(max_length=120)
    user_form_salt = models.CharField(max_length=96)
    user_new = models.IntegerField()
    user_reminded = models.IntegerField()
    user_reminded_time = models.IntegerField()
    user_index = models.TextField()
    user_gender = models.IntegerField()
    user_reputation = models.IntegerField()
    class Meta:
        db_table = u'phpbb_users'

class PhpbbWarnings(models.Model):
    warning_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    post_id = models.IntegerField()
    log_id = models.IntegerField()
    warning_time = models.IntegerField()
    class Meta:
        db_table = u'phpbb_warnings'

class PhpbbWords(models.Model):
    word_id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=765)
    replacement = models.CharField(max_length=765)
    class Meta:
        db_table = u'phpbb_words'

class PhpbbZebra(models.Model):
    user_id = models.IntegerField(primary_key=True)
    zebra_id = models.IntegerField(primary_key=True)
    friend = models.IntegerField()
    foe = models.IntegerField()
    class Meta:
        db_table = u'phpbb_zebra'

class WeatherGismeteodata(models.Model):
    id = models.CharField(max_length=60, primary_key=True)
    data = models.TextField()
    class Meta:
        db_table = u'weather_gismeteodata'

