--
-- PostgreSQL database dump
--

\restrict boDfvfP6OeEitN1JEeoRH9X4VwTI0OovdWEq3Hcp3JLISFXZg1gLpmKdgEuTeOR

-- Dumped from database version 15.14 (Homebrew)
-- Dumped by pg_dump version 15.14 (Homebrew)

-- Started on 2025-09-12 10:21:55 CEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE IF EXISTS ONLY public.wagtailusers_userprofile DROP CONSTRAINT IF EXISTS wagtailusers_userprofile_user_id_59c92331_fk_auth_user_id;
ALTER TABLE IF EXISTS ONLY public.wagtailsearchpromotions_searchpromotion DROP CONSTRAINT IF EXISTS wagtailsearchpromoti_query_id_fbce4eaa_fk_wagtailse;
ALTER TABLE IF EXISTS ONLY public.wagtailsearchpromotions_querydailyhits DROP CONSTRAINT IF EXISTS wagtailsearchpromoti_query_id_3a591f4d_fk_wagtailse;
ALTER TABLE IF EXISTS ONLY public.wagtailsearchpromotions_searchpromotion DROP CONSTRAINT IF EXISTS wagtailsearchpromoti_page_id_71920f17_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailsearch_indexentry DROP CONSTRAINT IF EXISTS wagtailsearch_indexe_content_type_id_62ed694f_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailredirects_redirect DROP CONSTRAINT IF EXISTS wagtailredirects_red_site_id_780a0e1e_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailredirects_redirect DROP CONSTRAINT IF EXISTS wagtailredirects_red_redirect_page_id_b5728a8f_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailimages_rendition DROP CONSTRAINT IF EXISTS wagtailimages_rendit_image_id_3e1fd774_fk_wagtailim;
ALTER TABLE IF EXISTS ONLY public.wagtailimages_image DROP CONSTRAINT IF EXISTS wagtailimages_image_uploaded_by_user_id_5d73dc75_fk_auth_user;
ALTER TABLE IF EXISTS ONLY public.wagtailimages_image DROP CONSTRAINT IF EXISTS wagtailimages_image_collection_id_c2f8af7e_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailforms_formsubmission DROP CONSTRAINT IF EXISTS wagtailforms_formsub_page_id_e48e93e7_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtaildocs_document DROP CONSTRAINT IF EXISTS wagtaildocs_document_uploaded_by_user_id_17258b41_fk_auth_user;
ALTER TABLE IF EXISTS ONLY public.wagtaildocs_document DROP CONSTRAINT IF EXISTS wagtaildocs_document_collection_id_23881625_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowtask DROP CONSTRAINT IF EXISTS wagtailcore_workflow_workflow_id_b9717175_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowcontenttype DROP CONSTRAINT IF EXISTS wagtailcore_workflow_workflow_id_9aad7cd2_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowpage DROP CONSTRAINT IF EXISTS wagtailcore_workflow_workflow_id_56f56ff6_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowstate DROP CONSTRAINT IF EXISTS wagtailcore_workflow_workflow_id_1f18378f_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowtask DROP CONSTRAINT IF EXISTS wagtailcore_workflow_task_id_ce7716fe_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowstate DROP CONSTRAINT IF EXISTS wagtailcore_workflow_requested_by_id_4090bca3_fk_auth_user;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowpage DROP CONSTRAINT IF EXISTS wagtailcore_workflow_page_id_81e7bab6_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowstate DROP CONSTRAINT IF EXISTS wagtailcore_workflow_current_task_state_i_3a1a0632_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowcontenttype DROP CONSTRAINT IF EXISTS wagtailcore_workflow_content_type_id_b261bb37_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowstate DROP CONSTRAINT IF EXISTS wagtailcore_workflow_content_type_id_2bb78ce1_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowstate DROP CONSTRAINT IF EXISTS wagtailcore_workflow_base_content_type_id_a30dc576_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_uploadedfile DROP CONSTRAINT IF EXISTS wagtailcore_uploaded_uploaded_by_user_id_c7580fe8_fk_auth_user;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_uploadedfile DROP CONSTRAINT IF EXISTS wagtailcore_uploaded_for_content_type_id_b0fc87b2_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_taskstate DROP CONSTRAINT IF EXISTS wagtailcore_taskstate_task_id_c3677c34_fk_wagtailcore_task_id;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_taskstate DROP CONSTRAINT IF EXISTS wagtailcore_taskstate_finished_by_id_13f98229_fk_auth_user_id;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_taskstate DROP CONSTRAINT IF EXISTS wagtailcore_taskstat_workflow_state_id_9239a775_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_taskstate DROP CONSTRAINT IF EXISTS wagtailcore_taskstat_revision_id_df25a499_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_taskstate DROP CONSTRAINT IF EXISTS wagtailcore_taskstat_content_type_id_0a758fdc_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_task DROP CONSTRAINT IF EXISTS wagtailcore_task_content_type_id_249ab8ba_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_site DROP CONSTRAINT IF EXISTS wagtailcore_site_root_page_id_e02fb95c_fk_wagtailcore_page_id;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_revision DROP CONSTRAINT IF EXISTS wagtailcore_revision_content_type_id_c8cb69c0_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_revision DROP CONSTRAINT IF EXISTS wagtailcore_revision_base_content_type_id_5b4ef7bd_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_referenceindex DROP CONSTRAINT IF EXISTS wagtailcore_referenc_to_content_type_id_93690bbd_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_referenceindex DROP CONSTRAINT IF EXISTS wagtailcore_referenc_content_type_id_766e0336_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_referenceindex DROP CONSTRAINT IF EXISTS wagtailcore_referenc_base_content_type_id_313cf40f_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_pageviewrestriction_groups DROP CONSTRAINT IF EXISTS wagtailcore_pageview_pageviewrestriction__f147a99a_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_pageviewrestriction DROP CONSTRAINT IF EXISTS wagtailcore_pageview_page_id_15a8bea6_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_pageviewrestriction_groups DROP CONSTRAINT IF EXISTS wagtailcore_pageview_group_id_6460f223_fk_auth_grou;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_pagesubscription DROP CONSTRAINT IF EXISTS wagtailcore_pagesubscription_user_id_89d7def9_fk_auth_user_id;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_pagesubscription DROP CONSTRAINT IF EXISTS wagtailcore_pagesubs_page_id_a085e7a6_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_revision DROP CONSTRAINT IF EXISTS wagtailcore_pagerevision_user_id_2409d2f4_fk_auth_user_id;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_pagelogentry DROP CONSTRAINT IF EXISTS wagtailcore_pageloge_content_type_id_74e7708a_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_page DROP CONSTRAINT IF EXISTS wagtailcore_page_owner_id_fbf7c332_fk_auth_user_id;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_page DROP CONSTRAINT IF EXISTS wagtailcore_page_locked_by_id_bcb86245_fk_auth_user_id;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_page DROP CONSTRAINT IF EXISTS wagtailcore_page_locale_id_3c7e30a6_fk_wagtailcore_locale_id;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_page DROP CONSTRAINT IF EXISTS wagtailcore_page_live_revision_id_930bd822_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_page DROP CONSTRAINT IF EXISTS wagtailcore_page_latest_revision_id_e60fef51_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_page DROP CONSTRAINT IF EXISTS wagtailcore_page_content_type_id_c28424df_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_page DROP CONSTRAINT IF EXISTS wagtailcore_page_alias_of_id_12945502_fk_wagtailcore_page_id;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_modellogentry DROP CONSTRAINT IF EXISTS wagtailcore_modellog_content_type_id_68849e77_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupsitepermission DROP CONSTRAINT IF EXISTS wagtailcore_groupsit_site_id_245de488_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupsitepermission DROP CONSTRAINT IF EXISTS wagtailcore_groupsit_permission_id_459b1f38_fk_auth_perm;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupsitepermission DROP CONSTRAINT IF EXISTS wagtailcore_groupsit_group_id_e5cdbee4_fk_auth_grou;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_grouppagepermission DROP CONSTRAINT IF EXISTS wagtailcore_grouppag_permission_id_05acb22e_fk_auth_perm;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_grouppagepermission DROP CONSTRAINT IF EXISTS wagtailcore_grouppag_page_id_710b114a_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_grouppagepermission DROP CONSTRAINT IF EXISTS wagtailcore_grouppag_group_id_fc07e671_fk_auth_grou;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupcollectionpermission DROP CONSTRAINT IF EXISTS wagtailcore_groupcol_permission_id_1b626275_fk_auth_perm;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupcollectionpermission DROP CONSTRAINT IF EXISTS wagtailcore_groupcol_group_id_05d61460_fk_auth_grou;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupcollectionpermission DROP CONSTRAINT IF EXISTS wagtailcore_groupcol_collection_id_5423575a_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupapprovaltask DROP CONSTRAINT IF EXISTS wagtailcore_groupapp_task_ptr_id_cfe58781_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupapprovaltask_groups DROP CONSTRAINT IF EXISTS wagtailcore_groupapp_groupapprovaltask_id_9a9255ea_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupapprovaltask_groups DROP CONSTRAINT IF EXISTS wagtailcore_groupapp_group_id_2e64b61f_fk_auth_grou;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_commentreply DROP CONSTRAINT IF EXISTS wagtailcore_commentreply_user_id_d0b3b9c3_fk_auth_user_id;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_commentreply DROP CONSTRAINT IF EXISTS wagtailcore_commentr_comment_id_afc7e027_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_comment DROP CONSTRAINT IF EXISTS wagtailcore_comment_user_id_0c577ca6_fk_auth_user_id;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_comment DROP CONSTRAINT IF EXISTS wagtailcore_comment_revision_created_id_1d058279_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_comment DROP CONSTRAINT IF EXISTS wagtailcore_comment_resolved_by_id_a282aa0e_fk_auth_user_id;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_comment DROP CONSTRAINT IF EXISTS wagtailcore_comment_page_id_108444b5_fk_wagtailcore_page_id;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_collectionviewrestriction_groups DROP CONSTRAINT IF EXISTS wagtailcore_collecti_group_id_1823f2a3_fk_auth_grou;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_collectionviewrestriction_groups DROP CONSTRAINT IF EXISTS wagtailcore_collecti_collectionviewrestri_47320efd_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_collectionviewrestriction DROP CONSTRAINT IF EXISTS wagtailcore_collecti_collection_id_761908ec_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.wagtailadmin_editingsession DROP CONSTRAINT IF EXISTS wagtailadmin_editingsession_user_id_6e1a9b70_fk_auth_user_id;
ALTER TABLE IF EXISTS ONLY public.wagtailadmin_editingsession DROP CONSTRAINT IF EXISTS wagtailadmin_editing_content_type_id_4df7730e_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.taggit_taggeditem DROP CONSTRAINT IF EXISTS taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id;
ALTER TABLE IF EXISTS ONLY public.taggit_taggeditem DROP CONSTRAINT IF EXISTS taggit_taggeditem_content_type_id_9957a03c_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.projects_projecttag DROP CONSTRAINT IF EXISTS projects_projecttag_tag_id_d49ab282_fk_taggit_tag_id;
ALTER TABLE IF EXISTS ONLY public.projects_projecttag DROP CONSTRAINT IF EXISTS projects_projecttag_content_object_id_ac067992_fk_projects_;
ALTER TABLE IF EXISTS ONLY public.projects_projectpagetag DROP CONSTRAINT IF EXISTS projects_projectpagetag_tag_id_d11386be_fk_taggit_tag_id;
ALTER TABLE IF EXISTS ONLY public.projects_projectpageimage DROP CONSTRAINT IF EXISTS projects_projectpage_project_page_id_1f3f194b_fk_projects_;
ALTER TABLE IF EXISTS ONLY public.projects_projectpage DROP CONSTRAINT IF EXISTS projects_projectpage_page_ptr_id_2eccd927_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.projects_projectpageimage DROP CONSTRAINT IF EXISTS projects_projectpage_image_id_1e7b6756_fk_wagtailim;
ALTER TABLE IF EXISTS ONLY public.projects_projectpagetag DROP CONSTRAINT IF EXISTS projects_projectpage_content_object_id_b258f16e_fk_projects_;
ALTER TABLE IF EXISTS ONLY public.projects_projectimage DROP CONSTRAINT IF EXISTS projects_projectimag_project_id_618ded0e_fk_projects_;
ALTER TABLE IF EXISTS ONLY public.projects_projectimage DROP CONSTRAINT IF EXISTS projects_projectimag_image_id_f5a991e8_fk_wagtailim;
ALTER TABLE IF EXISTS ONLY public.pages_sitesettings DROP CONSTRAINT IF EXISTS pages_sitesettings_site_id_cbd7f7da_fk_wagtailcore_site_id;
ALTER TABLE IF EXISTS ONLY public.pages_sitesettings DROP CONSTRAINT IF EXISTS pages_sitesettings_navigation_cta_page__99fb3790_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.pages_sitesettings DROP CONSTRAINT IF EXISTS pages_sitesettings_logo_id_ef4fb98b_fk_wagtailimages_image_id;
ALTER TABLE IF EXISTS ONLY public.pages_modularpage DROP CONSTRAINT IF EXISTS pages_modularpage_page_ptr_id_802d7c31_fk_wagtailcore_page_id;
ALTER TABLE IF EXISTS ONLY public.pages_logo DROP CONSTRAINT IF EXISTS pages_logo_image_id_375482c6_fk_wagtailimages_image_id;
ALTER TABLE IF EXISTS ONLY public.pages_homepage DROP CONSTRAINT IF EXISTS pages_homepage_page_ptr_id_5b805d74_fk_wagtailcore_page_id;
ALTER TABLE IF EXISTS ONLY public.pages_gallerypage DROP CONSTRAINT IF EXISTS pages_gallerypage_page_ptr_id_c6ee2214_fk_wagtailcore_page_id;
ALTER TABLE IF EXISTS ONLY public.pages_contactpage DROP CONSTRAINT IF EXISTS pages_contactpage_page_ptr_id_604d75e6_fk_wagtailcore_page_id;
ALTER TABLE IF EXISTS ONLY public.django_admin_log DROP CONSTRAINT IF EXISTS django_admin_log_user_id_c564eba6_fk_auth_user_id;
ALTER TABLE IF EXISTS ONLY public.django_admin_log DROP CONSTRAINT IF EXISTS django_admin_log_content_type_id_c4bce8eb_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.contacts_contactsubmission DROP CONSTRAINT IF EXISTS contacts_contactsubm_site_id_66673466_fk_wagtailco;
ALTER TABLE IF EXISTS ONLY public.auth_user_user_permissions DROP CONSTRAINT IF EXISTS auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
ALTER TABLE IF EXISTS ONLY public.auth_user_user_permissions DROP CONSTRAINT IF EXISTS auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
ALTER TABLE IF EXISTS ONLY public.auth_user_groups DROP CONSTRAINT IF EXISTS auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
ALTER TABLE IF EXISTS ONLY public.auth_user_groups DROP CONSTRAINT IF EXISTS auth_user_groups_group_id_97559544_fk_auth_group_id;
ALTER TABLE IF EXISTS ONLY public.auth_permission DROP CONSTRAINT IF EXISTS auth_permission_content_type_id_2f476e4b_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.auth_group_permissions DROP CONSTRAINT IF EXISTS auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
ALTER TABLE IF EXISTS ONLY public.auth_group_permissions DROP CONSTRAINT IF EXISTS auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
DROP INDEX IF EXISTS public.workflowstate_ct_id_idx;
DROP INDEX IF EXISTS public.workflowstate_base_ct_id_idx;
DROP INDEX IF EXISTS public.wagtailsearchpromotions_searchpromotion_query_id_fbce4eaa;
DROP INDEX IF EXISTS public.wagtailsearchpromotions_searchpromotion_page_id_71920f17;
DROP INDEX IF EXISTS public.wagtailsearchpromotions_querydailyhits_query_id_3a591f4d;
DROP INDEX IF EXISTS public.wagtailsearchpromotions_query_query_string_0e19aecc_like;
DROP INDEX IF EXISTS public.wagtailsearch_indexentry_content_type_id_62ed694f;
DROP INDEX IF EXISTS public.wagtailsear_title_9caae0_gin;
DROP INDEX IF EXISTS public.wagtailsear_body_90c85d_gin;
DROP INDEX IF EXISTS public.wagtailsear_autocom_476c89_gin;
DROP INDEX IF EXISTS public.wagtailredirects_redirect_site_id_780a0e1e;
DROP INDEX IF EXISTS public.wagtailredirects_redirect_redirect_page_id_b5728a8f;
DROP INDEX IF EXISTS public.wagtailredirects_redirect_old_path_bb35247b_like;
DROP INDEX IF EXISTS public.wagtailredirects_redirect_old_path_bb35247b;
DROP INDEX IF EXISTS public.wagtailimages_rendition_image_id_3e1fd774;
DROP INDEX IF EXISTS public.wagtailimages_rendition_filter_spec_1cba3201_like;
DROP INDEX IF EXISTS public.wagtailimages_rendition_filter_spec_1cba3201;
DROP INDEX IF EXISTS public.wagtailimages_image_uploaded_by_user_id_5d73dc75;
DROP INDEX IF EXISTS public.wagtailimages_image_file_hash_fb5bbb23_like;
DROP INDEX IF EXISTS public.wagtailimages_image_file_hash_fb5bbb23;
DROP INDEX IF EXISTS public.wagtailimages_image_created_at_86fa6cd4;
DROP INDEX IF EXISTS public.wagtailimages_image_collection_id_c2f8af7e;
DROP INDEX IF EXISTS public.wagtailforms_formsubmission_page_id_e48e93e7;
DROP INDEX IF EXISTS public.wagtailembeds_embed_hash_c9bd8c9a_like;
DROP INDEX IF EXISTS public.wagtailembeds_embed_cache_until_26c94bb0;
DROP INDEX IF EXISTS public.wagtaildocs_document_uploaded_by_user_id_17258b41;
DROP INDEX IF EXISTS public.wagtaildocs_document_collection_id_23881625;
DROP INDEX IF EXISTS public.wagtailcore_workflowtask_workflow_id_b9717175;
DROP INDEX IF EXISTS public.wagtailcore_workflowtask_task_id_ce7716fe;
DROP INDEX IF EXISTS public.wagtailcore_workflowstate_workflow_id_1f18378f;
DROP INDEX IF EXISTS public.wagtailcore_workflowstate_requested_by_id_4090bca3;
DROP INDEX IF EXISTS public.wagtailcore_workflowstate_content_type_id_2bb78ce1;
DROP INDEX IF EXISTS public.wagtailcore_workflowstate_base_content_type_id_a30dc576;
DROP INDEX IF EXISTS public.wagtailcore_workflowpage_workflow_id_56f56ff6;
DROP INDEX IF EXISTS public.wagtailcore_workflowcontenttype_workflow_id_9aad7cd2;
DROP INDEX IF EXISTS public.wagtailcore_uploadedfile_uploaded_by_user_id_c7580fe8;
DROP INDEX IF EXISTS public.wagtailcore_uploadedfile_for_content_type_id_b0fc87b2;
DROP INDEX IF EXISTS public.wagtailcore_taskstate_workflow_state_id_9239a775;
DROP INDEX IF EXISTS public.wagtailcore_taskstate_task_id_c3677c34;
DROP INDEX IF EXISTS public.wagtailcore_taskstate_page_revision_id_9f52c88e;
DROP INDEX IF EXISTS public.wagtailcore_taskstate_finished_by_id_13f98229;
DROP INDEX IF EXISTS public.wagtailcore_taskstate_content_type_id_0a758fdc;
DROP INDEX IF EXISTS public.wagtailcore_task_content_type_id_249ab8ba;
DROP INDEX IF EXISTS public.wagtailcore_site_root_page_id_e02fb95c;
DROP INDEX IF EXISTS public.wagtailcore_site_hostname_96b20b46_like;
DROP INDEX IF EXISTS public.wagtailcore_site_hostname_96b20b46;
DROP INDEX IF EXISTS public.wagtailcore_revision_content_type_id_c8cb69c0;
DROP INDEX IF EXISTS public.wagtailcore_revision_base_content_type_id_5b4ef7bd;
DROP INDEX IF EXISTS public.wagtailcore_referenceindex_to_content_type_id_93690bbd;
DROP INDEX IF EXISTS public.wagtailcore_referenceindex_content_type_id_766e0336;
DROP INDEX IF EXISTS public.wagtailcore_referenceindex_base_content_type_id_313cf40f;
DROP INDEX IF EXISTS public.wagtailcore_pageviewrestriction_page_id_15a8bea6;
DROP INDEX IF EXISTS public.wagtailcore_pageviewrestriction_groups_group_id_6460f223;
DROP INDEX IF EXISTS public.wagtailcore_pageviewrestri_pageviewrestriction_id_f147a99a;
DROP INDEX IF EXISTS public.wagtailcore_pagesubscription_user_id_89d7def9;
DROP INDEX IF EXISTS public.wagtailcore_pagesubscription_page_id_a085e7a6;
DROP INDEX IF EXISTS public.wagtailcore_pagerevision_user_id_2409d2f4;
DROP INDEX IF EXISTS public.wagtailcore_pagerevision_created_at_66954e3b;
DROP INDEX IF EXISTS public.wagtailcore_pagerevision_approved_go_live_at_e56afc67;
DROP INDEX IF EXISTS public.wagtailcore_pagelogentry_user_id_604ccfd8;
DROP INDEX IF EXISTS public.wagtailcore_pagelogentry_timestamp_deb774c4;
DROP INDEX IF EXISTS public.wagtailcore_pagelogentry_revision_id_8043d103;
DROP INDEX IF EXISTS public.wagtailcore_pagelogentry_page_id_8464e327;
DROP INDEX IF EXISTS public.wagtailcore_pagelogentry_content_type_id_74e7708a;
DROP INDEX IF EXISTS public.wagtailcore_pagelogentry_content_changed_99f27ade;
DROP INDEX IF EXISTS public.wagtailcore_pagelogentry_action_c2408198_like;
DROP INDEX IF EXISTS public.wagtailcore_pagelogentry_action_c2408198;
DROP INDEX IF EXISTS public.wagtailcore_page_slug_e7c11b8f_like;
DROP INDEX IF EXISTS public.wagtailcore_page_slug_e7c11b8f;
DROP INDEX IF EXISTS public.wagtailcore_page_path_98eba2c8_like;
DROP INDEX IF EXISTS public.wagtailcore_page_owner_id_fbf7c332;
DROP INDEX IF EXISTS public.wagtailcore_page_locked_by_id_bcb86245;
DROP INDEX IF EXISTS public.wagtailcore_page_locale_id_3c7e30a6;
DROP INDEX IF EXISTS public.wagtailcore_page_live_revision_id_930bd822;
DROP INDEX IF EXISTS public.wagtailcore_page_latest_revision_id_e60fef51;
DROP INDEX IF EXISTS public.wagtailcore_page_first_published_at_2b5dd637;
DROP INDEX IF EXISTS public.wagtailcore_page_content_type_id_c28424df;
DROP INDEX IF EXISTS public.wagtailcore_page_alias_of_id_12945502;
DROP INDEX IF EXISTS public.wagtailcore_modellogentry_user_id_0278d1bf;
DROP INDEX IF EXISTS public.wagtailcore_modellogentry_timestamp_9694521b;
DROP INDEX IF EXISTS public.wagtailcore_modellogentry_revision_id_df6ca33a;
DROP INDEX IF EXISTS public.wagtailcore_modellogentry_object_id_e0e7d4ef_like;
DROP INDEX IF EXISTS public.wagtailcore_modellogentry_object_id_e0e7d4ef;
DROP INDEX IF EXISTS public.wagtailcore_modellogentry_content_type_id_68849e77;
DROP INDEX IF EXISTS public.wagtailcore_modellogentry_content_changed_8bc39742;
DROP INDEX IF EXISTS public.wagtailcore_modellogentry_action_d2d856ee_like;
DROP INDEX IF EXISTS public.wagtailcore_modellogentry_action_d2d856ee;
DROP INDEX IF EXISTS public.wagtailcore_locale_language_code_03149338_like;
DROP INDEX IF EXISTS public.wagtailcore_groupsitepermission_site_id_245de488;
DROP INDEX IF EXISTS public.wagtailcore_groupsitepermission_permission_id_459b1f38;
DROP INDEX IF EXISTS public.wagtailcore_groupsitepermission_group_id_e5cdbee4;
DROP INDEX IF EXISTS public.wagtailcore_grouppagepermission_permission_id_05acb22e;
DROP INDEX IF EXISTS public.wagtailcore_grouppagepermission_page_id_710b114a;
DROP INDEX IF EXISTS public.wagtailcore_grouppagepermission_group_id_fc07e671;
DROP INDEX IF EXISTS public.wagtailcore_groupcollectionpermission_permission_id_1b626275;
DROP INDEX IF EXISTS public.wagtailcore_groupcollectionpermission_group_id_05d61460;
DROP INDEX IF EXISTS public.wagtailcore_groupcollectionpermission_collection_id_5423575a;
DROP INDEX IF EXISTS public.wagtailcore_groupapprovaltask_groups_group_id_2e64b61f;
DROP INDEX IF EXISTS public.wagtailcore_groupapprovalt_groupapprovaltask_id_9a9255ea;
DROP INDEX IF EXISTS public.wagtailcore_commentreply_user_id_d0b3b9c3;
DROP INDEX IF EXISTS public.wagtailcore_commentreply_comment_id_afc7e027;
DROP INDEX IF EXISTS public.wagtailcore_comment_user_id_0c577ca6;
DROP INDEX IF EXISTS public.wagtailcore_comment_revision_created_id_1d058279;
DROP INDEX IF EXISTS public.wagtailcore_comment_resolved_by_id_a282aa0e;
DROP INDEX IF EXISTS public.wagtailcore_comment_page_id_108444b5;
DROP INDEX IF EXISTS public.wagtailcore_collectionviewrestriction_groups_group_id_1823f2a3;
DROP INDEX IF EXISTS public.wagtailcore_collectionviewrestriction_collection_id_761908ec;
DROP INDEX IF EXISTS public.wagtailcore_collectionview_collectionviewrestriction__47320efd;
DROP INDEX IF EXISTS public.wagtailcore_collection_path_d848dc19_like;
DROP INDEX IF EXISTS public.wagtailadmin_editingsession_user_id_6e1a9b70;
DROP INDEX IF EXISTS public.wagtailadmin_editingsession_content_type_id_4df7730e;
DROP INDEX IF EXISTS public.wagtailadmi_content_717955_idx;
DROP INDEX IF EXISTS public.unique_in_progress_workflow;
DROP INDEX IF EXISTS public.taggit_taggeditem_tag_id_f4f5b767;
DROP INDEX IF EXISTS public.taggit_taggeditem_object_id_e2d7d1df;
DROP INDEX IF EXISTS public.taggit_taggeditem_content_type_id_9957a03c;
DROP INDEX IF EXISTS public.taggit_tagg_content_8fc721_idx;
DROP INDEX IF EXISTS public.taggit_tag_slug_6be58b2c_like;
DROP INDEX IF EXISTS public.taggit_tag_name_58eb2ed9_like;
DROP INDEX IF EXISTS public.projects_projecttag_tag_id_d49ab282;
DROP INDEX IF EXISTS public.projects_projecttag_content_object_id_ac067992;
DROP INDEX IF EXISTS public.projects_projectpagetag_tag_id_d11386be;
DROP INDEX IF EXISTS public.projects_projectpagetag_content_object_id_b258f16e;
DROP INDEX IF EXISTS public.projects_projectpageimage_project_page_id_1f3f194b;
DROP INDEX IF EXISTS public.projects_projectpageimage_image_id_1e7b6756;
DROP INDEX IF EXISTS public.projects_projectimage_project_id_618ded0e;
DROP INDEX IF EXISTS public.projects_projectimage_image_id_f5a991e8;
DROP INDEX IF EXISTS public.projects_project_slug_2d50067a_like;
DROP INDEX IF EXISTS public.pages_sitesettings_navigation_cta_page_id_99fb3790;
DROP INDEX IF EXISTS public.pages_sitesettings_logo_id_ef4fb98b;
DROP INDEX IF EXISTS public.pages_logo_image_id_375482c6;
DROP INDEX IF EXISTS public.django_site_domain_a2e37b91_like;
DROP INDEX IF EXISTS public.django_session_session_key_c0390e0f_like;
DROP INDEX IF EXISTS public.django_session_expire_date_a5c62663;
DROP INDEX IF EXISTS public.django_admin_log_user_id_c564eba6;
DROP INDEX IF EXISTS public.django_admin_log_content_type_id_c4bce8eb;
DROP INDEX IF EXISTS public.content_object_idx;
DROP INDEX IF EXISTS public.contacts_contactsubmission_site_id_66673466;
DROP INDEX IF EXISTS public.base_content_object_idx;
DROP INDEX IF EXISTS public.auth_user_username_6821ab7c_like;
DROP INDEX IF EXISTS public.auth_user_user_permissions_user_id_a95ead1b;
DROP INDEX IF EXISTS public.auth_user_user_permissions_permission_id_1fbb5f2c;
DROP INDEX IF EXISTS public.auth_user_groups_user_id_6a12ed8b;
DROP INDEX IF EXISTS public.auth_user_groups_group_id_97559544;
DROP INDEX IF EXISTS public.auth_permission_content_type_id_2f476e4b;
DROP INDEX IF EXISTS public.auth_group_permissions_permission_id_84c5c92e;
DROP INDEX IF EXISTS public.auth_group_permissions_group_id_b120cbf9;
DROP INDEX IF EXISTS public.auth_group_name_a6ea08ec_like;
ALTER TABLE IF EXISTS ONLY public.wagtailusers_userprofile DROP CONSTRAINT IF EXISTS wagtailusers_userprofile_user_id_key;
ALTER TABLE IF EXISTS ONLY public.wagtailusers_userprofile DROP CONSTRAINT IF EXISTS wagtailusers_userprofile_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailsearchpromotions_searchpromotion DROP CONSTRAINT IF EXISTS wagtailsearchpromotions_searchpromotion_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailsearchpromotions_querydailyhits DROP CONSTRAINT IF EXISTS wagtailsearchpromotions_querydailyhits_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailsearchpromotions_query DROP CONSTRAINT IF EXISTS wagtailsearchpromotions_query_query_string_key;
ALTER TABLE IF EXISTS ONLY public.wagtailsearchpromotions_query DROP CONSTRAINT IF EXISTS wagtailsearchpromotions_query_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailsearchpromotions_querydailyhits DROP CONSTRAINT IF EXISTS wagtailsearchpromotions__query_id_date_b9f15515_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtailsearch_indexentry DROP CONSTRAINT IF EXISTS wagtailsearch_indexentry_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailsearch_indexentry DROP CONSTRAINT IF EXISTS wagtailsearch_indexentry_content_type_id_object_i_bcd7ba73_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtailredirects_redirect DROP CONSTRAINT IF EXISTS wagtailredirects_redirect_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailredirects_redirect DROP CONSTRAINT IF EXISTS wagtailredirects_redirect_old_path_site_id_783622d7_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtailimages_rendition DROP CONSTRAINT IF EXISTS wagtailimages_rendition_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailimages_rendition DROP CONSTRAINT IF EXISTS wagtailimages_rendition_image_id_filter_spec_foc_323c8fe0_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtailimages_image DROP CONSTRAINT IF EXISTS wagtailimages_image_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailforms_formsubmission DROP CONSTRAINT IF EXISTS wagtailforms_formsubmission_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailembeds_embed DROP CONSTRAINT IF EXISTS wagtailembeds_embed_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailembeds_embed DROP CONSTRAINT IF EXISTS wagtailembeds_embed_hash_c9bd8c9a_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtaildocs_document DROP CONSTRAINT IF EXISTS wagtaildocs_document_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowtask DROP CONSTRAINT IF EXISTS wagtailcore_workflowtask_workflow_id_task_id_4ec7a62b_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowtask DROP CONSTRAINT IF EXISTS wagtailcore_workflowtask_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowstate DROP CONSTRAINT IF EXISTS wagtailcore_workflowstate_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowstate DROP CONSTRAINT IF EXISTS wagtailcore_workflowstate_current_task_state_id_key;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowpage DROP CONSTRAINT IF EXISTS wagtailcore_workflowpage_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflowcontenttype DROP CONSTRAINT IF EXISTS wagtailcore_workflowcontenttype_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_workflow DROP CONSTRAINT IF EXISTS wagtailcore_workflow_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_uploadedfile DROP CONSTRAINT IF EXISTS wagtailcore_uploadedfile_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_taskstate DROP CONSTRAINT IF EXISTS wagtailcore_taskstate_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_task DROP CONSTRAINT IF EXISTS wagtailcore_task_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_site DROP CONSTRAINT IF EXISTS wagtailcore_site_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_site DROP CONSTRAINT IF EXISTS wagtailcore_site_hostname_port_2c626d70_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_referenceindex DROP CONSTRAINT IF EXISTS wagtailcore_referenceindex_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_referenceindex DROP CONSTRAINT IF EXISTS wagtailcore_referenceind_base_content_type_id_obj_9e6ccd6a_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_pageviewrestriction DROP CONSTRAINT IF EXISTS wagtailcore_pageviewrestriction_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_pageviewrestriction_groups DROP CONSTRAINT IF EXISTS wagtailcore_pageviewrestriction_groups_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_pageviewrestriction_groups DROP CONSTRAINT IF EXISTS wagtailcore_pageviewrest_pageviewrestriction_id_g_d23f80bb_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_pagesubscription DROP CONSTRAINT IF EXISTS wagtailcore_pagesubscription_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_pagesubscription DROP CONSTRAINT IF EXISTS wagtailcore_pagesubscription_page_id_user_id_0cef73ed_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_revision DROP CONSTRAINT IF EXISTS wagtailcore_pagerevision_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_pagelogentry DROP CONSTRAINT IF EXISTS wagtailcore_pagelogentry_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_page DROP CONSTRAINT IF EXISTS wagtailcore_page_translation_key_locale_id_9b041bad_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_page DROP CONSTRAINT IF EXISTS wagtailcore_page_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_page DROP CONSTRAINT IF EXISTS wagtailcore_page_path_key;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_modellogentry DROP CONSTRAINT IF EXISTS wagtailcore_modellogentry_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_locale DROP CONSTRAINT IF EXISTS wagtailcore_locale_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_locale DROP CONSTRAINT IF EXISTS wagtailcore_locale_language_code_key;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupsitepermission DROP CONSTRAINT IF EXISTS wagtailcore_groupsitepermission_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupsitepermission DROP CONSTRAINT IF EXISTS wagtailcore_groupsiteper_group_id_site_id_permiss_a58ee30d_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_grouppagepermission DROP CONSTRAINT IF EXISTS wagtailcore_grouppagepermission_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupcollectionpermission DROP CONSTRAINT IF EXISTS wagtailcore_groupcollectionpermission_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupcollectionpermission DROP CONSTRAINT IF EXISTS wagtailcore_groupcollect_group_id_collection_id_p_a21cefe9_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupapprovaltask DROP CONSTRAINT IF EXISTS wagtailcore_groupapprovaltask_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupapprovaltask_groups DROP CONSTRAINT IF EXISTS wagtailcore_groupapprovaltask_groups_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_groupapprovaltask_groups DROP CONSTRAINT IF EXISTS wagtailcore_groupapprova_groupapprovaltask_id_gro_bb5ee7eb_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_commentreply DROP CONSTRAINT IF EXISTS wagtailcore_commentreply_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_comment DROP CONSTRAINT IF EXISTS wagtailcore_comment_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_collectionviewrestriction DROP CONSTRAINT IF EXISTS wagtailcore_collectionviewrestriction_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_collectionviewrestriction_groups DROP CONSTRAINT IF EXISTS wagtailcore_collectionviewrestriction_groups_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_collectionviewrestriction_groups DROP CONSTRAINT IF EXISTS wagtailcore_collectionvi_collectionviewrestrictio_988995ae_uniq;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_collection DROP CONSTRAINT IF EXISTS wagtailcore_collection_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_collection DROP CONSTRAINT IF EXISTS wagtailcore_collection_path_key;
ALTER TABLE IF EXISTS ONLY public.wagtailadmin_editingsession DROP CONSTRAINT IF EXISTS wagtailadmin_editingsession_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailadmin_admin DROP CONSTRAINT IF EXISTS wagtailadmin_admin_pkey;
ALTER TABLE IF EXISTS ONLY public.wagtailcore_grouppagepermission DROP CONSTRAINT IF EXISTS unique_permission;
ALTER TABLE IF EXISTS ONLY public.taggit_taggeditem DROP CONSTRAINT IF EXISTS taggit_taggeditem_pkey;
ALTER TABLE IF EXISTS ONLY public.taggit_taggeditem DROP CONSTRAINT IF EXISTS taggit_taggeditem_content_type_id_object_id_tag_id_4bb97a8e_uni;
ALTER TABLE IF EXISTS ONLY public.taggit_tag DROP CONSTRAINT IF EXISTS taggit_tag_slug_key;
ALTER TABLE IF EXISTS ONLY public.taggit_tag DROP CONSTRAINT IF EXISTS taggit_tag_pkey;
ALTER TABLE IF EXISTS ONLY public.taggit_tag DROP CONSTRAINT IF EXISTS taggit_tag_name_key;
ALTER TABLE IF EXISTS ONLY public.projects_projecttag DROP CONSTRAINT IF EXISTS projects_projecttag_pkey;
ALTER TABLE IF EXISTS ONLY public.projects_projectpagetag DROP CONSTRAINT IF EXISTS projects_projectpagetag_pkey;
ALTER TABLE IF EXISTS ONLY public.projects_projectpageimage DROP CONSTRAINT IF EXISTS projects_projectpageimage_pkey;
ALTER TABLE IF EXISTS ONLY public.projects_projectpage DROP CONSTRAINT IF EXISTS projects_projectpage_pkey;
ALTER TABLE IF EXISTS ONLY public.projects_projectimage DROP CONSTRAINT IF EXISTS projects_projectimage_pkey;
ALTER TABLE IF EXISTS ONLY public.projects_project DROP CONSTRAINT IF EXISTS projects_project_slug_key;
ALTER TABLE IF EXISTS ONLY public.projects_project DROP CONSTRAINT IF EXISTS projects_project_pkey;
ALTER TABLE IF EXISTS ONLY public.pages_testimonial DROP CONSTRAINT IF EXISTS pages_testimonial_pkey;
ALTER TABLE IF EXISTS ONLY public.pages_sitesettings DROP CONSTRAINT IF EXISTS pages_sitesettings_site_id_key;
ALTER TABLE IF EXISTS ONLY public.pages_sitesettings DROP CONSTRAINT IF EXISTS pages_sitesettings_pkey;
ALTER TABLE IF EXISTS ONLY public.pages_service DROP CONSTRAINT IF EXISTS pages_service_pkey;
ALTER TABLE IF EXISTS ONLY public.pages_modularpage DROP CONSTRAINT IF EXISTS pages_modularpage_pkey;
ALTER TABLE IF EXISTS ONLY public.pages_logo DROP CONSTRAINT IF EXISTS pages_logo_pkey;
ALTER TABLE IF EXISTS ONLY public.pages_homepage DROP CONSTRAINT IF EXISTS pages_homepage_pkey;
ALTER TABLE IF EXISTS ONLY public.pages_gallerypage DROP CONSTRAINT IF EXISTS pages_gallerypage_pkey;
ALTER TABLE IF EXISTS ONLY public.pages_contactpage DROP CONSTRAINT IF EXISTS pages_contactpage_pkey;
ALTER TABLE IF EXISTS ONLY public.django_site DROP CONSTRAINT IF EXISTS django_site_pkey;
ALTER TABLE IF EXISTS ONLY public.django_site DROP CONSTRAINT IF EXISTS django_site_domain_a2e37b91_uniq;
ALTER TABLE IF EXISTS ONLY public.django_session DROP CONSTRAINT IF EXISTS django_session_pkey;
ALTER TABLE IF EXISTS ONLY public.django_migrations DROP CONSTRAINT IF EXISTS django_migrations_pkey;
ALTER TABLE IF EXISTS ONLY public.django_content_type DROP CONSTRAINT IF EXISTS django_content_type_pkey;
ALTER TABLE IF EXISTS ONLY public.django_content_type DROP CONSTRAINT IF EXISTS django_content_type_app_label_model_76bd3d3b_uniq;
ALTER TABLE IF EXISTS ONLY public.django_admin_log DROP CONSTRAINT IF EXISTS django_admin_log_pkey;
ALTER TABLE IF EXISTS ONLY public.contacts_contactsubmission DROP CONSTRAINT IF EXISTS contacts_contactsubmission_pkey;
ALTER TABLE IF EXISTS ONLY public.auth_user DROP CONSTRAINT IF EXISTS auth_user_username_key;
ALTER TABLE IF EXISTS ONLY public.auth_user_user_permissions DROP CONSTRAINT IF EXISTS auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
ALTER TABLE IF EXISTS ONLY public.auth_user_user_permissions DROP CONSTRAINT IF EXISTS auth_user_user_permissions_pkey;
ALTER TABLE IF EXISTS ONLY public.auth_user DROP CONSTRAINT IF EXISTS auth_user_pkey;
ALTER TABLE IF EXISTS ONLY public.auth_user_groups DROP CONSTRAINT IF EXISTS auth_user_groups_user_id_group_id_94350c0c_uniq;
ALTER TABLE IF EXISTS ONLY public.auth_user_groups DROP CONSTRAINT IF EXISTS auth_user_groups_pkey;
ALTER TABLE IF EXISTS ONLY public.auth_permission DROP CONSTRAINT IF EXISTS auth_permission_pkey;
ALTER TABLE IF EXISTS ONLY public.auth_permission DROP CONSTRAINT IF EXISTS auth_permission_content_type_id_codename_01ab375a_uniq;
ALTER TABLE IF EXISTS ONLY public.auth_group DROP CONSTRAINT IF EXISTS auth_group_pkey;
ALTER TABLE IF EXISTS ONLY public.auth_group_permissions DROP CONSTRAINT IF EXISTS auth_group_permissions_pkey;
ALTER TABLE IF EXISTS ONLY public.auth_group_permissions DROP CONSTRAINT IF EXISTS auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
ALTER TABLE IF EXISTS ONLY public.auth_group DROP CONSTRAINT IF EXISTS auth_group_name_key;
DROP TABLE IF EXISTS public.wagtailusers_userprofile;
DROP TABLE IF EXISTS public.wagtailsearchpromotions_searchpromotion;
DROP TABLE IF EXISTS public.wagtailsearchpromotions_querydailyhits;
DROP TABLE IF EXISTS public.wagtailsearchpromotions_query;
DROP TABLE IF EXISTS public.wagtailsearch_indexentry;
DROP TABLE IF EXISTS public.wagtailredirects_redirect;
DROP TABLE IF EXISTS public.wagtailimages_rendition;
DROP TABLE IF EXISTS public.wagtailimages_image;
DROP TABLE IF EXISTS public.wagtailforms_formsubmission;
DROP TABLE IF EXISTS public.wagtailembeds_embed;
DROP TABLE IF EXISTS public.wagtaildocs_document;
DROP TABLE IF EXISTS public.wagtailcore_workflowtask;
DROP TABLE IF EXISTS public.wagtailcore_workflowstate;
DROP TABLE IF EXISTS public.wagtailcore_workflowpage;
DROP TABLE IF EXISTS public.wagtailcore_workflowcontenttype;
DROP TABLE IF EXISTS public.wagtailcore_workflow;
DROP TABLE IF EXISTS public.wagtailcore_uploadedfile;
DROP TABLE IF EXISTS public.wagtailcore_taskstate;
DROP TABLE IF EXISTS public.wagtailcore_task;
DROP TABLE IF EXISTS public.wagtailcore_site;
DROP TABLE IF EXISTS public.wagtailcore_referenceindex;
DROP TABLE IF EXISTS public.wagtailcore_pageviewrestriction_groups;
DROP TABLE IF EXISTS public.wagtailcore_pageviewrestriction;
DROP TABLE IF EXISTS public.wagtailcore_pagesubscription;
DROP TABLE IF EXISTS public.wagtailcore_revision;
DROP TABLE IF EXISTS public.wagtailcore_pagelogentry;
DROP TABLE IF EXISTS public.wagtailcore_page;
DROP TABLE IF EXISTS public.wagtailcore_modellogentry;
DROP TABLE IF EXISTS public.wagtailcore_locale;
DROP TABLE IF EXISTS public.wagtailcore_groupsitepermission;
DROP TABLE IF EXISTS public.wagtailcore_grouppagepermission;
DROP TABLE IF EXISTS public.wagtailcore_groupcollectionpermission;
DROP TABLE IF EXISTS public.wagtailcore_groupapprovaltask_groups;
DROP TABLE IF EXISTS public.wagtailcore_groupapprovaltask;
DROP TABLE IF EXISTS public.wagtailcore_commentreply;
DROP TABLE IF EXISTS public.wagtailcore_comment;
DROP TABLE IF EXISTS public.wagtailcore_collectionviewrestriction_groups;
DROP TABLE IF EXISTS public.wagtailcore_collectionviewrestriction;
DROP TABLE IF EXISTS public.wagtailcore_collection;
DROP TABLE IF EXISTS public.wagtailadmin_editingsession;
DROP TABLE IF EXISTS public.wagtailadmin_admin;
DROP TABLE IF EXISTS public.taggit_taggeditem;
DROP TABLE IF EXISTS public.taggit_tag;
DROP TABLE IF EXISTS public.projects_projecttag;
DROP TABLE IF EXISTS public.projects_projectpagetag;
DROP TABLE IF EXISTS public.projects_projectpageimage;
DROP TABLE IF EXISTS public.projects_projectpage;
DROP TABLE IF EXISTS public.projects_projectimage;
DROP TABLE IF EXISTS public.projects_project;
DROP TABLE IF EXISTS public.pages_testimonial;
DROP TABLE IF EXISTS public.pages_sitesettings;
DROP TABLE IF EXISTS public.pages_service;
DROP TABLE IF EXISTS public.pages_modularpage;
DROP TABLE IF EXISTS public.pages_logo;
DROP TABLE IF EXISTS public.pages_homepage;
DROP TABLE IF EXISTS public.pages_gallerypage;
DROP TABLE IF EXISTS public.pages_contactpage;
DROP TABLE IF EXISTS public.django_site;
DROP TABLE IF EXISTS public.django_session;
DROP TABLE IF EXISTS public.django_migrations;
DROP TABLE IF EXISTS public.django_content_type;
DROP TABLE IF EXISTS public.django_admin_log;
DROP TABLE IF EXISTS public.contacts_contactsubmission;
DROP TABLE IF EXISTS public.auth_user_user_permissions;
DROP TABLE IF EXISTS public.auth_user_groups;
DROP TABLE IF EXISTS public.auth_user;
DROP TABLE IF EXISTS public.auth_permission;
DROP TABLE IF EXISTS public.auth_group_permissions;
DROP TABLE IF EXISTS public.auth_group;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 221 (class 1259 OID 26274)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


--
-- TOC entry 220 (class 1259 OID 26273)
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 223 (class 1259 OID 26282)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- TOC entry 222 (class 1259 OID 26281)
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 219 (class 1259 OID 26268)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


--
-- TOC entry 218 (class 1259 OID 26267)
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 225 (class 1259 OID 26288)
-- Name: auth_user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


--
-- TOC entry 227 (class 1259 OID 26296)
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- TOC entry 226 (class 1259 OID 26295)
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_user_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 224 (class 1259 OID 26287)
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_user ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 229 (class 1259 OID 26302)
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- TOC entry 228 (class 1259 OID 26301)
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 243 (class 1259 OID 26486)
-- Name: contacts_contactsubmission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.contacts_contactsubmission (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    name character varying(255) NOT NULL,
    email character varying(254) NOT NULL,
    phone character varying(64) NOT NULL,
    message text NOT NULL,
    consent boolean NOT NULL,
    status character varying(16) NOT NULL,
    site_id integer NOT NULL
);


--
-- TOC entry 242 (class 1259 OID 26485)
-- Name: contacts_contactsubmission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.contacts_contactsubmission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.contacts_contactsubmission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 231 (class 1259 OID 26360)
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


--
-- TOC entry 230 (class 1259 OID 26359)
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 217 (class 1259 OID 26260)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- TOC entry 216 (class 1259 OID 26259)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 215 (class 1259 OID 26252)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- TOC entry 214 (class 1259 OID 26251)
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 313 (class 1259 OID 27429)
-- Name: django_session; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- TOC entry 315 (class 1259 OID 27439)
-- Name: django_site; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


--
-- TOC entry 314 (class 1259 OID 27438)
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_site ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 296 (class 1259 OID 27246)
-- Name: pages_contactpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_contactpage (
    page_ptr_id integer NOT NULL,
    intro text NOT NULL,
    show_contact_form boolean NOT NULL,
    contact_form_title character varying(255) NOT NULL,
    contact_form_intro text NOT NULL
);


--
-- TOC entry 297 (class 1259 OID 27253)
-- Name: pages_gallerypage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_gallerypage (
    page_ptr_id integer NOT NULL,
    intro text NOT NULL
);


--
-- TOC entry 295 (class 1259 OID 27234)
-- Name: pages_homepage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_homepage (
    page_ptr_id integer NOT NULL,
    intro text NOT NULL,
    body jsonb NOT NULL
);


--
-- TOC entry 304 (class 1259 OID 27294)
-- Name: pages_logo; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_logo (
    id bigint NOT NULL,
    title character varying(120) NOT NULL,
    url character varying(200) NOT NULL,
    image_id integer
);


--
-- TOC entry 303 (class 1259 OID 27293)
-- Name: pages_logo_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.pages_logo ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.pages_logo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 298 (class 1259 OID 27270)
-- Name: pages_modularpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_modularpage (
    page_ptr_id integer NOT NULL,
    intro text NOT NULL,
    body jsonb NOT NULL
);


--
-- TOC entry 300 (class 1259 OID 27278)
-- Name: pages_service; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_service (
    id bigint NOT NULL,
    title character varying(120) NOT NULL,
    description text NOT NULL
);


--
-- TOC entry 299 (class 1259 OID 27277)
-- Name: pages_service_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.pages_service ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.pages_service_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 306 (class 1259 OID 27324)
-- Name: pages_sitesettings; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_sitesettings (
    id bigint NOT NULL,
    company_name character varying(255) NOT NULL,
    phone character varying(50) NOT NULL,
    email character varying(254) NOT NULL,
    cvr character varying(20) NOT NULL,
    address text NOT NULL,
    default_theme character varying(20) NOT NULL,
    logo_id integer,
    site_id integer NOT NULL,
    copyright_text character varying(255) NOT NULL,
    footer_contact_title character varying(100) NOT NULL,
    footer_description text NOT NULL,
    navigation_cta_page_id integer,
    navigation_cta_text character varying(100) NOT NULL,
    show_navigation boolean NOT NULL,
    facebook_url character varying(200),
    footer_cta_button_text character varying(50) NOT NULL,
    footer_cta_text character varying(255) NOT NULL,
    footer_cta_title character varying(100) NOT NULL,
    instagram_url character varying(200),
    linkedin_url character varying(200),
    opening_hours text NOT NULL,
    footer_services_title character varying(100) NOT NULL,
    font_choice character varying(30) NOT NULL,
    enable_preview boolean NOT NULL,
    preview_url_override character varying(255) NOT NULL
);


--
-- TOC entry 305 (class 1259 OID 27323)
-- Name: pages_sitesettings_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.pages_sitesettings ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.pages_sitesettings_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 302 (class 1259 OID 27286)
-- Name: pages_testimonial; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_testimonial (
    id bigint NOT NULL,
    name character varying(120) NOT NULL,
    quote text NOT NULL,
    role character varying(120) NOT NULL
);


--
-- TOC entry 301 (class 1259 OID 27285)
-- Name: pages_testimonial_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.pages_testimonial ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.pages_testimonial_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 308 (class 1259 OID 27371)
-- Name: projects_project; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.projects_project (
    id bigint NOT NULL,
    title character varying(255) NOT NULL,
    slug character varying(255) NOT NULL,
    description text NOT NULL,
    featured boolean NOT NULL,
    published boolean NOT NULL,
    date date,
    client_name character varying(255) NOT NULL,
    location character varying(255) NOT NULL,
    materials text NOT NULL
);


--
-- TOC entry 307 (class 1259 OID 27370)
-- Name: projects_project_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.projects_project ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.projects_project_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 312 (class 1259 OID 27410)
-- Name: projects_projectimage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.projects_projectimage (
    id bigint NOT NULL,
    sort_order integer,
    caption character varying(500) NOT NULL,
    alt_text character varying(255) NOT NULL,
    image_id integer,
    project_id bigint NOT NULL
);


--
-- TOC entry 311 (class 1259 OID 27409)
-- Name: projects_projectimage_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.projects_projectimage ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.projects_projectimage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 332 (class 1259 OID 27668)
-- Name: projects_projectpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.projects_projectpage (
    page_ptr_id integer NOT NULL,
    description text NOT NULL,
    materials text NOT NULL,
    client_name character varying(255) NOT NULL,
    location character varying(255) NOT NULL,
    featured boolean NOT NULL,
    project_date date,
    estimated_budget numeric(10,2),
    priority character varying(10) NOT NULL,
    project_status character varying(20) NOT NULL
);


--
-- TOC entry 334 (class 1259 OID 27676)
-- Name: projects_projectpageimage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.projects_projectpageimage (
    id bigint NOT NULL,
    sort_order integer,
    caption character varying(500) NOT NULL,
    alt_text character varying(255) NOT NULL,
    image_id integer,
    project_page_id integer NOT NULL
);


--
-- TOC entry 333 (class 1259 OID 27675)
-- Name: projects_projectpageimage_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.projects_projectpageimage ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.projects_projectpageimage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 336 (class 1259 OID 27684)
-- Name: projects_projectpagetag; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.projects_projectpagetag (
    id bigint NOT NULL,
    content_object_id integer NOT NULL,
    tag_id integer NOT NULL
);


--
-- TOC entry 335 (class 1259 OID 27683)
-- Name: projects_projectpagetag_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.projects_projectpagetag ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.projects_projectpagetag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 310 (class 1259 OID 27381)
-- Name: projects_projecttag; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.projects_projecttag (
    id bigint NOT NULL,
    content_object_id bigint NOT NULL,
    tag_id integer NOT NULL
);


--
-- TOC entry 309 (class 1259 OID 27380)
-- Name: projects_projecttag_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.projects_projecttag ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.projects_projecttag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 288 (class 1259 OID 27147)
-- Name: taggit_tag; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.taggit_tag (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    slug character varying(100) NOT NULL
);


--
-- TOC entry 287 (class 1259 OID 27146)
-- Name: taggit_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.taggit_tag ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.taggit_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 290 (class 1259 OID 27157)
-- Name: taggit_taggeditem; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.taggit_taggeditem (
    id integer NOT NULL,
    object_id integer NOT NULL,
    content_type_id integer NOT NULL,
    tag_id integer NOT NULL
);


--
-- TOC entry 289 (class 1259 OID 27156)
-- Name: taggit_taggeditem_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.taggit_taggeditem ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.taggit_taggeditem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 317 (class 1259 OID 27448)
-- Name: wagtailadmin_admin; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailadmin_admin (
    id integer NOT NULL
);


--
-- TOC entry 316 (class 1259 OID 27447)
-- Name: wagtailadmin_admin_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailadmin_admin ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailadmin_admin_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 319 (class 1259 OID 27454)
-- Name: wagtailadmin_editingsession; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailadmin_editingsession (
    id integer NOT NULL,
    object_id character varying(255) NOT NULL,
    last_seen_at timestamp with time zone NOT NULL,
    content_type_id integer NOT NULL,
    user_id integer NOT NULL,
    is_editing boolean NOT NULL
);


--
-- TOC entry 318 (class 1259 OID 27453)
-- Name: wagtailadmin_editingsession_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailadmin_editingsession ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailadmin_editingsession_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 245 (class 1259 OID 26504)
-- Name: wagtailcore_collection; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_collection (
    id integer NOT NULL,
    path character varying(255) NOT NULL COLLATE pg_catalog."C",
    depth integer NOT NULL,
    numchild integer NOT NULL,
    name character varying(255) NOT NULL,
    CONSTRAINT wagtailcore_collection_depth_check CHECK ((depth >= 0)),
    CONSTRAINT wagtailcore_collection_numchild_check CHECK ((numchild >= 0))
);


--
-- TOC entry 244 (class 1259 OID 26503)
-- Name: wagtailcore_collection_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_collection ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_collection_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 251 (class 1259 OID 26574)
-- Name: wagtailcore_collectionviewrestriction; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_collectionviewrestriction (
    id integer NOT NULL,
    restriction_type character varying(20) NOT NULL,
    password character varying(255) NOT NULL,
    collection_id integer NOT NULL
);


--
-- TOC entry 253 (class 1259 OID 26580)
-- Name: wagtailcore_collectionviewrestriction_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_collectionviewrestriction_groups (
    id bigint NOT NULL,
    collectionviewrestriction_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- TOC entry 252 (class 1259 OID 26579)
-- Name: wagtailcore_collectionviewrestriction_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_collectionviewrestriction_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_collectionviewrestriction_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 250 (class 1259 OID 26573)
-- Name: wagtailcore_collectionviewrestriction_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_collectionviewrestriction ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_collectionviewrestriction_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 273 (class 1259 OID 26821)
-- Name: wagtailcore_comment; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_comment (
    id integer NOT NULL,
    text text NOT NULL,
    contentpath text NOT NULL,
    "position" text NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    resolved_at timestamp with time zone,
    page_id integer NOT NULL,
    resolved_by_id integer,
    revision_created_id integer,
    user_id integer NOT NULL
);


--
-- TOC entry 272 (class 1259 OID 26820)
-- Name: wagtailcore_comment_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_comment ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_comment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 275 (class 1259 OID 26829)
-- Name: wagtailcore_commentreply; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_commentreply (
    id integer NOT NULL,
    text text NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    comment_id integer NOT NULL,
    user_id integer NOT NULL
);


--
-- TOC entry 274 (class 1259 OID 26828)
-- Name: wagtailcore_commentreply_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_commentreply ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_commentreply_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 260 (class 1259 OID 26632)
-- Name: wagtailcore_groupapprovaltask; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_groupapprovaltask (
    task_ptr_id integer NOT NULL
);


--
-- TOC entry 267 (class 1259 OID 26663)
-- Name: wagtailcore_groupapprovaltask_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_groupapprovaltask_groups (
    id bigint NOT NULL,
    groupapprovaltask_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- TOC entry 266 (class 1259 OID 26662)
-- Name: wagtailcore_groupapprovaltask_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_groupapprovaltask_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_groupapprovaltask_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 247 (class 1259 OID 26517)
-- Name: wagtailcore_groupcollectionpermission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_groupcollectionpermission (
    id integer NOT NULL,
    collection_id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- TOC entry 246 (class 1259 OID 26516)
-- Name: wagtailcore_groupcollectionpermission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_groupcollectionpermission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_groupcollectionpermission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 235 (class 1259 OID 26403)
-- Name: wagtailcore_grouppagepermission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_grouppagepermission (
    id integer NOT NULL,
    group_id integer NOT NULL,
    page_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- TOC entry 234 (class 1259 OID 26402)
-- Name: wagtailcore_grouppagepermission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_grouppagepermission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_grouppagepermission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 286 (class 1259 OID 27121)
-- Name: wagtailcore_groupsitepermission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_groupsitepermission (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL,
    site_id integer NOT NULL
);


--
-- TOC entry 285 (class 1259 OID 27120)
-- Name: wagtailcore_groupsitepermission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_groupsitepermission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_groupsitepermission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 271 (class 1259 OID 26791)
-- Name: wagtailcore_locale; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_locale (
    id integer NOT NULL,
    language_code character varying(100) NOT NULL
);


--
-- TOC entry 270 (class 1259 OID 26790)
-- Name: wagtailcore_locale_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_locale ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_locale_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 279 (class 1259 OID 26893)
-- Name: wagtailcore_modellogentry; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_modellogentry (
    id integer NOT NULL,
    label text NOT NULL,
    action character varying(255) NOT NULL,
    data jsonb NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    content_changed boolean NOT NULL,
    deleted boolean NOT NULL,
    object_id character varying(255) NOT NULL,
    content_type_id integer,
    user_id integer,
    uuid uuid,
    revision_id integer
);


--
-- TOC entry 278 (class 1259 OID 26892)
-- Name: wagtailcore_modellogentry_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_modellogentry ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_modellogentry_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 233 (class 1259 OID 26389)
-- Name: wagtailcore_page; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_page (
    id integer NOT NULL,
    path character varying(255) NOT NULL COLLATE pg_catalog."C",
    depth integer NOT NULL,
    numchild integer NOT NULL,
    title character varying(255) NOT NULL,
    slug character varying(255) NOT NULL,
    live boolean NOT NULL,
    has_unpublished_changes boolean NOT NULL,
    url_path text NOT NULL,
    seo_title character varying(255) NOT NULL,
    show_in_menus boolean NOT NULL,
    search_description text NOT NULL,
    go_live_at timestamp with time zone,
    expire_at timestamp with time zone,
    expired boolean NOT NULL,
    content_type_id integer NOT NULL,
    owner_id integer,
    locked boolean NOT NULL,
    latest_revision_created_at timestamp with time zone,
    first_published_at timestamp with time zone,
    live_revision_id integer,
    last_published_at timestamp with time zone,
    draft_title character varying(255) NOT NULL,
    locked_at timestamp with time zone,
    locked_by_id integer,
    translation_key uuid NOT NULL,
    locale_id integer NOT NULL,
    alias_of_id integer,
    latest_revision_id integer,
    CONSTRAINT wagtailcore_page_depth_check CHECK ((depth >= 0)),
    CONSTRAINT wagtailcore_page_numchild_check CHECK ((numchild >= 0))
);


--
-- TOC entry 232 (class 1259 OID 26388)
-- Name: wagtailcore_page_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_page ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_page_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 269 (class 1259 OID 26771)
-- Name: wagtailcore_pagelogentry; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_pagelogentry (
    id integer NOT NULL,
    label text NOT NULL,
    action character varying(255) NOT NULL,
    data jsonb NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    content_changed boolean NOT NULL,
    deleted boolean NOT NULL,
    content_type_id integer,
    page_id integer NOT NULL,
    revision_id integer,
    user_id integer,
    uuid uuid
);


--
-- TOC entry 268 (class 1259 OID 26770)
-- Name: wagtailcore_pagelogentry_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_pagelogentry ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_pagelogentry_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 237 (class 1259 OID 26411)
-- Name: wagtailcore_revision; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_revision (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    content jsonb NOT NULL,
    approved_go_live_at timestamp with time zone,
    object_id character varying(255) NOT NULL,
    user_id integer,
    content_type_id integer NOT NULL,
    base_content_type_id integer NOT NULL,
    object_str text NOT NULL
);


--
-- TOC entry 236 (class 1259 OID 26410)
-- Name: wagtailcore_pagerevision_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_revision ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_pagerevision_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 277 (class 1259 OID 26837)
-- Name: wagtailcore_pagesubscription; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_pagesubscription (
    id integer NOT NULL,
    comment_notifications boolean NOT NULL,
    page_id integer NOT NULL,
    user_id integer NOT NULL
);


--
-- TOC entry 276 (class 1259 OID 26836)
-- Name: wagtailcore_pagesubscription_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_pagesubscription ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_pagesubscription_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 239 (class 1259 OID 26419)
-- Name: wagtailcore_pageviewrestriction; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_pageviewrestriction (
    id integer NOT NULL,
    password character varying(255) NOT NULL,
    page_id integer NOT NULL,
    restriction_type character varying(20) NOT NULL
);


--
-- TOC entry 249 (class 1259 OID 26547)
-- Name: wagtailcore_pageviewrestriction_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_pageviewrestriction_groups (
    id bigint NOT NULL,
    pageviewrestriction_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- TOC entry 248 (class 1259 OID 26546)
-- Name: wagtailcore_pageviewrestriction_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_pageviewrestriction_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_pageviewrestriction_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 238 (class 1259 OID 26418)
-- Name: wagtailcore_pageviewrestriction_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_pageviewrestriction ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_pageviewrestriction_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 281 (class 1259 OID 27006)
-- Name: wagtailcore_referenceindex; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_referenceindex (
    id integer NOT NULL,
    object_id character varying(255) NOT NULL,
    to_object_id character varying(255) NOT NULL,
    model_path text NOT NULL,
    content_path text NOT NULL,
    content_path_hash uuid NOT NULL,
    base_content_type_id integer NOT NULL,
    content_type_id integer NOT NULL,
    to_content_type_id integer NOT NULL
);


--
-- TOC entry 280 (class 1259 OID 27005)
-- Name: wagtailcore_referenceindex_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_referenceindex ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_referenceindex_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 241 (class 1259 OID 26425)
-- Name: wagtailcore_site; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_site (
    id integer NOT NULL,
    hostname character varying(255) NOT NULL,
    port integer NOT NULL,
    is_default_site boolean NOT NULL,
    root_page_id integer NOT NULL,
    site_name character varying(255) NOT NULL
);


--
-- TOC entry 240 (class 1259 OID 26424)
-- Name: wagtailcore_site_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_site ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 255 (class 1259 OID 26615)
-- Name: wagtailcore_task; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_task (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    active boolean NOT NULL,
    content_type_id integer NOT NULL
);


--
-- TOC entry 254 (class 1259 OID 26614)
-- Name: wagtailcore_task_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_task ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_task_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 257 (class 1259 OID 26621)
-- Name: wagtailcore_taskstate; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_taskstate (
    id integer NOT NULL,
    status character varying(50) NOT NULL,
    started_at timestamp with time zone NOT NULL,
    finished_at timestamp with time zone,
    content_type_id integer NOT NULL,
    revision_id integer NOT NULL,
    task_id integer NOT NULL,
    workflow_state_id integer NOT NULL,
    finished_by_id integer,
    comment text NOT NULL
);


--
-- TOC entry 256 (class 1259 OID 26620)
-- Name: wagtailcore_taskstate_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_taskstate ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_taskstate_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 284 (class 1259 OID 27103)
-- Name: wagtailcore_uploadedfile; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_uploadedfile (
    id integer NOT NULL,
    file character varying(200) NOT NULL,
    for_content_type_id integer,
    uploaded_by_user_id integer
);


--
-- TOC entry 283 (class 1259 OID 27102)
-- Name: wagtailcore_uploadedfile_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_uploadedfile ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_uploadedfile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 259 (class 1259 OID 26627)
-- Name: wagtailcore_workflow; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_workflow (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    active boolean NOT NULL
);


--
-- TOC entry 258 (class 1259 OID 26626)
-- Name: wagtailcore_workflow_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_workflow ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_workflow_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 282 (class 1259 OID 27070)
-- Name: wagtailcore_workflowcontenttype; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_workflowcontenttype (
    content_type_id integer NOT NULL,
    workflow_id integer NOT NULL
);


--
-- TOC entry 263 (class 1259 OID 26645)
-- Name: wagtailcore_workflowpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_workflowpage (
    page_id integer NOT NULL,
    workflow_id integer NOT NULL
);


--
-- TOC entry 262 (class 1259 OID 26638)
-- Name: wagtailcore_workflowstate; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_workflowstate (
    id integer NOT NULL,
    status character varying(50) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    current_task_state_id integer,
    object_id character varying(255) NOT NULL,
    requested_by_id integer,
    workflow_id integer NOT NULL,
    content_type_id integer NOT NULL,
    base_content_type_id integer NOT NULL
);


--
-- TOC entry 261 (class 1259 OID 26637)
-- Name: wagtailcore_workflowstate_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_workflowstate ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_workflowstate_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 265 (class 1259 OID 26656)
-- Name: wagtailcore_workflowtask; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_workflowtask (
    id integer NOT NULL,
    sort_order integer,
    task_id integer NOT NULL,
    workflow_id integer NOT NULL
);


--
-- TOC entry 264 (class 1259 OID 26655)
-- Name: wagtailcore_workflowtask_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailcore_workflowtask ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailcore_workflowtask_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 321 (class 1259 OID 27474)
-- Name: wagtaildocs_document; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtaildocs_document (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    file character varying(100) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    uploaded_by_user_id integer,
    collection_id integer NOT NULL,
    file_size bigint,
    file_hash character varying(40) NOT NULL,
    CONSTRAINT wagtaildocs_document_file_size_check CHECK ((file_size >= 0))
);


--
-- TOC entry 320 (class 1259 OID 27473)
-- Name: wagtaildocs_document_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtaildocs_document ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtaildocs_document_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 323 (class 1259 OID 27514)
-- Name: wagtailembeds_embed; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailembeds_embed (
    id integer NOT NULL,
    url text NOT NULL,
    max_width smallint,
    type character varying(10) NOT NULL,
    html text NOT NULL,
    title text NOT NULL,
    author_name text NOT NULL,
    provider_name text NOT NULL,
    thumbnail_url text NOT NULL,
    width integer,
    height integer,
    last_updated timestamp with time zone NOT NULL,
    hash character varying(32) NOT NULL,
    cache_until timestamp with time zone
);


--
-- TOC entry 322 (class 1259 OID 27513)
-- Name: wagtailembeds_embed_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailembeds_embed ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailembeds_embed_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 325 (class 1259 OID 27530)
-- Name: wagtailforms_formsubmission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailforms_formsubmission (
    id integer NOT NULL,
    form_data jsonb NOT NULL,
    submit_time timestamp with time zone NOT NULL,
    page_id integer NOT NULL
);


--
-- TOC entry 324 (class 1259 OID 27529)
-- Name: wagtailforms_formsubmission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailforms_formsubmission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailforms_formsubmission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 292 (class 1259 OID 27178)
-- Name: wagtailimages_image; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailimages_image (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    file character varying(100) NOT NULL,
    width integer NOT NULL,
    height integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    focal_point_x integer,
    focal_point_y integer,
    focal_point_width integer,
    focal_point_height integer,
    uploaded_by_user_id integer,
    file_size integer,
    collection_id integer NOT NULL,
    file_hash character varying(40) NOT NULL,
    description character varying(255) NOT NULL,
    CONSTRAINT wagtailimages_image_file_size_check CHECK ((file_size >= 0)),
    CONSTRAINT wagtailimages_image_focal_point_height_check CHECK ((focal_point_height >= 0)),
    CONSTRAINT wagtailimages_image_focal_point_width_check CHECK ((focal_point_width >= 0)),
    CONSTRAINT wagtailimages_image_focal_point_x_check CHECK ((focal_point_x >= 0)),
    CONSTRAINT wagtailimages_image_focal_point_y_check CHECK ((focal_point_y >= 0))
);


--
-- TOC entry 291 (class 1259 OID 27177)
-- Name: wagtailimages_image_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailimages_image ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailimages_image_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 294 (class 1259 OID 27189)
-- Name: wagtailimages_rendition; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailimages_rendition (
    id integer NOT NULL,
    file character varying(100) NOT NULL,
    width integer NOT NULL,
    height integer NOT NULL,
    focal_point_key character varying(16) NOT NULL,
    filter_spec character varying(255) NOT NULL,
    image_id integer NOT NULL
);


--
-- TOC entry 293 (class 1259 OID 27188)
-- Name: wagtailimages_rendition_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailimages_rendition ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailimages_rendition_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 327 (class 1259 OID 27551)
-- Name: wagtailredirects_redirect; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailredirects_redirect (
    id integer NOT NULL,
    old_path character varying(255) NOT NULL,
    is_permanent boolean NOT NULL,
    redirect_link character varying(255) NOT NULL,
    redirect_page_id integer,
    site_id integer,
    automatically_created boolean NOT NULL,
    created_at timestamp with time zone,
    redirect_page_route_path character varying(255) NOT NULL
);


--
-- TOC entry 326 (class 1259 OID 27550)
-- Name: wagtailredirects_redirect_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailredirects_redirect ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailredirects_redirect_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 329 (class 1259 OID 27623)
-- Name: wagtailsearch_indexentry; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailsearch_indexentry (
    id integer NOT NULL,
    object_id character varying(50) NOT NULL,
    title_norm double precision NOT NULL,
    content_type_id integer NOT NULL,
    autocomplete tsvector NOT NULL,
    title tsvector NOT NULL,
    body tsvector NOT NULL
);


--
-- TOC entry 328 (class 1259 OID 27622)
-- Name: wagtailsearch_indexentry_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailsearch_indexentry ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailsearch_indexentry_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 340 (class 1259 OID 27739)
-- Name: wagtailsearchpromotions_query; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailsearchpromotions_query (
    id integer NOT NULL,
    query_string character varying(255) NOT NULL
);


--
-- TOC entry 339 (class 1259 OID 27738)
-- Name: wagtailsearchpromotions_query_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailsearchpromotions_query ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailsearchpromotions_query_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 342 (class 1259 OID 27747)
-- Name: wagtailsearchpromotions_querydailyhits; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailsearchpromotions_querydailyhits (
    id integer NOT NULL,
    date date NOT NULL,
    hits integer NOT NULL,
    query_id integer NOT NULL
);


--
-- TOC entry 341 (class 1259 OID 27746)
-- Name: wagtailsearchpromotions_querydailyhits_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailsearchpromotions_querydailyhits ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailsearchpromotions_querydailyhits_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 338 (class 1259 OID 27719)
-- Name: wagtailsearchpromotions_searchpromotion; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailsearchpromotions_searchpromotion (
    id integer NOT NULL,
    sort_order integer,
    description text NOT NULL,
    page_id integer,
    query_id integer NOT NULL,
    external_link_text character varying(200),
    external_link_url character varying(200) NOT NULL
);


--
-- TOC entry 337 (class 1259 OID 27718)
-- Name: wagtailsearchpromotions_searchpromotion_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailsearchpromotions_searchpromotion ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailsearchpromotions_searchpromotion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 331 (class 1259 OID 27642)
-- Name: wagtailusers_userprofile; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailusers_userprofile (
    id integer NOT NULL,
    submitted_notifications boolean NOT NULL,
    approved_notifications boolean NOT NULL,
    rejected_notifications boolean NOT NULL,
    user_id integer NOT NULL,
    preferred_language character varying(10) NOT NULL,
    current_time_zone character varying(40) NOT NULL,
    avatar character varying(100) NOT NULL,
    updated_comments_notifications boolean NOT NULL,
    dismissibles jsonb NOT NULL,
    theme character varying(40) NOT NULL,
    density character varying(40) NOT NULL,
    contrast character varying(40) NOT NULL,
    keyboard_shortcuts boolean NOT NULL
);


--
-- TOC entry 330 (class 1259 OID 27641)
-- Name: wagtailusers_userprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wagtailusers_userprofile ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wagtailusers_userprofile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 4596 (class 0 OID 26274)
-- Dependencies: 221
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group (id, name) FROM stdin;
1	Moderators
2	Editors
\.


--
-- TOC entry 4598 (class 0 OID 26282)
-- Dependencies: 223
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	105
2	1	106
3	1	107
4	2	105
5	2	106
6	2	107
7	1	108
8	2	108
9	1	109
10	2	109
11	1	112
12	1	110
13	1	111
14	2	112
15	2	110
16	2	111
17	1	113
18	2	113
\.


--
-- TOC entry 4594 (class 0 OID 26268)
-- Dependencies: 219
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add locale	3	add_locale
2	Can change locale	3	change_locale
3	Can delete locale	3	delete_locale
4	Can view locale	3	view_locale
5	Can add site	4	add_site
6	Can change site	4	change_site
7	Can delete site	4	delete_site
8	Can view site	4	view_site
9	Can add group site permission	5	add_groupsitepermission
10	Can change group site permission	5	change_groupsitepermission
11	Can delete group site permission	5	delete_groupsitepermission
12	Can view group site permission	5	view_groupsitepermission
13	Can add model log entry	6	add_modellogentry
14	Can change model log entry	6	change_modellogentry
15	Can delete model log entry	6	delete_modellogentry
16	Can view model log entry	6	view_modellogentry
17	Can add revision	7	add_revision
18	Can change revision	7	change_revision
19	Can delete revision	7	delete_revision
20	Can view revision	7	view_revision
21	Can add collection view restriction	8	add_collectionviewrestriction
22	Can change collection view restriction	8	change_collectionviewrestriction
23	Can delete collection view restriction	8	delete_collectionviewrestriction
24	Can view collection view restriction	8	view_collectionviewrestriction
25	Can add collection	9	add_collection
26	Can change collection	9	change_collection
27	Can delete collection	9	delete_collection
28	Can view collection	9	view_collection
29	Can add group collection permission	10	add_groupcollectionpermission
30	Can change group collection permission	10	change_groupcollectionpermission
31	Can delete group collection permission	10	delete_groupcollectionpermission
32	Can view group collection permission	10	view_groupcollectionpermission
33	Can add uploaded file	11	add_uploadedfile
34	Can change uploaded file	11	change_uploadedfile
35	Can delete uploaded file	11	delete_uploadedfile
36	Can view uploaded file	11	view_uploadedfile
37	Can add workflow content type	12	add_workflowcontenttype
38	Can change workflow content type	12	change_workflowcontenttype
39	Can delete workflow content type	12	delete_workflowcontenttype
40	Can view workflow content type	12	view_workflowcontenttype
41	Can add Workflow state	13	add_workflowstate
42	Can change Workflow state	13	change_workflowstate
43	Can delete Workflow state	13	delete_workflowstate
44	Can view Workflow state	13	view_workflowstate
45	Can add workflow	14	add_workflow
46	Can change workflow	14	change_workflow
47	Can delete workflow	14	delete_workflow
48	Can view workflow	14	view_workflow
49	Can add workflow task order	15	add_workflowtask
50	Can change workflow task order	15	change_workflowtask
51	Can delete workflow task order	15	delete_workflowtask
52	Can view workflow task order	15	view_workflowtask
53	Can add task	16	add_task
54	Can change task	16	change_task
55	Can delete task	16	delete_task
56	Can view task	16	view_task
57	Can add Group approval task	2	add_groupapprovaltask
58	Can change Group approval task	2	change_groupapprovaltask
59	Can delete Group approval task	2	delete_groupapprovaltask
60	Can view Group approval task	2	view_groupapprovaltask
61	Can add Task state	17	add_taskstate
62	Can change Task state	17	change_taskstate
63	Can delete Task state	17	delete_taskstate
64	Can view Task state	17	view_taskstate
65	Can add page	1	add_page
66	Can change page	1	change_page
67	Can delete page	1	delete_page
68	Can view page	1	view_page
69	Delete pages with children	1	bulk_delete_page
70	Lock/unlock pages you've locked	1	lock_page
71	Publish any page	1	publish_page
72	Unlock any page	1	unlock_page
73	Can add group page permission	18	add_grouppagepermission
74	Can change group page permission	18	change_grouppagepermission
75	Can delete group page permission	18	delete_grouppagepermission
76	Can view group page permission	18	view_grouppagepermission
77	Can add page view restriction	19	add_pageviewrestriction
78	Can change page view restriction	19	change_pageviewrestriction
79	Can delete page view restriction	19	delete_pageviewrestriction
80	Can view page view restriction	19	view_pageviewrestriction
81	Can add workflow page	20	add_workflowpage
82	Can change workflow page	20	change_workflowpage
83	Can delete workflow page	20	delete_workflowpage
84	Can view workflow page	20	view_workflowpage
85	Can add page log entry	21	add_pagelogentry
86	Can change page log entry	21	change_pagelogentry
87	Can delete page log entry	21	delete_pagelogentry
88	Can view page log entry	21	view_pagelogentry
89	Can add comment	22	add_comment
90	Can change comment	22	change_comment
91	Can delete comment	22	delete_comment
92	Can view comment	22	view_comment
93	Can add comment reply	23	add_commentreply
94	Can change comment reply	23	change_commentreply
95	Can delete comment reply	23	delete_commentreply
96	Can view comment reply	23	view_commentreply
97	Can add page subscription	24	add_pagesubscription
98	Can change page subscription	24	change_pagesubscription
99	Can delete page subscription	24	delete_pagesubscription
100	Can view page subscription	24	view_pagesubscription
101	Can add reference index	25	add_referenceindex
102	Can change reference index	25	change_referenceindex
103	Can delete reference index	25	delete_referenceindex
104	Can view reference index	25	view_referenceindex
105	Can add image	26	add_image
106	Can change image	26	change_image
107	Can delete image	26	delete_image
108	Can access Wagtail admin	27	access_admin
109	Can choose image	26	choose_image
110	Can add document	28	add_document
111	Can change document	28	change_document
112	Can delete document	28	delete_document
113	Can choose document	28	choose_document
114	Can add log entry	29	add_logentry
115	Can change log entry	29	change_logentry
116	Can delete log entry	29	delete_logentry
117	Can view log entry	29	view_logentry
118	Can add permission	30	add_permission
119	Can change permission	30	change_permission
120	Can delete permission	30	delete_permission
121	Can view permission	30	view_permission
122	Can add group	31	add_group
123	Can change group	31	change_group
124	Can delete group	31	delete_group
125	Can view group	31	view_group
126	Can add user	32	add_user
127	Can change user	32	change_user
128	Can delete user	32	delete_user
129	Can view user	32	view_user
130	Can add content type	33	add_contenttype
131	Can change content type	33	change_contenttype
132	Can delete content type	33	delete_contenttype
133	Can view content type	33	view_contenttype
134	Can add session	34	add_session
135	Can change session	34	change_session
136	Can delete session	34	delete_session
137	Can view session	34	view_session
138	Can add site	35	add_site
139	Can change site	35	change_site
140	Can delete site	35	delete_site
141	Can view site	35	view_site
142	Can add form submission	36	add_formsubmission
143	Can change form submission	36	change_formsubmission
144	Can delete form submission	36	delete_formsubmission
145	Can view form submission	36	view_formsubmission
146	Can add redirect	37	add_redirect
147	Can change redirect	37	change_redirect
148	Can delete redirect	37	delete_redirect
149	Can view redirect	37	view_redirect
150	Can add embed	38	add_embed
151	Can change embed	38	change_embed
152	Can delete embed	38	delete_embed
153	Can view embed	38	view_embed
154	Can add user profile	39	add_userprofile
155	Can change user profile	39	change_userprofile
156	Can delete user profile	39	delete_userprofile
157	Can view user profile	39	view_userprofile
158	Can view document	28	view_document
159	Can view image	26	view_image
160	Can add rendition	44	add_rendition
161	Can change rendition	44	change_rendition
162	Can delete rendition	44	delete_rendition
163	Can view rendition	44	view_rendition
164	Can add index entry	45	add_indexentry
165	Can change index entry	45	change_indexentry
166	Can delete index entry	45	delete_indexentry
167	Can view index entry	45	view_indexentry
168	Can add editing session	46	add_editingsession
169	Can change editing session	46	change_editingsession
170	Can delete editing session	46	delete_editingsession
171	Can view editing session	46	view_editingsession
172	Can add tag	47	add_tag
173	Can change tag	47	change_tag
174	Can delete tag	47	delete_tag
175	Can view tag	47	view_tag
176	Can add tagged item	48	add_taggeditem
177	Can change tagged item	48	change_taggeditem
178	Can delete tagged item	48	delete_taggeditem
179	Can view tagged item	48	view_taggeditem
180	Can add Hjemmeside	49	add_homepage
181	Can change Hjemmeside	49	change_homepage
182	Can delete Hjemmeside	49	delete_homepage
183	Can view Hjemmeside	49	view_homepage
184	Can add Kontakt Side	50	add_contactpage
185	Can change Kontakt Side	50	change_contactpage
186	Can delete Kontakt Side	50	delete_contactpage
187	Can view Kontakt Side	50	view_contactpage
188	Can add Galleri Side	51	add_gallerypage
189	Can change Galleri Side	51	change_gallerypage
190	Can delete Galleri Side	51	delete_gallerypage
191	Can view Galleri Side	51	view_gallerypage
192	Can add Modul side	52	add_modularpage
193	Can change Modul side	52	change_modularpage
194	Can delete Modul side	52	delete_modularpage
195	Can view Modul side	52	view_modularpage
196	Can add Service	42	add_service
197	Can change Service	42	change_service
198	Can delete Service	42	delete_service
199	Can view Service	42	view_service
200	Can add Udtalelse	43	add_testimonial
201	Can change Udtalelse	43	change_testimonial
202	Can delete Udtalelse	43	delete_testimonial
203	Can view Udtalelse	43	view_testimonial
204	Can add Logo	40	add_logo
205	Can change Logo	40	change_logo
206	Can delete Logo	40	delete_logo
207	Can view Logo	40	view_logo
208	Can add Generelle indstillinger	53	add_sitesettings
209	Can change Generelle indstillinger	53	change_sitesettings
210	Can delete Generelle indstillinger	53	delete_sitesettings
211	Can view Generelle indstillinger	53	view_sitesettings
212	Can add Projekt	41	add_project
213	Can change Projekt	41	change_project
214	Can delete Projekt	41	delete_project
215	Can view Projekt	41	view_project
216	Can add project tag	54	add_projecttag
217	Can change project tag	54	change_projecttag
218	Can delete project tag	54	delete_projecttag
219	Can view project tag	54	view_projecttag
220	Can add Projekt billede	55	add_projectimage
221	Can change Projekt billede	55	change_projectimage
222	Can delete Projekt billede	55	delete_projectimage
223	Can view Projekt billede	55	view_projectimage
224	Can add contact submission	56	add_contactsubmission
225	Can change contact submission	56	change_contactsubmission
226	Can delete contact submission	56	delete_contactsubmission
227	Can view contact submission	56	view_contactsubmission
228	Can add Projekt billede	59	add_projectpageimage
229	Can change Projekt billede	59	change_projectpageimage
230	Can delete Projekt billede	59	delete_projectpageimage
231	Can view Projekt billede	59	view_projectpageimage
232	Can add project page tag	60	add_projectpagetag
233	Can change project page tag	60	change_projectpagetag
234	Can delete project page tag	60	delete_projectpagetag
235	Can view project page tag	60	view_projectpagetag
236	Can add Projekt Side	58	add_projectpage
237	Can change Projekt Side	58	change_projectpage
238	Can delete Projekt Side	58	delete_projectpage
239	Can view Projekt Side	58	view_projectpage
240	Can add search promotion	61	add_searchpromotion
241	Can change search promotion	61	change_searchpromotion
242	Can delete search promotion	61	delete_searchpromotion
243	Can view search promotion	61	view_searchpromotion
244	Can add query	62	add_query
245	Can change query	62	change_query
246	Can delete query	62	delete_query
247	Can view query	62	view_query
248	Can add Query Daily Hits	63	add_querydailyhits
249	Can change Query Daily Hits	63	change_querydailyhits
250	Can delete Query Daily Hits	63	delete_querydailyhits
251	Can view Query Daily Hits	63	view_querydailyhits
252	Can approve projects	58	can_approve_projects
253	Can manage project budget	58	can_manage_project_budget
254	Can set project priority	58	can_set_project_priority
\.


--
-- TOC entry 4600 (class 0 OID 26288)
-- Dependencies: 225
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$720000$TS2mlhQFc74VbVv5K9sAhm$wFI5eAhB1efQHUGj1/CQzaL/amNaOC4zBjDkIQsm9Xw=	2025-09-12 08:01:39.250428+02	t	admin			admin@example.com	t	t	2025-09-11 15:45:08.011701+02
\.


--
-- TOC entry 4602 (class 0 OID 26296)
-- Dependencies: 227
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- TOC entry 4604 (class 0 OID 26302)
-- Dependencies: 229
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- TOC entry 4618 (class 0 OID 26486)
-- Dependencies: 243
-- Data for Name: contacts_contactsubmission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.contacts_contactsubmission (id, created_at, name, email, phone, message, consent, status, site_id) FROM stdin;
\.


--
-- TOC entry 4606 (class 0 OID 26360)
-- Dependencies: 231
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- TOC entry 4592 (class 0 OID 26260)
-- Dependencies: 217
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	wagtailcore	page
2	wagtailcore	groupapprovaltask
3	wagtailcore	locale
4	wagtailcore	site
5	wagtailcore	groupsitepermission
6	wagtailcore	modellogentry
7	wagtailcore	revision
8	wagtailcore	collectionviewrestriction
9	wagtailcore	collection
10	wagtailcore	groupcollectionpermission
11	wagtailcore	uploadedfile
12	wagtailcore	workflowcontenttype
13	wagtailcore	workflowstate
14	wagtailcore	workflow
15	wagtailcore	workflowtask
16	wagtailcore	task
17	wagtailcore	taskstate
18	wagtailcore	grouppagepermission
19	wagtailcore	pageviewrestriction
20	wagtailcore	workflowpage
21	wagtailcore	pagelogentry
22	wagtailcore	comment
23	wagtailcore	commentreply
24	wagtailcore	pagesubscription
25	wagtailcore	referenceindex
26	wagtailimages	image
27	wagtailadmin	admin
28	wagtaildocs	document
29	admin	logentry
30	auth	permission
31	auth	group
32	auth	user
33	contenttypes	contenttype
34	sessions	session
35	sites	site
36	wagtailforms	formsubmission
37	wagtailredirects	redirect
38	wagtailembeds	embed
39	wagtailusers	userprofile
40	pages	logo
41	projects	project
42	pages	service
43	pages	testimonial
44	wagtailimages	rendition
45	wagtailsearch	indexentry
46	wagtailadmin	editingsession
47	taggit	tag
48	taggit	taggeditem
49	pages	homepage
50	pages	contactpage
51	pages	gallerypage
52	pages	modularpage
53	pages	sitesettings
54	projects	projecttag
55	projects	projectimage
56	contacts	contactsubmission
58	projects	projectpage
59	projects	projectpageimage
60	projects	projectpagetag
61	wagtailsearchpromotions	searchpromotion
62	wagtailsearchpromotions	query
63	wagtailsearchpromotions	querydailyhits
\.


--
-- TOC entry 4590 (class 0 OID 26252)
-- Dependencies: 215
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2025-09-11 15:44:58.405725+02
2	auth	0001_initial	2025-09-11 15:44:58.451132+02
3	admin	0001_initial	2025-09-11 15:44:58.460529+02
4	admin	0002_logentry_remove_auto_add	2025-09-11 15:44:58.462957+02
5	admin	0003_logentry_add_action_flag_choices	2025-09-11 15:44:58.465725+02
6	contenttypes	0002_remove_content_type_name	2025-09-11 15:44:58.47129+02
7	auth	0002_alter_permission_name_max_length	2025-09-11 15:44:58.474102+02
8	auth	0003_alter_user_email_max_length	2025-09-11 15:44:58.477023+02
9	auth	0004_alter_user_username_opts	2025-09-11 15:44:58.479335+02
10	auth	0005_alter_user_last_login_null	2025-09-11 15:44:58.48417+02
11	auth	0006_require_contenttypes_0002	2025-09-11 15:44:58.484692+02
12	auth	0007_alter_validators_add_error_messages	2025-09-11 15:44:58.48698+02
13	auth	0008_alter_user_username_max_length	2025-09-11 15:44:58.492971+02
14	auth	0009_alter_user_last_name_max_length	2025-09-11 15:44:58.496223+02
15	auth	0010_alter_group_name_max_length	2025-09-11 15:44:58.500037+02
16	auth	0011_update_proxy_permissions	2025-09-11 15:44:58.502459+02
17	auth	0012_alter_user_first_name_max_length	2025-09-11 15:44:58.505408+02
18	wagtailcore	0001_initial	2025-09-11 15:44:58.612511+02
19	wagtailcore	0002_initial_data	2025-09-11 15:44:58.614201+02
20	wagtailcore	0003_add_uniqueness_constraint_on_group_page_permission	2025-09-11 15:44:58.614632+02
21	wagtailcore	0004_page_locked	2025-09-11 15:44:58.615053+02
22	wagtailcore	0005_add_page_lock_permission_to_moderators	2025-09-11 15:44:58.615564+02
23	wagtailcore	0006_add_lock_page_permission	2025-09-11 15:44:58.615994+02
24	wagtailcore	0007_page_latest_revision_created_at	2025-09-11 15:44:58.616776+02
25	wagtailcore	0008_populate_latest_revision_created_at	2025-09-11 15:44:58.617228+02
26	wagtailcore	0009_remove_auto_now_add_from_pagerevision_created_at	2025-09-11 15:44:58.617688+02
27	wagtailcore	0010_change_page_owner_to_null_on_delete	2025-09-11 15:44:58.618105+02
28	wagtailcore	0011_page_first_published_at	2025-09-11 15:44:58.618527+02
29	wagtailcore	0012_extend_page_slug_field	2025-09-11 15:44:58.618955+02
30	wagtailcore	0013_update_golive_expire_help_text	2025-09-11 15:44:58.619395+02
31	wagtailcore	0014_add_verbose_name	2025-09-11 15:44:58.619817+02
32	wagtailcore	0015_add_more_verbose_names	2025-09-11 15:44:58.620217+02
33	wagtailcore	0016_change_page_url_path_to_text_field	2025-09-11 15:44:58.620627+02
34	contacts	0001_initial	2025-09-11 15:44:58.636782+02
35	wagtailcore	0017_change_edit_page_permission_description	2025-09-11 15:44:58.669986+02
36	wagtailcore	0018_pagerevision_submitted_for_moderation_index	2025-09-11 15:44:58.677134+02
37	wagtailcore	0019_verbose_names_cleanup	2025-09-11 15:44:58.690061+02
38	wagtailcore	0020_add_index_on_page_first_published_at	2025-09-11 15:44:58.696308+02
39	wagtailcore	0021_capitalizeverbose	2025-09-11 15:44:58.77915+02
40	wagtailcore	0022_add_site_name	2025-09-11 15:44:58.785887+02
41	wagtailcore	0023_alter_page_revision_on_delete_behaviour	2025-09-11 15:44:58.789845+02
42	wagtailcore	0024_collection	2025-09-11 15:44:58.799095+02
43	wagtailcore	0025_collection_initial_data	2025-09-11 15:44:58.804207+02
44	wagtailcore	0026_group_collection_permission	2025-09-11 15:44:58.825503+02
45	wagtailcore	0027_fix_collection_path_collation	2025-09-11 15:44:58.834591+02
46	wagtailcore	0024_alter_page_content_type_on_delete_behaviour	2025-09-11 15:44:58.840121+02
47	wagtailcore	0028_merge	2025-09-11 15:44:58.841236+02
48	wagtailcore	0029_unicode_slugfield_dj19	2025-09-11 15:44:58.845221+02
49	wagtailcore	0030_index_on_pagerevision_created_at	2025-09-11 15:44:58.85096+02
50	wagtailcore	0031_add_page_view_restriction_types	2025-09-11 15:44:58.877461+02
51	wagtailcore	0032_add_bulk_delete_page_permission	2025-09-11 15:44:58.881686+02
52	wagtailcore	0033_remove_golive_expiry_help_text	2025-09-11 15:44:58.888596+02
53	wagtailcore	0034_page_live_revision	2025-09-11 15:44:58.897562+02
54	wagtailcore	0035_page_last_published_at	2025-09-11 15:44:58.901952+02
55	wagtailcore	0036_populate_page_last_published_at	2025-09-11 15:44:58.909179+02
56	wagtailcore	0037_set_page_owner_editable	2025-09-11 15:44:58.914012+02
57	wagtailcore	0038_make_first_published_at_editable	2025-09-11 15:44:58.918126+02
58	wagtailcore	0039_collectionviewrestriction	2025-09-11 15:44:58.945012+02
59	wagtailcore	0040_page_draft_title	2025-09-11 15:44:58.957409+02
60	wagtailcore	0041_group_collection_permissions_verbose_name_plural	2025-09-11 15:44:58.961003+02
61	wagtailcore	0042_index_on_pagerevision_approved_go_live_at	2025-09-11 15:44:58.967252+02
62	wagtailcore	0043_lock_fields	2025-09-11 15:44:58.979874+02
63	wagtailcore	0044_add_unlock_grouppagepermission	2025-09-11 15:44:58.98387+02
64	wagtailcore	0045_assign_unlock_grouppagepermission	2025-09-11 15:44:58.992801+02
65	wagtailcore	0046_site_name_remove_null	2025-09-11 15:44:58.998938+02
66	wagtailcore	0047_add_workflow_models	2025-09-11 15:44:59.115125+02
67	wagtailcore	0048_add_default_workflows	2025-09-11 15:44:59.144564+02
68	wagtailcore	0049_taskstate_finished_by	2025-09-11 15:44:59.157764+02
69	wagtailcore	0050_workflow_rejected_to_needs_changes	2025-09-11 15:44:59.179623+02
70	wagtailcore	0051_taskstate_comment	2025-09-11 15:44:59.189079+02
71	wagtailcore	0052_pagelogentry	2025-09-11 15:44:59.214768+02
72	wagtailcore	0053_locale_model	2025-09-11 15:44:59.222132+02
73	wagtailcore	0054_initial_locale	2025-09-11 15:44:59.231488+02
74	wagtailcore	0055_page_locale_fields	2025-09-11 15:44:59.255571+02
75	wagtailcore	0056_page_locale_fields_populate	2025-09-11 15:44:59.269475+02
76	wagtailcore	0057_page_locale_fields_notnull	2025-09-11 15:44:59.295297+02
77	wagtailcore	0058_page_alias_of	2025-09-11 15:44:59.306556+02
78	wagtailcore	0059_apply_collection_ordering	2025-09-11 15:44:59.316548+02
79	wagtailcore	0060_fix_workflow_unique_constraint	2025-09-11 15:44:59.329989+02
80	wagtailcore	0061_change_promote_tab_helpt_text_and_verbose_names	2025-09-11 15:44:59.342636+02
81	wagtailcore	0062_comment_models_and_pagesubscription	2025-09-11 15:44:59.398844+02
82	wagtailcore	0063_modellogentry	2025-09-11 15:44:59.417157+02
83	wagtailcore	0064_log_timestamp_indexes	2025-09-11 15:44:59.432703+02
84	wagtailcore	0065_log_entry_uuid	2025-09-11 15:44:59.444106+02
85	wagtailcore	0066_collection_management_permissions	2025-09-11 15:44:59.456599+02
86	wagtailcore	0067_alter_pagerevision_content_json	2025-09-11 15:44:59.479461+02
87	wagtailcore	0068_log_entry_empty_object	2025-09-11 15:44:59.493396+02
88	wagtailcore	0069_log_entry_jsonfield	2025-09-11 15:44:59.541053+02
89	wagtailcore	0070_rename_pagerevision_revision	2025-09-11 15:44:59.69455+02
90	wagtailcore	0071_populate_revision_content_type	2025-09-11 15:44:59.705265+02
91	wagtailcore	0072_alter_revision_content_type_notnull	2025-09-11 15:44:59.736782+02
92	wagtailcore	0073_page_latest_revision	2025-09-11 15:44:59.750374+02
93	wagtailcore	0074_revision_object_str	2025-09-11 15:44:59.7568+02
94	wagtailcore	0075_populate_latest_revision_and_revision_object_str	2025-09-11 15:44:59.774019+02
95	wagtailcore	0076_modellogentry_revision	2025-09-11 15:44:59.787563+02
96	wagtailcore	0077_alter_revision_user	2025-09-11 15:44:59.79535+02
97	wagtailcore	0078_referenceindex	2025-09-11 15:44:59.821019+02
98	wagtailcore	0079_rename_taskstate_page_revision	2025-09-11 15:44:59.836179+02
99	wagtailcore	0080_generic_workflowstate	2025-09-11 15:44:59.916952+02
100	wagtailcore	0081_populate_workflowstate_content_type	2025-09-11 15:44:59.927567+02
101	wagtailcore	0082_alter_workflowstate_content_type_notnull	2025-09-11 15:44:59.960964+02
102	wagtailcore	0083_workflowcontenttype	2025-09-11 15:44:59.978488+02
103	wagtailcore	0084_add_default_page_permissions	2025-09-11 15:44:59.985409+02
104	wagtailcore	0085_add_grouppagepermission_permission	2025-09-11 15:45:00.003255+02
105	wagtailcore	0086_populate_grouppagepermission_permission	2025-09-11 15:45:00.043137+02
106	wagtailcore	0087_alter_grouppagepermission_unique_together_and_more	2025-09-11 15:45:00.077407+02
107	wagtailcore	0088_fix_log_entry_json_timestamps	2025-09-11 15:45:00.105868+02
108	wagtailcore	0089_log_entry_data_json_null_to_object	2025-09-11 15:45:00.115162+02
109	wagtailcore	0090_remove_grouppagepermission_permission_type	2025-09-11 15:45:00.149025+02
110	wagtailcore	0091_remove_revision_submitted_for_moderation	2025-09-11 15:45:00.159316+02
111	wagtailcore	0092_alter_collectionviewrestriction_password_and_more	2025-09-11 15:45:00.177247+02
112	wagtailcore	0093_uploadedfile	2025-09-11 15:45:00.197167+02
113	wagtailcore	0094_alter_page_locale	2025-09-11 15:45:00.206707+02
114	wagtailcore	0095_groupsitepermission	2025-09-11 15:45:00.231797+02
115	taggit	0001_initial	2025-09-11 15:45:00.256527+02
116	wagtailimages	0001_initial	2025-09-11 15:45:00.335205+02
117	wagtailimages	0002_initial_data	2025-09-11 15:45:00.335982+02
118	wagtailimages	0003_fix_focal_point_fields	2025-09-11 15:45:00.336281+02
119	wagtailimages	0004_make_focal_point_key_not_nullable	2025-09-11 15:45:00.336599+02
120	wagtailimages	0005_make_filter_spec_unique	2025-09-11 15:45:00.336897+02
121	wagtailimages	0006_add_verbose_names	2025-09-11 15:45:00.337185+02
122	wagtailimages	0007_image_file_size	2025-09-11 15:45:00.337482+02
123	wagtailimages	0008_image_created_at_index	2025-09-11 15:45:00.337772+02
124	wagtailimages	0009_capitalizeverbose	2025-09-11 15:45:00.33824+02
125	wagtailimages	0010_change_on_delete_behaviour	2025-09-11 15:45:00.338527+02
126	wagtailimages	0011_image_collection	2025-09-11 15:45:00.338814+02
127	wagtailimages	0012_copy_image_permissions_to_collections	2025-09-11 15:45:00.339097+02
128	wagtailimages	0013_make_rendition_upload_callable	2025-09-11 15:45:00.33938+02
129	wagtailimages	0014_add_filter_spec_field	2025-09-11 15:45:00.339663+02
130	wagtailimages	0015_fill_filter_spec_field	2025-09-11 15:45:00.339942+02
131	wagtailimages	0016_deprecate_rendition_filter_relation	2025-09-11 15:45:00.340236+02
132	wagtailimages	0017_reduce_focal_point_key_max_length	2025-09-11 15:45:00.34052+02
133	wagtailimages	0018_remove_rendition_filter	2025-09-11 15:45:00.3408+02
134	wagtailimages	0019_delete_filter	2025-09-11 15:45:00.341079+02
135	wagtailimages	0020_add-verbose-name	2025-09-11 15:45:00.341401+02
136	wagtailimages	0021_image_file_hash	2025-09-11 15:45:00.341721+02
137	wagtailimages	0022_uploadedimage	2025-09-11 15:45:00.355471+02
138	wagtailadmin	0001_create_admin_access_permissions	2025-09-11 15:45:00.368256+02
139	wagtailimages	0023_add_choose_permissions	2025-09-11 15:45:00.403326+02
140	wagtailimages	0024_index_image_file_hash	2025-09-11 15:45:00.415563+02
141	wagtailimages	0025_alter_image_file_alter_rendition_file	2025-09-11 15:45:00.424849+02
142	wagtailimages	0026_delete_uploadedimage	2025-09-11 15:45:00.42808+02
143	wagtailimages	0027_image_description	2025-09-11 15:45:00.439918+02
144	pages	0001_initial	2025-09-11 15:45:00.457316+02
145	pages	0002_contactpage_gallerypage_alter_homepage_options_and_more	2025-09-11 15:45:00.549683+02
146	pages	0003_modularpage_service_testimonial_and_more	2025-09-11 15:45:00.623629+02
147	pages	0004_alter_homepage_body	2025-09-11 15:45:00.6342+02
148	pages	0005_alter_homepage_body_alter_modularpage_body	2025-09-11 15:45:00.648619+02
149	pages	0006_sitesettings_delete_themesettings	2025-09-11 15:45:00.674511+02
150	pages	0007_remove_homepage_theme_override_and_more	2025-09-11 15:45:00.692639+02
151	pages	0008_sitesettings_copyright_text_and_more	2025-09-11 15:45:00.7603+02
152	pages	0009_alter_contactpage_contact_form_intro_and_more	2025-09-11 15:45:00.77694+02
153	pages	0010_remove_sitesettings_footer_services_title_and_more	2025-09-11 15:45:00.843638+02
154	pages	0011_auto_20250910_2113	2025-09-11 15:45:00.86587+02
155	pages	0012_sitesettings_footer_services_title	2025-09-11 15:45:00.875426+02
156	pages	0013_alter_sitesettings_facebook_url_and_more	2025-09-11 15:45:00.898272+02
157	pages	0014_alter_sitesettings_footer_cta_button_text_and_more	2025-09-11 15:45:00.928152+02
158	pages	0015_add_font_and_preview_settings	2025-09-11 15:45:00.953591+02
159	taggit	0002_auto_20150616_2121	2025-09-11 15:45:00.96359+02
160	taggit	0003_taggeditem_add_unique_index	2025-09-11 15:45:00.970831+02
161	taggit	0004_alter_taggeditem_content_type_alter_taggeditem_tag	2025-09-11 15:45:00.994178+02
162	taggit	0005_auto_20220424_2025	2025-09-11 15:45:01.006747+02
163	taggit	0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx	2025-09-11 15:45:01.023753+02
164	projects	0001_initial	2025-09-11 15:45:01.08046+02
165	projects	0002_alter_project_options_project_client_name_and_more	2025-09-11 15:45:01.159027+02
166	projects	0003_remove_project_project_type	2025-09-11 15:45:01.165277+02
167	projects	0004_remove_site_field	2025-09-11 15:45:01.229758+02
168	sessions	0001_initial	2025-09-11 15:45:01.237767+02
169	sites	0001_initial	2025-09-11 15:45:01.240623+02
170	sites	0002_alter_domain_unique	2025-09-11 15:45:01.244463+02
171	wagtailadmin	0002_admin	2025-09-11 15:45:01.245578+02
172	wagtailadmin	0003_admin_managed	2025-09-11 15:45:01.24878+02
173	wagtailadmin	0004_editingsession	2025-09-11 15:45:01.271087+02
174	wagtailadmin	0005_editingsession_is_editing	2025-09-11 15:45:01.279444+02
175	wagtaildocs	0001_initial	2025-09-11 15:45:01.29981+02
176	wagtaildocs	0002_initial_data	2025-09-11 15:45:01.323704+02
177	wagtaildocs	0003_add_verbose_names	2025-09-11 15:45:01.349572+02
178	wagtaildocs	0004_capitalizeverbose	2025-09-11 15:45:01.402375+02
179	wagtaildocs	0005_document_collection	2025-09-11 15:45:01.423887+02
180	wagtaildocs	0006_copy_document_permissions_to_collections	2025-09-11 15:45:01.442476+02
181	wagtaildocs	0005_alter_uploaded_by_user_on_delete_action	2025-09-11 15:45:01.456546+02
182	wagtaildocs	0007_merge	2025-09-11 15:45:01.457626+02
183	wagtaildocs	0008_document_file_size	2025-09-11 15:45:01.466622+02
184	wagtaildocs	0009_document_verbose_name_plural	2025-09-11 15:45:01.476443+02
185	wagtaildocs	0010_document_file_hash	2025-09-11 15:45:01.486372+02
186	wagtaildocs	0011_add_choose_permissions	2025-09-11 15:45:01.529288+02
187	wagtaildocs	0012_uploadeddocument	2025-09-11 15:45:01.55076+02
188	wagtaildocs	0013_delete_uploadeddocument	2025-09-11 15:45:01.553767+02
189	wagtaildocs	0014_alter_document_file_size	2025-09-11 15:45:01.569067+02
190	wagtailembeds	0001_initial	2025-09-11 15:45:01.579451+02
191	wagtailembeds	0002_add_verbose_names	2025-09-11 15:45:01.581405+02
192	wagtailembeds	0003_capitalizeverbose	2025-09-11 15:45:01.583433+02
193	wagtailembeds	0004_embed_verbose_name_plural	2025-09-11 15:45:01.585089+02
194	wagtailembeds	0005_specify_thumbnail_url_max_length	2025-09-11 15:45:01.588033+02
195	wagtailembeds	0006_add_embed_hash	2025-09-11 15:45:01.590814+02
196	wagtailembeds	0007_populate_hash	2025-09-11 15:45:01.607252+02
197	wagtailembeds	0008_allow_long_urls	2025-09-11 15:45:01.623745+02
198	wagtailembeds	0009_embed_cache_until	2025-09-11 15:45:01.628162+02
199	wagtailforms	0001_initial	2025-09-11 15:45:01.653858+02
200	wagtailforms	0002_add_verbose_names	2025-09-11 15:45:01.666608+02
201	wagtailforms	0003_capitalizeverbose	2025-09-11 15:45:01.678685+02
202	wagtailforms	0004_add_verbose_name_plural	2025-09-11 15:45:01.685729+02
203	wagtailforms	0005_alter_formsubmission_form_data	2025-09-11 15:45:01.697766+02
204	wagtailredirects	0001_initial	2025-09-11 15:45:01.727582+02
205	wagtailredirects	0002_add_verbose_names	2025-09-11 15:45:01.747952+02
206	wagtailredirects	0003_make_site_field_editable	2025-09-11 15:45:01.761997+02
207	wagtailredirects	0004_set_unique_on_path_and_site	2025-09-11 15:45:01.785979+02
208	wagtailredirects	0005_capitalizeverbose	2025-09-11 15:45:01.840426+02
209	wagtailredirects	0006_redirect_increase_max_length	2025-09-11 15:45:01.851498+02
210	wagtailredirects	0007_add_autocreate_fields	2025-09-11 15:45:01.874008+02
211	wagtailredirects	0008_add_verbose_name_plural	2025-09-11 15:45:01.882898+02
212	wagtailsearch	0001_initial	2025-09-11 15:45:01.939683+02
213	wagtailsearch	0002_add_verbose_names	2025-09-11 15:45:02.018985+02
214	wagtailsearch	0003_remove_editors_pick	2025-09-11 15:45:02.02066+02
215	wagtailsearch	0004_querydailyhits_verbose_name_plural	2025-09-11 15:45:02.022703+02
216	wagtailsearch	0005_create_indexentry	2025-09-11 15:45:02.051331+02
217	wagtailsearch	0006_customise_indexentry	2025-09-11 15:45:02.088261+02
218	wagtailsearch	0007_delete_editorspick	2025-09-11 15:45:02.096197+02
219	wagtailsearch	0008_remove_query_and_querydailyhits_models	2025-09-11 15:45:02.114499+02
220	wagtailsearch	0009_remove_ngram_autocomplete	2025-09-11 15:45:02.118334+02
221	wagtailusers	0001_initial	2025-09-11 15:45:02.140525+02
222	wagtailusers	0002_add_verbose_name_on_userprofile	2025-09-11 15:45:02.159752+02
223	wagtailusers	0003_add_verbose_names	2025-09-11 15:45:02.168135+02
224	wagtailusers	0004_capitalizeverbose	2025-09-11 15:45:02.192611+02
225	wagtailusers	0005_make_related_name_wagtail_specific	2025-09-11 15:45:02.207321+02
226	wagtailusers	0006_userprofile_prefered_language	2025-09-11 15:45:02.217771+02
227	wagtailusers	0007_userprofile_current_time_zone	2025-09-11 15:45:02.226354+02
228	wagtailusers	0008_userprofile_avatar	2025-09-11 15:45:02.234992+02
229	wagtailusers	0009_userprofile_verbose_name_plural	2025-09-11 15:45:02.24174+02
230	wagtailusers	0010_userprofile_updated_comments_notifications	2025-09-11 15:45:02.25046+02
231	wagtailusers	0011_userprofile_dismissibles	2025-09-11 15:45:02.261358+02
232	wagtailusers	0012_userprofile_theme	2025-09-11 15:45:02.269291+02
233	wagtailusers	0013_userprofile_density	2025-09-11 15:45:02.277145+02
234	wagtailusers	0014_userprofile_contrast	2025-09-11 15:45:02.287381+02
235	wagtailusers	0015_userprofile_keyboard_shortcuts	2025-09-11 15:45:02.295983+02
236	wagtailimages	0001_squashed_0021	2025-09-11 15:45:02.298483+02
237	wagtailcore	0001_squashed_0016_change_page_url_path_to_text_field	2025-09-11 15:45:02.298954+02
238	projects	0005_add_project_page_models	2025-09-11 16:22:40.038554+02
239	projects	0006_convert_projects_to_pages	2025-09-11 16:22:40.047142+02
240	projects	0007_convert_projects_to_pages_fixed	2025-09-11 16:23:49.90461+02
241	pages	0016_alter_contactpage_contact_form_intro_and_more	2025-09-11 16:34:35.499857+02
242	wagtailsearchpromotions	0001_initial	2025-09-11 16:34:35.540835+02
243	wagtailsearchpromotions	0002_capitalizeverbose	2025-09-11 16:34:35.591265+02
244	wagtailsearchpromotions	0003_query_querydailyhits	2025-09-11 16:34:35.608838+02
245	wagtailsearchpromotions	0004_copy_queries	2025-09-11 16:34:35.609431+02
246	wagtailsearchpromotions	0005_switch_query_model	2025-09-11 16:34:35.639943+02
247	wagtailsearchpromotions	0006_reset_query_sequence	2025-09-11 16:34:35.661703+02
248	wagtailsearchpromotions	0007_searchpromotion_external_link_text_and_more	2025-09-11 16:34:35.714993+02
249	projects	0008_alter_projectpage_options_projectpage_collection_and_more	2025-09-11 16:54:13.74418+02
250	projects	0009_remove_collection_field	2025-09-11 18:24:00.467668+02
\.


--
-- TOC entry 4688 (class 0 OID 27429)
-- Dependencies: 313
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
v1p3lz8mc0mnby7nhzernz29omlgyk3v	.eJxVjMEOwiAQRP-FsyFLsS3t0bvfQJZlFdSAgTbRGP9dSXrQZE4zb95LWFyXYNfKxUYvZqHE7rdzSFdObfAXTOcsKaelRCcbIre1ymP2fDts7J8gYA3tbfa6H432E6GHjjwjK02Dgo4RiBScaPpGITjmEdl0AIA9agOoBmrSyrXGnCw_7rE8xQzvD7RSP9A:1uwhd9:Y8ADH3psdneg1xwcbI4DfJQtIkFW-AN-zJgc6xCjga8	2025-09-25 15:46:31.162255+02
magqj7t49ktawuwf8xzowdluxhtb009i	.eJxVjEEOwiAQRe_C2pCxlGnr0r1nIMDMWNSAKW2iMd5dm3Sh2__efy_l_DKPbqk8uUTqoPZq97sFH6-cV0AXn89Fx5LnKQW9KnqjVZ8K8e24uX-B0dfx-27Ytj6SRBFGgM4gWGsitNCJNDiQDEgmoAm9geCFySBGS8G2A_Zg12jlWlPJjh_3ND3VAd4fn9s_Rg:1uwhzQ:gMYueolaleIJBVQ2vlu01wZHHF9MYJ2EH4TTnHoaTG0	2025-09-25 16:09:32.965561+02
uy37tcsk1e3a3fgbtax6wcoy2cccn3gu	.eJxVjEEOwiAQRe_C2pCxlGnr0r1nIMDMWNSAKW2iMd5dm3Sh2__efy_l_DKPbqk8uUTqoPZq97sFH6-cV0AXn89Fx5LnKQW9KnqjVZ8K8e24uX-B0dfx-27Ytj6SRBFGgM4gWGsitNCJNDiQDEgmoAm9geCFySBGS8G2A_Zg12jlWlPJjh_3ND3VAd4fn9s_Rg:1uwwqp:z9DPz4zlj1Ey86dFvuA27qOl8n3N_TrLu6erjaqNpEo	2025-09-26 08:01:39.252397+02
\.


--
-- TOC entry 4690 (class 0 OID 27439)
-- Dependencies: 315
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- TOC entry 4671 (class 0 OID 27246)
-- Dependencies: 296
-- Data for Name: pages_contactpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_contactpage (page_ptr_id, intro, show_contact_form, contact_form_title, contact_form_intro) FROM stdin;
5	<p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>	t	Send os en besked	<p>Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
\.


--
-- TOC entry 4672 (class 0 OID 27253)
-- Dependencies: 297
-- Data for Name: pages_gallerypage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_gallerypage (page_ptr_id, intro) FROM stdin;
4	<p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
11	
\.


--
-- TOC entry 4670 (class 0 OID 27234)
-- Dependencies: 295
-- Data for Name: pages_homepage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_homepage (page_ptr_id, intro, body) FROM stdin;
3	<p data-block-key="fichi">Professionelle bygge- og renoveringsløsninger med fokus på kvalitet og håndværk</p>	[{"id": "3475c607-30ae-48b8-bbd5-93b14c9218cb", "type": "hero_v2", "value": {"image": null, "style": {"divider": false, "spacing": "md", "container": "normal", "background": "hero"}, "heading": "Professionelle byggeløsninger i København og omegn", "subheading": "Fra køkkenrenovering til komplette nybyggerier - vi leverer håndværk af højeste kvalitet med fokus på kundetilfredshed og termintro fastholding.", "primary_page": 5, "primary_text": "Få et uforpligtende tilbud", "secondary_page": 4, "secondary_text": "Se vores projekter"}}, {"id": "fb18f1d7-0f6c-4b13-8d42-38eef9aa72d9", "type": "trust_badges", "value": {"items": [{"id": "01c444da-75ef-4754-9251-081ae07a8dcd", "type": "item", "value": {"icon": "star", "title": "Kvalitet i hver detalje", "description": "Vi går aldrig på kompromis med kvaliteten. Alle materialer og håndværk lever op til de højeste standarder."}}, {"id": "95a47f2f-fad0-4b0e-a08e-7ad574fee53d", "type": "item", "value": {"icon": "clock", "title": "Altid til tiden", "description": "Vi overholder altid vores deadlines og leverer projekter til tiden. Planlægning og pålidelighed er i højsædet."}}], "style": {"divider": false, "spacing": "md", "container": "normal", "background": "surface"}, "columns": "4", "heading": "Derfor vælger kunder JCleemannByg"}}, {"id": "90037c54-259e-4132-8d90-128931be7ceb", "type": "featured_projects", "value": {"style": {"divider": false, "spacing": "md", "container": "normal", "background": "surface"}, "columns": "3", "heading": "Udvalgte projekter", "subheading": "Se eksempler på vores seneste arbejde og få inspiration til dit næste projekt", "show_all_link": true, "all_projects_page": 4}}, {"id": "3d581778-17de-45f9-b911-fa5da29ca790", "type": "services_grid_inline", "value": {"items": [{"id": "338dfc7d-5ee7-433d-927d-42d4d25005f1", "type": "item", "value": {"icon": "check", "title": "Køkkenrenovering", "description": "Totalrenovering af køkkener med skræddersyede løsninger, kvalitetsmaterialer og moderne design"}}], "style": {"divider": false, "spacing": "md", "container": "normal", "background": "surface"}, "columns": "3", "heading": "Vores services"}}]
\.


--
-- TOC entry 4679 (class 0 OID 27294)
-- Dependencies: 304
-- Data for Name: pages_logo; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_logo (id, title, url, image_id) FROM stdin;
\.


--
-- TOC entry 4673 (class 0 OID 27270)
-- Dependencies: 298
-- Data for Name: pages_modularpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_modularpage (page_ptr_id, intro, body) FROM stdin;
\.


--
-- TOC entry 4675 (class 0 OID 27278)
-- Dependencies: 300
-- Data for Name: pages_service; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_service (id, title, description) FROM stdin;
\.


--
-- TOC entry 4681 (class 0 OID 27324)
-- Dependencies: 306
-- Data for Name: pages_sitesettings; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_sitesettings (id, company_name, phone, email, cvr, address, default_theme, logo_id, site_id, copyright_text, footer_contact_title, footer_description, navigation_cta_page_id, navigation_cta_text, show_navigation, facebook_url, footer_cta_button_text, footer_cta_text, footer_cta_title, instagram_url, linkedin_url, opening_hours, footer_services_title, font_choice, enable_preview, preview_url_override) FROM stdin;
1	JCleemannByg	+45 12 34 56 78	info@jcleemannbyg.dk	12345678	Eksempel Vej 123, 1234 København	forest	1	1	© 2025 JCleemannByg. Alle rettigheder forbeholdes.	Kontakt		\N		t	\N	Få et tilbud	Kontakt JCleemannByg i dag for et uforpligtende tilbud på dit næste projekt.	Klar til at starte?	\N	\N	Mandag - Fredag: 08:00 - 16:00\r\nLørdag: 08:00 - 12:00\r\nSøndag: Lukket	Services	inter-playfair	t	
\.


--
-- TOC entry 4677 (class 0 OID 27286)
-- Dependencies: 302
-- Data for Name: pages_testimonial; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_testimonial (id, name, quote, role) FROM stdin;
\.


--
-- TOC entry 4683 (class 0 OID 27371)
-- Dependencies: 308
-- Data for Name: projects_project; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects_project (id, title, slug, description, featured, published, date, client_name, location, materials) FROM stdin;
10	Træ terrasse og udendørs køkken	tr-terrasse-og-udendrs-kkken	<h3>Smukt udendørs køkken og terrasse</h3>\n                <p>Vi har bygget en fantastisk træterrasse med integreret udendørs køkken. Projektet omfatter:</p>\n                <ul>\n                    <li>Lærketræ terrasse på 45m²</li>\n                    <li>Indbygget grill og kogezone</li>\n                    <li>Opbevaringsløsninger i vejrbestandigt træ</li>\n                    <li>LED-belysning til aftentimer</li>\n                </ul>\n                <p>Materialer brugt: Lærketræ, rustfrit stål, natursten. Projektet blev færdiggjort til tiden og within budget.</p>	t	t	2024-08-15	Familie Hansen	Privat villa, Nordsjælland	Lærketræ, rustfrit stål, natursten
11	Villa renovering i København	villa-renovering-i-kbenhavn	<h3>Totalrenovering af historisk villa</h3>\n                <p>Komplet renovering af villa fra 1920'erne med respekt for den oprindelige arkitektur:</p>\n                <ul>\n                    <li>Restaurering af originale trægulve</li>\n                    <li>Modernisering af køkken og badeværelser</li>\n                    <li>Energioptimering med nye vinduer</li>\n                    <li>Tilbygning af moderne familierum</li>\n                </ul>\n                <p>Et smukt eksempel på hvordan historie og moderne komfort kan forenes harmonisk.</p>	t	t	2024-06-20	Privat kunde	Indre København	Eg, marmor, glas, tegl
12	Skræddersyet køkken installation	skrddersyet-kkken-installation	<h3>Håndlavet køkken efter mål</h3>\n                <p>Designet og bygget et unikt køkken der passer perfekt til kundens behov:</p>\n                <ul>\n                    <li>Massiv eg køkkenø med Corian bordplade</li>\n                    <li>Skræddersyede skabe i alle højder</li>\n                    <li>Integrerede hvidevarer af højeste kvalitet</li>\n                    <li>Skjult LED-belysning under skabe</li>\n                </ul>\n                <p>Køkkenet er både funktionelt og æstetisk smukt.</p>	f	t	2024-03-10		Frederiksberg	Massiv eg, Corian, rustfrit stål
13	Badeværelse renovering	badevrelse-renovering	<h3>Luksuriøst badeværelse</h3>\n                <p>Fuldstændig renovering af master badeværelse:</p>\n                <ul>\n                    <li>Italienske marmor fliser</li>\n                    <li>Fritstående badekar</li>\n                    <li>Regnbruser med termostat</li>\n                    <li>Skræddersyet vask møbel</li>\n                </ul>\n                <p>Et spa-lignende badeværelse der oser af luksus og komfort.</p>	f	t	2023-11-05		Gentofte	Marmor, messing, glas
14	Moderne kontorbygning	moderne-kontorbygning	<h3>Erhvervsprojekt med fokus på bæredygtighed</h3>\n                <p>Opførelse af moderne kontorbygning for mindre virksomhed:</p>\n                <ul>\n                    <li>Bæredygtige materialer i hele byggeriet</li>\n                    <li>Store glaspartier for naturligt lys</li>\n                    <li>Energieffektiv varme- og ventilationsystem</li>\n                    <li>Fleksible kontorrum der kan tilpasses</li>\n                </ul>\n                <p>Et moderne og miljøvenligt arbejdsmiljø.</p>	f	t	2023-09-15	TechStart ApS	Erhvervsområde, Glostrup	Træ, glas, beton, stål
\.


--
-- TOC entry 4687 (class 0 OID 27410)
-- Dependencies: 312
-- Data for Name: projects_projectimage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects_projectimage (id, sort_order, caption, alt_text, image_id, project_id) FROM stdin;
10	\N	Billede af Træ terrasse og udendørs køkken	Professionelt håndværk: Træ terrasse og udendørs køkken	10	10
11	\N	Billede af Villa renovering i København	Professionelt håndværk: Villa renovering i København	11	11
12	\N	Billede af Skræddersyet køkken installation	Professionelt håndværk: Skræddersyet køkken installation	12	12
13	\N	Billede af Badeværelse renovering	Professionelt håndværk: Badeværelse renovering	13	13
14	\N	Billede af Moderne kontorbygning	Professionelt håndværk: Moderne kontorbygning	14	14
\.


--
-- TOC entry 4707 (class 0 OID 27668)
-- Dependencies: 332
-- Data for Name: projects_projectpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects_projectpage (page_ptr_id, description, materials, client_name, location, featured, project_date, estimated_budget, priority, project_status) FROM stdin;
12					f	\N	\N	medium	planning
13					f	\N	\N	medium	planning
14					f	\N	\N	medium	planning
15					f	\N	\N	medium	planning
16					f	\N	\N	medium	planning
17					f	\N	\N	medium	planning
18					f	\N	\N	medium	planning
6	<h3>Smukt udendørs køkken og terrasse</h3>\n                <p>Vi har bygget en fantastisk træterrasse med integreret udendørs køkken. Projektet omfatter:</p>\n                <ul>\n                    <li>Lærketræ terrasse på 45m²</li>\n                    <li>Indbygget grill og kogezone</li>\n                    <li>Opbevaringsløsninger i vejrbestandigt træ</li>\n                    <li>LED-belysning til aftentimer</li>\n                </ul>\n                <p>Materialer brugt: Lærketræ, rustfrit stål, natursten. Projektet blev færdiggjort til tiden og within budget.</p>	Lærketræ, rustfrit stål, natursten	Familie Hansen	Privat villa, Nordsjælland	t	2024-08-15	\N	medium	planning
20					f	\N	\N	medium	planning
21					f	\N	\N	medium	planning
22					f	\N	\N	medium	planning
7	<h3>Totalrenovering af historisk villa</h3>\n                <p>Komplet renovering af villa fra 1920'erne med respekt for den oprindelige arkitektur:</p>\n                <ul>\n                    <li>Restaurering af originale trægulve</li>\n                    <li>Modernisering af køkken og badeværelser</li>\n                    <li>Energioptimering med nye vinduer</li>\n                    <li>Tilbygning af moderne familierum</li>\n                </ul>\n                <p>Et smukt eksempel på hvordan historie og moderne komfort kan forenes harmonisk.</p>	Eg, marmor, glas, tegl	Privat kunde	Indre København	t	2024-06-20	\N	medium	planning
8	<h3>Håndlavet køkken efter mål</h3>\n                <p>Designet og bygget et unikt køkken der passer perfekt til kundens behov:</p>\n                <ul>\n                    <li>Massiv eg køkkenø med Corian bordplade</li>\n                    <li>Skræddersyede skabe i alle højder</li>\n                    <li>Integrerede hvidevarer af højeste kvalitet</li>\n                    <li>Skjult LED-belysning under skabe</li>\n                </ul>\n                <p>Køkkenet er både funktionelt og æstetisk smukt.</p>	Massiv eg, Corian, rustfrit stål		Frederiksberg	f	2024-03-10	\N	medium	planning
24					f	\N	\N	medium	planning
9	<h3>Luksuriøst badeværelse</h3>\n                <p>Fuldstændig renovering af master badeværelse:</p>\n                <ul>\n                    <li>Italienske marmor fliser</li>\n                    <li>Fritstående badekar</li>\n                    <li>Regnbruser med termostat</li>\n                    <li>Skræddersyet vask møbel</li>\n                </ul>\n                <p>Et spa-lignende badeværelse der oser af luksus og komfort.</p>	Marmor, messing, glas		Gentofte	f	2023-11-05	\N	medium	planning
25					f	\N	\N	medium	planning
10	<h3>Erhvervsprojekt med fokus på bæredygtighed</h3>\n                <p>Opførelse af moderne kontorbygning for mindre virksomhed:</p>\n                <ul>\n                    <li>Bæredygtige materialer i hele byggeriet</li>\n                    <li>Store glaspartier for naturligt lys</li>\n                    <li>Energieffektiv varme- og ventilationsystem</li>\n                    <li>Fleksible kontorrum der kan tilpasses</li>\n                </ul>\n                <p>Et moderne og miljøvenligt arbejdsmiljø.</p>	Træ, glas, beton, stål	TechStart ApS	Erhvervsområde, Glostrup	f	2023-09-15	\N	medium	planning
26	Perfekt tidspunkt at få fjernet råd og lavet en lus! 🦔\n#tømrer				f	\N	\N	medium	planning
27	Trods byger og blæst har vi fået lavet undertag, kvist og nyt solstrålerne!😎🌞\nNu en lang weekend til mig!🍺				f	\N	\N	medium	planning
28	Men ruden var knust, det er den ikke længere. Det er en succes i min bog 🐳\nGod dag derude				f	\N	\N	medium	planning
29	Mit første møbel er et simpelt sofabord til min egen stue, det næste bliver at give sig i kast med to runde linoleumsborde🌚				f	\N	\N	medium	planning
30	Behandlet med linolie og linoliemaling.🖌️				f	\N	\N	medium	planning
19	Dejligt at kunne være semi indenfor nu efteråret for alvor er sat ind 🍁🦔				f	\N	\N	medium	planning
31					f	\N	\N	medium	planning
32	Så kommer der ikke vand ind der længere 🥸				f	\N	\N	medium	planning
33					f	\N	\N	medium	planning
23	Efter og før				f	\N	\N	medium	planning
\.


--
-- TOC entry 4709 (class 0 OID 27676)
-- Dependencies: 334
-- Data for Name: projects_projectpageimage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects_projectpageimage (id, sort_order, caption, alt_text, image_id, project_page_id) FROM stdin;
1	\N	Billede af Træ terrasse og udendørs køkken	Professionelt håndværk: Træ terrasse og udendørs køkken	10	6
2	\N	Billede af Villa renovering i København	Professionelt håndværk: Villa renovering i København	11	7
3	\N	Billede af Skræddersyet køkken installation	Professionelt håndværk: Skræddersyet køkken installation	12	8
4	\N	Billede af Badeværelse renovering	Professionelt håndværk: Badeværelse renovering	13	9
5	\N	Billede af Moderne kontorbygning	Professionelt håndværk: Moderne kontorbygning	14	10
6	\N			15	12
7	\N			16	13
8	\N			17	13
9	\N			18	14
10	\N			19	14
11	\N			20	14
12	\N			21	14
13	\N			22	15
14	\N			23	15
15	\N			24	15
16	\N			25	16
17	\N			26	16
18	\N			27	17
19	\N			28	17
20	\N			29	18
21	\N			30	18
25	\N			34	20
26	\N			35	20
27	\N			36	20
28	\N			37	20
29	\N			38	20
30	\N			39	21
31	\N			40	21
32	\N			41	22
33	\N			42	22
36	\N			45	24
37	\N			46	25
38	\N			47	25
39	\N			48	26
40	\N			49	26
41	\N			50	26
42	\N			51	26
43	\N			52	27
44	\N			53	27
45	\N			54	27
46	\N			55	28
47	\N			56	28
48	\N			57	29
49	\N			58	29
50	\N			59	30
51	\N			60	30
22	\N			31	19
23	\N			32	19
24	\N			33	19
52	\N			64	31
53	\N			65	31
54	\N			66	31
55	\N			67	31
56	\N			68	31
57	\N			69	32
58	\N			70	32
59	\N			71	33
60	\N			72	33
34	\N			43	23
35	\N			44	23
\.


--
-- TOC entry 4711 (class 0 OID 27684)
-- Dependencies: 336
-- Data for Name: projects_projectpagetag; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects_projectpagetag (id, content_object_id, tag_id) FROM stdin;
1	6	1
2	6	2
3	6	3
4	6	4
5	7	5
6	7	6
7	7	7
8	7	8
9	8	3
10	8	9
11	8	10
12	9	11
13	9	5
14	9	12
15	10	13
16	10	14
17	10	15
18	10	16
\.


--
-- TOC entry 4685 (class 0 OID 27381)
-- Dependencies: 310
-- Data for Name: projects_projecttag; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects_projecttag (id, content_object_id, tag_id) FROM stdin;
\.


--
-- TOC entry 4663 (class 0 OID 27147)
-- Dependencies: 288
-- Data for Name: taggit_tag; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.taggit_tag (id, name, slug) FROM stdin;
1	udendoers	udendoers
2	terrasse	terrasse
3	koekken	koekken
4	traeterre	traeterre
5	renovering	renovering
6	villa	villa
7	historisk	historisk
8	koebenhavn	koebenhavn
9	skreddersyet	skreddersyet
10	installation	installation
11	badevaerelse	badevaerelse
12	luksurios	luksurios
13	kontor	kontor
14	moderne	moderne
15	erhverv	erhverv
16	baeredygtig	baeredygtig
\.


--
-- TOC entry 4665 (class 0 OID 27157)
-- Dependencies: 290
-- Data for Name: taggit_taggeditem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.taggit_taggeditem (id, object_id, content_type_id, tag_id) FROM stdin;
\.


--
-- TOC entry 4692 (class 0 OID 27448)
-- Dependencies: 317
-- Data for Name: wagtailadmin_admin; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailadmin_admin (id) FROM stdin;
\.


--
-- TOC entry 4694 (class 0 OID 27454)
-- Dependencies: 319
-- Data for Name: wagtailadmin_editingsession; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailadmin_editingsession (id, object_id, last_seen_at, content_type_id, user_id, is_editing) FROM stdin;
\.


--
-- TOC entry 4620 (class 0 OID 26504)
-- Dependencies: 245
-- Data for Name: wagtailcore_collection; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_collection (id, path, depth, numchild, name) FROM stdin;
1	0001	1	0	Root
\.


--
-- TOC entry 4626 (class 0 OID 26574)
-- Dependencies: 251
-- Data for Name: wagtailcore_collectionviewrestriction; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_collectionviewrestriction (id, restriction_type, password, collection_id) FROM stdin;
\.


--
-- TOC entry 4628 (class 0 OID 26580)
-- Dependencies: 253
-- Data for Name: wagtailcore_collectionviewrestriction_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_collectionviewrestriction_groups (id, collectionviewrestriction_id, group_id) FROM stdin;
\.


--
-- TOC entry 4648 (class 0 OID 26821)
-- Dependencies: 273
-- Data for Name: wagtailcore_comment; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_comment (id, text, contentpath, "position", created_at, updated_at, resolved_at, page_id, resolved_by_id, revision_created_id, user_id) FROM stdin;
\.


--
-- TOC entry 4650 (class 0 OID 26829)
-- Dependencies: 275
-- Data for Name: wagtailcore_commentreply; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_commentreply (id, text, created_at, updated_at, comment_id, user_id) FROM stdin;
\.


--
-- TOC entry 4635 (class 0 OID 26632)
-- Dependencies: 260
-- Data for Name: wagtailcore_groupapprovaltask; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_groupapprovaltask (task_ptr_id) FROM stdin;
1
\.


--
-- TOC entry 4642 (class 0 OID 26663)
-- Dependencies: 267
-- Data for Name: wagtailcore_groupapprovaltask_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_groupapprovaltask_groups (id, groupapprovaltask_id, group_id) FROM stdin;
1	1	1
\.


--
-- TOC entry 4622 (class 0 OID 26517)
-- Dependencies: 247
-- Data for Name: wagtailcore_groupcollectionpermission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_groupcollectionpermission (id, collection_id, group_id, permission_id) FROM stdin;
1	1	1	105
2	1	2	105
3	1	1	106
4	1	2	106
5	1	1	109
6	1	2	109
7	1	1	110
8	1	2	110
9	1	1	111
10	1	2	111
11	1	1	113
12	1	2	113
\.


--
-- TOC entry 4610 (class 0 OID 26403)
-- Dependencies: 235
-- Data for Name: wagtailcore_grouppagepermission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_grouppagepermission (id, group_id, page_id, permission_id) FROM stdin;
1	1	1	65
2	1	1	66
3	1	1	71
4	2	1	65
5	2	1	66
6	1	1	70
7	1	1	72
\.


--
-- TOC entry 4661 (class 0 OID 27121)
-- Dependencies: 286
-- Data for Name: wagtailcore_groupsitepermission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_groupsitepermission (id, group_id, permission_id, site_id) FROM stdin;
\.


--
-- TOC entry 4646 (class 0 OID 26791)
-- Dependencies: 271
-- Data for Name: wagtailcore_locale; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_locale (id, language_code) FROM stdin;
1	da
\.


--
-- TOC entry 4654 (class 0 OID 26893)
-- Dependencies: 279
-- Data for Name: wagtailcore_modellogentry; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_modellogentry (id, label, action, data, "timestamp", content_changed, deleted, object_id, content_type_id, user_id, uuid, revision_id) FROM stdin;
1	Generelle indstillinger for localhost [standardindstilling]	wagtail.edit	{}	2025-09-11 16:12:41.599939+02	t	f	1	53	1	d3c46905-e624-4d9a-8ad4-ad8dcf2e9308	\N
\.


--
-- TOC entry 4608 (class 0 OID 26389)
-- Dependencies: 233
-- Data for Name: wagtailcore_page; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_page (id, path, depth, numchild, title, slug, live, has_unpublished_changes, url_path, seo_title, show_in_menus, search_description, go_live_at, expire_at, expired, content_type_id, owner_id, locked, latest_revision_created_at, first_published_at, live_revision_id, last_published_at, draft_title, locked_at, locked_by_id, translation_key, locale_id, alias_of_id, latest_revision_id) FROM stdin;
6	0001000200020001	4	0	Træ terrasse og udendørs køkken	tr-terrasse-og-udendrs-kkken	t	f	/home-1/galleri/tr-terrasse-og-udendrs-kkken/		f		\N	\N	f	58	\N	f	\N	\N	\N	\N	Træ terrasse og udendørs køkken	\N	\N	64daaaf9-73a7-4274-85f1-d4717738b961	1	\N	\N
1	0001	1	2	Root	root	t	f	/		f		\N	\N	f	1	\N	f	\N	\N	\N	\N	Root	\N	\N	06315736-99b7-4c3d-8d9f-7376af6c1faf	1	\N	\N
4	000100020002	3	5	Projekt Galleri	galleri	t	f	/home-1/galleri/		f		\N	\N	f	51	\N	f	2025-09-11 15:45:14.577423+02	2025-09-11 15:45:14.591057+02	2	2025-09-11 15:45:14.591057+02	Projekt Galleri	\N	\N	f18d5f96-a655-4c41-bc93-ba827d7e972d	1	\N	2
2	00010001	2	0	Welcome to your new Wagtail site!	home	t	f	/home/		f		\N	\N	f	1	\N	f	\N	\N	\N	\N	Welcome to your new Wagtail site!	\N	\N	746f9dbd-92b2-4971-979c-e7f9e9f989ec	1	\N	\N
24	000100020003000D	4	0	Lille trin udført i jatoba	lille-trin-udført-i-jatoba-2	t	f	/home-1/galleri-2/lille-trin-udført-i-jatoba-2/		f		\N	\N	f	58	\N	f	2025-09-11 18:13:58.260847+02	2025-09-11 18:13:58.264239+02	20	2025-09-11 18:13:58.264239+02	Lille trin udført i jatoba	\N	\N	2deacdfa-7c0c-4c16-8ea7-0a9f3e863413	1	\N	20
7	0001000200020002	4	0	Villa renovering i København	villa-renovering-i-kbenhavn	t	f	/home-1/galleri/villa-renovering-i-kbenhavn/		f		\N	\N	f	58	\N	f	\N	\N	\N	\N	Villa renovering i København	\N	\N	62db3e0a-ca81-464b-9a22-5f33ee8d05c2	1	\N	\N
25	000100020003000E	4	0	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗	nogen-gange-kan-man-spare-stilladset-det-kræver-bare-man-kan-lokke-nogen-til-at-sikre-den-anden-ende-af-det-reb-der-holder-dig-2	t	f	/home-1/galleri-2/nogen-gange-kan-man-spare-stilladset-det-kræver-bare-man-kan-lokke-nogen-til-at-sikre-den-anden-ende-af-det-reb-der-holder-dig-2/		f		\N	\N	f	58	\N	f	2025-09-11 18:13:58.317675+02	2025-09-11 18:13:58.320577+02	21	2025-09-11 18:13:58.320577+02	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗	\N	\N	b25769e5-8b2e-4951-beae-2e456922bcca	1	\N	21
3	00010002	2	3	Velkommen til JCleemannByg	home-1	t	f	/home-1/		f		\N	\N	f	49	\N	f	2025-09-11 16:01:51.176786+02	2025-09-11 15:45:14.529+02	6	2025-09-11 16:01:51.209615+02	Velkommen til JCleemannByg	\N	\N	3fc166df-3682-476a-ba86-e93c617785c0	1	\N	6
8	0001000200020003	4	0	Skræddersyet køkken installation	skrddersyet-kkken-installation	t	f	/home-1/galleri/skrddersyet-kkken-installation/		f		\N	\N	f	58	\N	f	\N	\N	\N	\N	Skræddersyet køkken installation	\N	\N	d7026c46-3e5d-499d-bc13-aeeae715fc74	1	\N	\N
26	000100020003000F	4	0	Fugen skulle skiftes på disse døre. 	fugen-skulle-skiftes-på-disse-døre-2	t	f	/home-1/galleri-2/fugen-skulle-skiftes-på-disse-døre-2/		f		\N	\N	f	58	\N	f	2025-09-11 18:13:58.370132+02	2025-09-11 18:13:58.372508+02	22	2025-09-11 18:13:58.372508+02	Fugen skulle skiftes på disse døre. 	\N	\N	4ad408f2-6cfc-4455-8cad-e2f92c4c4c4c	1	\N	22
9	0001000200020004	4	0	Badeværelse renovering	badevrelse-renovering	t	f	/home-1/galleri/badevrelse-renovering/		f		\N	\N	f	58	\N	f	\N	\N	\N	\N	Badeværelse renovering	\N	\N	6119dda3-b1f0-44de-ace3-bc874618ce74	1	\N	\N
27	000100020003000G	4	0	Lærepladsen bliver også passet🦦	lærepladsen-bliver-også-passet-2	t	f	/home-1/galleri-2/lærepladsen-bliver-også-passet-2/		f		\N	\N	f	58	\N	f	2025-09-11 18:13:58.453697+02	2025-09-11 18:13:58.456587+02	23	2025-09-11 18:13:58.456587+02	Lærepladsen bliver også passet🦦	\N	\N	3f41bf6f-190c-4646-89ee-c91c98f7e382	1	\N	23
5	000100020001	3	0	Kontakt Os	kontakt	t	f	/home-1/kontakt/		f		\N	\N	f	50	\N	f	2025-09-11 15:45:14.640185+02	2025-09-11 15:45:14.654193+02	3	2025-09-11 15:45:14.654193+02	Kontakt Os	\N	\N	1c559f5d-212e-44d6-893a-0163fe51b483	1	\N	3
10	0001000200020005	4	0	Moderne kontorbygning	moderne-kontorbygning	t	f	/home-1/galleri/moderne-kontorbygning/		f		\N	\N	f	58	\N	f	\N	\N	\N	\N	Moderne kontorbygning	\N	\N	5607ce71-3c2e-465f-911f-90c186d585e5	1	\N	\N
28	000100020003000H	4	0	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 	har-jeg-glemt-at-tage-et-før-billede-det-har-jeg-vist-nok-lige-2	t	f	/home-1/galleri-2/har-jeg-glemt-at-tage-et-før-billede-det-har-jeg-vist-nok-lige-2/		f		\N	\N	f	58	\N	f	2025-09-11 18:13:58.531466+02	2025-09-11 18:13:58.533888+02	24	2025-09-11 18:13:58.533888+02	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 	\N	\N	b590cb22-e762-4d39-9bbd-3aa0b942bfd5	1	\N	24
12	0001000200030001	4	0	Lille trin udført i jatoba	lille-trin-udført-i-jatoba	t	f	/home-1/galleri-2/lille-trin-udført-i-jatoba/		f		\N	\N	f	58	\N	f	2025-09-11 18:11:15.437926+02	2025-09-11 18:11:15.442612+02	8	2025-09-11 18:11:15.442612+02	Lille trin udført i jatoba	\N	\N	7808fd2a-0673-49e5-8320-8e55c192d7f3	1	\N	8
29	000100020003000I	4	0	Møbelsnedkeren i mig er virkelig glad! 🥳 	møbelsnedkeren-i-mig-er-virkelig-glad-2	t	f	/home-1/galleri-2/møbelsnedkeren-i-mig-er-virkelig-glad-2/		f		\N	\N	f	58	\N	f	2025-09-11 18:13:58.576824+02	2025-09-11 18:13:58.579281+02	25	2025-09-11 18:13:58.579281+02	Møbelsnedkeren i mig er virkelig glad! 🥳 	\N	\N	86f705af-96d5-4474-b0a9-064505430110	1	\N	25
13	0001000200030002	4	0	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗	nogen-gange-kan-man-spare-stilladset-det-kræver-bare-man-kan-lokke-nogen-til-at-sikre-den-anden-ende-af-det-reb-der-holder-dig	t	f	/home-1/galleri-2/nogen-gange-kan-man-spare-stilladset-det-kræver-bare-man-kan-lokke-nogen-til-at-sikre-den-anden-ende-af-det-reb-der-holder-dig/		f		\N	\N	f	58	\N	f	2025-09-11 18:11:15.729171+02	2025-09-11 18:11:15.734266+02	9	2025-09-11 18:11:15.734266+02	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗	\N	\N	0a8e680e-975b-4a33-8e8c-dd365d01cc81	1	\N	9
30	000100020003000J	4	0	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵	bevaringsværdige-vinduer-4-sæt-færdige-4-sæt-tilbage-2	t	f	/home-1/galleri-2/bevaringsværdige-vinduer-4-sæt-færdige-4-sæt-tilbage-2/		f		\N	\N	f	58	\N	f	2025-09-11 18:13:58.621082+02	2025-09-11 18:13:58.623116+02	26	2025-09-11 18:13:58.623116+02	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵	\N	\N	605da428-9e78-4227-9d48-9f76d3cd806b	1	\N	26
14	0001000200030003	4	0	Fugen skulle skiftes på disse døre. 	fugen-skulle-skiftes-på-disse-døre	t	f	/home-1/galleri-2/fugen-skulle-skiftes-på-disse-døre/		f		\N	\N	f	58	\N	f	2025-09-11 18:11:15.793913+02	2025-09-11 18:11:15.798174+02	10	2025-09-11 18:11:15.798174+02	Fugen skulle skiftes på disse døre. 	\N	\N	472b744d-7fde-482c-8bdf-633f80f5c515	1	\N	10
15	0001000200030004	4	0	Lærepladsen bliver også passet🦦	lærepladsen-bliver-også-passet	t	f	/home-1/galleri-2/lærepladsen-bliver-også-passet/		f		\N	\N	f	58	\N	f	2025-09-11 18:11:15.881307+02	2025-09-11 18:11:15.885386+02	11	2025-09-11 18:11:15.885386+02	Lærepladsen bliver også passet🦦	\N	\N	7414ddd0-e21d-4d7c-a06f-83547ffea0b2	1	\N	11
16	0001000200030005	4	0	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 	har-jeg-glemt-at-tage-et-før-billede-det-har-jeg-vist-nok-lige	t	f	/home-1/galleri-2/har-jeg-glemt-at-tage-et-før-billede-det-har-jeg-vist-nok-lige/		f		\N	\N	f	58	\N	f	2025-09-11 18:11:15.957311+02	2025-09-11 18:11:15.961722+02	12	2025-09-11 18:11:15.961722+02	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 	\N	\N	0b874f60-8116-4588-b54c-c0e3df2dfdcf	1	\N	12
17	0001000200030006	4	0	Møbelsnedkeren i mig er virkelig glad! 🥳 	møbelsnedkeren-i-mig-er-virkelig-glad	t	f	/home-1/galleri-2/møbelsnedkeren-i-mig-er-virkelig-glad/		f		\N	\N	f	58	\N	f	2025-09-11 18:11:16.007831+02	2025-09-11 18:11:16.011902+02	13	2025-09-11 18:11:16.011902+02	Møbelsnedkeren i mig er virkelig glad! 🥳 	\N	\N	a3f42928-f74e-44de-9de4-68668ee82f8b	1	\N	13
19	0001000200030008	4	0	Fundament/beton/whatever skjuler. 	fundamentbetonwhatever-skjuler	t	f	/home-1/galleri-2/fundamentbetonwhatever-skjuler/		f		\N	\N	f	58	\N	f	2025-09-11 18:13:58.67146+02	2025-09-11 18:11:16.127659+02	27	2025-09-11 18:13:58.676588+02	Fundament/beton/whatever skjuler. 	\N	\N	4b009bd0-e2ba-439c-8b10-e4253fbef55d	1	\N	27
18	0001000200030007	4	0	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵	bevaringsværdige-vinduer-4-sæt-færdige-4-sæt-tilbage	t	f	/home-1/galleri-2/bevaringsværdige-vinduer-4-sæt-færdige-4-sæt-tilbage/		f		\N	\N	f	58	\N	f	2025-09-11 18:11:16.061863+02	2025-09-11 18:11:16.066017+02	14	2025-09-11 18:11:16.066017+02	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵	\N	\N	b37a742c-5400-4a0e-9a5a-ae10a428d871	1	\N	14
31	000100020003000K	4	0	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!	havde-søde-tihizebra-med-ude-for-at-fikse-vinduer-samt-udvide-min-viden-om-linolie-og-linoliemaling-det-var-super-hyggeligt-2	t	f	/home-1/galleri-2/havde-søde-tihizebra-med-ude-for-at-fikse-vinduer-samt-udvide-min-viden-om-linolie-og-linoliemaling-det-var-super-hyggeligt-2/		f		\N	\N	f	58	\N	f	2025-09-11 18:13:58.723494+02	2025-09-11 18:13:58.726061+02	28	2025-09-11 18:13:58.726061+02	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!	\N	\N	ca32e560-306b-4d05-935e-dd0f508da631	1	\N	28
32	000100020003000L	4	0	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔	en-uheldig-undertags-gennemføring-eller-mangel-på-gennemføring-så-er-det-heldigt-at-det-kan-laves-korrekt-indefra-2	t	f	/home-1/galleri-2/en-uheldig-undertags-gennemføring-eller-mangel-på-gennemføring-så-er-det-heldigt-at-det-kan-laves-korrekt-indefra-2/		f		\N	\N	f	58	\N	f	2025-09-11 18:13:58.821925+02	2025-09-11 18:13:58.825825+02	29	2025-09-11 18:13:58.825825+02	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔	\N	\N	b9941157-b0a6-450d-8261-7fd1c866c0e4	1	\N	29
20	0001000200030009	4	0	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!	havde-søde-tihizebra-med-ude-for-at-fikse-vinduer-samt-udvide-min-viden-om-linolie-og-linoliemaling-det-var-super-hyggeligt	t	f	/home-1/galleri-2/havde-søde-tihizebra-med-ude-for-at-fikse-vinduer-samt-udvide-min-viden-om-linolie-og-linoliemaling-det-var-super-hyggeligt/		f		\N	\N	f	58	\N	f	2025-09-11 18:11:16.180067+02	2025-09-11 18:11:16.184176+02	16	2025-09-11 18:11:16.184176+02	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!	\N	\N	2260ddb6-041f-4269-b162-3fcb0d52b54e	1	\N	16
21	000100020003000A	4	0	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔	en-uheldig-undertags-gennemføring-eller-mangel-på-gennemføring-så-er-det-heldigt-at-det-kan-laves-korrekt-indefra	t	f	/home-1/galleri-2/en-uheldig-undertags-gennemføring-eller-mangel-på-gennemføring-så-er-det-heldigt-at-det-kan-laves-korrekt-indefra/		f		\N	\N	f	58	\N	f	2025-09-11 18:11:16.297376+02	2025-09-11 18:11:16.301625+02	17	2025-09-11 18:11:16.301625+02	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔	\N	\N	5131ad23-a85c-40b7-839f-ce00cacda23b	1	\N	17
22	000100020003000B	4	0	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸	udskiftning-af-punkteret-rude-dejligt-at-finde-et-lille-hul-i-det-ellers-meget-grå-vejr	t	f	/home-1/galleri-2/udskiftning-af-punkteret-rude-dejligt-at-finde-et-lille-hul-i-det-ellers-meget-grå-vejr/		f		\N	\N	f	58	\N	f	2025-09-11 18:11:16.351757+02	2025-09-11 18:11:16.355936+02	18	2025-09-11 18:11:16.355936+02	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸	\N	\N	d482a385-1bb2-46d5-b45f-d328e94d5fef	1	\N	18
11	000100020003	3	22	Galleri	galleri-2	t	f	/home-1/galleri-2/		f		\N	\N	f	51	\N	f	2025-09-11 18:11:15.398621+02	2025-09-11 18:11:15.40702+02	7	2025-09-11 18:11:15.40702+02	Galleri	\N	\N	30b3ba81-500c-4a39-8c66-7bdedbae6461	1	\N	7
33	000100020003000M	4	0	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸	udskiftning-af-punkteret-rude-dejligt-at-finde-et-lille-hul-i-det-ellers-meget-grå-vejr-2	t	f	/home-1/galleri-2/udskiftning-af-punkteret-rude-dejligt-at-finde-et-lille-hul-i-det-ellers-meget-grå-vejr-2/		f		\N	\N	f	58	\N	f	2025-09-11 18:13:58.907985+02	2025-09-11 18:13:58.913093+02	30	2025-09-11 18:13:58.913093+02	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸	\N	\N	9e71348c-b508-41c3-a02a-8d88cfd576be	1	\N	30
23	000100020003000C	4	0	En opgradering af TV alteret hos min kammerat🦔	en-opgradering-af-tv-alteret-hos-min-kammerat	t	f	/home-1/galleri-2/en-opgradering-af-tv-alteret-hos-min-kammerat/		f		\N	\N	f	58	\N	f	2025-09-11 18:13:58.977304+02	2025-09-11 18:11:16.419833+02	31	2025-09-11 18:13:58.984059+02	En opgradering af TV alteret hos min kammerat🦔	\N	\N	b9dbf9b6-bb5b-4e7a-966d-5acd8c768969	1	\N	31
\.


--
-- TOC entry 4644 (class 0 OID 26771)
-- Dependencies: 269
-- Data for Name: wagtailcore_pagelogentry; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pagelogentry (id, label, action, data, "timestamp", content_changed, deleted, content_type_id, page_id, revision_id, user_id, uuid) FROM stdin;
1	Velkommen til JCleemannByg	wagtail.create	{}	2025-09-11 15:45:14.488913+02	t	f	49	3	\N	\N	\N
2	Velkommen til JCleemannByg	wagtail.publish	{}	2025-09-11 15:45:14.549317+02	t	f	49	3	1	\N	\N
3	Projekt Galleri	wagtail.create	{}	2025-09-11 15:45:14.563705+02	t	f	51	4	\N	\N	\N
4	Projekt Galleri	wagtail.publish	{}	2025-09-11 15:45:14.61091+02	t	f	51	4	2	\N	\N
5	Kontakt Os	wagtail.create	{}	2025-09-11 15:45:14.625077+02	t	f	50	5	\N	\N	\N
6	Kontakt Os	wagtail.publish	{}	2025-09-11 15:45:14.674705+02	t	f	50	5	3	\N	\N
7	Velkommen til JCleemannByg	wagtail.publish	{}	2025-09-11 15:45:56.78316+02	t	f	49	3	4	\N	\N
8	Kontakt Os	wagtail.move	{"source": {"id": 1, "title": "Root"}, "destination": {"id": 3, "title": "Velkommen til JCleemannByg"}}	2025-09-11 15:50:51.283539+02	f	f	50	5	\N	\N	\N
9	Velkommen til JCleemannByg	wagtail.edit	{}	2025-09-11 15:59:35.656122+02	t	f	49	3	5	1	01f85d8e-4421-4543-8687-93b56c93b4ed
10	Velkommen til JCleemannByg	wagtail.edit	{}	2025-09-11 16:01:51.200614+02	t	f	49	3	6	1	5fe7e187-99b1-4cc1-9995-d77dc9f98bf4
11	Velkommen til JCleemannByg	wagtail.publish	{}	2025-09-11 16:01:51.236516+02	f	f	49	3	6	1	5fe7e187-99b1-4cc1-9995-d77dc9f98bf4
12	Træ terrasse og udendørs køkken	wagtail.create	{}	2025-09-11 16:24:01.469144+02	t	f	58	6	\N	\N	\N
13	Villa renovering i København	wagtail.create	{}	2025-09-11 16:24:01.52418+02	t	f	58	7	\N	\N	\N
14	Skræddersyet køkken installation	wagtail.create	{}	2025-09-11 16:24:01.55674+02	t	f	58	8	\N	\N	\N
15	Badeværelse renovering	wagtail.create	{}	2025-09-11 16:24:01.587236+02	t	f	58	9	\N	\N	\N
16	Moderne kontorbygning	wagtail.create	{}	2025-09-11 16:24:01.615489+02	t	f	58	10	\N	\N	\N
17	Projekt Galleri	wagtail.move	{"source": {"id": 1, "title": "Root"}, "destination": {"id": 3, "title": "Velkommen til JCleemannByg"}}	2025-09-11 16:24:44.518321+02	f	f	51	4	\N	\N	\N
18	Galleri	wagtail.create	{}	2025-09-11 18:11:15.389645+02	t	f	51	11	\N	\N	\N
19	Galleri	wagtail.publish	{}	2025-09-11 18:11:15.418835+02	t	f	51	11	7	\N	\N
20	Lille trin udført i jatoba	wagtail.create	{}	2025-09-11 18:11:15.429749+02	t	f	58	12	\N	\N	\N
21	Lille trin udført i jatoba	wagtail.publish	{}	2025-09-11 18:11:15.454528+02	t	f	58	12	8	\N	\N
22	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗	wagtail.create	{}	2025-09-11 18:11:15.723535+02	t	f	58	13	\N	\N	\N
23	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗	wagtail.publish	{}	2025-09-11 18:11:15.745638+02	t	f	58	13	9	\N	\N
24	Fugen skulle skiftes på disse døre. 	wagtail.create	{}	2025-09-11 18:11:15.788714+02	t	f	58	14	\N	\N	\N
25	Fugen skulle skiftes på disse døre. 	wagtail.publish	{}	2025-09-11 18:11:15.808952+02	t	f	58	14	10	\N	\N
26	Lærepladsen bliver også passet🦦	wagtail.create	{}	2025-09-11 18:11:15.875881+02	t	f	58	15	\N	\N	\N
27	Lærepladsen bliver også passet🦦	wagtail.publish	{}	2025-09-11 18:11:15.89611+02	t	f	58	15	11	\N	\N
28	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 	wagtail.create	{}	2025-09-11 18:11:15.952445+02	t	f	58	16	\N	\N	\N
29	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 	wagtail.publish	{}	2025-09-11 18:11:15.97211+02	t	f	58	16	12	\N	\N
30	Møbelsnedkeren i mig er virkelig glad! 🥳 	wagtail.create	{}	2025-09-11 18:11:16.002688+02	t	f	58	17	\N	\N	\N
31	Møbelsnedkeren i mig er virkelig glad! 🥳 	wagtail.publish	{}	2025-09-11 18:11:16.022371+02	t	f	58	17	13	\N	\N
32	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵	wagtail.create	{}	2025-09-11 18:11:16.057082+02	t	f	58	18	\N	\N	\N
33	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵	wagtail.publish	{}	2025-09-11 18:11:16.076152+02	t	f	58	18	14	\N	\N
34	Fundament/beton/whatever skjuler. 	wagtail.create	{}	2025-09-11 18:11:16.118493+02	t	f	58	19	\N	\N	\N
35	Fundament/beton/whatever skjuler. 	wagtail.publish	{}	2025-09-11 18:11:16.138301+02	t	f	58	19	15	\N	\N
36	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!	wagtail.create	{}	2025-09-11 18:11:16.175138+02	t	f	58	20	\N	\N	\N
37	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!	wagtail.publish	{}	2025-09-11 18:11:16.194433+02	t	f	58	20	16	\N	\N
38	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔	wagtail.create	{}	2025-09-11 18:11:16.292007+02	t	f	58	21	\N	\N	\N
39	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔	wagtail.publish	{}	2025-09-11 18:11:16.311723+02	t	f	58	21	17	\N	\N
40	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸	wagtail.create	{}	2025-09-11 18:11:16.346856+02	t	f	58	22	\N	\N	\N
41	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸	wagtail.publish	{}	2025-09-11 18:11:16.365919+02	t	f	58	22	18	\N	\N
42	En opgradering af TV alteret hos min kammerat🦔	wagtail.create	{}	2025-09-11 18:11:16.412265+02	t	f	58	23	\N	\N	\N
43	En opgradering af TV alteret hos min kammerat🦔	wagtail.publish	{}	2025-09-11 18:11:16.429477+02	t	f	58	23	19	\N	\N
44	Lille trin udført i jatoba	wagtail.create	{}	2025-09-11 18:13:58.252134+02	t	f	58	24	\N	\N	\N
45	Lille trin udført i jatoba	wagtail.publish	{}	2025-09-11 18:13:58.270749+02	t	f	58	24	20	\N	\N
46	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗	wagtail.create	{}	2025-09-11 18:13:58.307824+02	t	f	58	25	\N	\N	\N
47	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗	wagtail.publish	{}	2025-09-11 18:13:58.326582+02	t	f	58	25	21	\N	\N
48	Fugen skulle skiftes på disse døre. 	wagtail.create	{}	2025-09-11 18:13:58.363855+02	t	f	58	26	\N	\N	\N
49	Fugen skulle skiftes på disse døre. 	wagtail.publish	{}	2025-09-11 18:13:58.378167+02	t	f	58	26	22	\N	\N
50	Lærepladsen bliver også passet🦦	wagtail.create	{}	2025-09-11 18:13:58.44788+02	t	f	58	27	\N	\N	\N
51	Lærepladsen bliver også passet🦦	wagtail.publish	{}	2025-09-11 18:13:58.468282+02	t	f	58	27	23	\N	\N
52	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 	wagtail.create	{}	2025-09-11 18:13:58.525612+02	t	f	58	28	\N	\N	\N
53	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 	wagtail.publish	{}	2025-09-11 18:13:58.53957+02	t	f	58	28	24	\N	\N
54	Møbelsnedkeren i mig er virkelig glad! 🥳 	wagtail.create	{}	2025-09-11 18:13:58.567355+02	t	f	58	29	\N	\N	\N
55	Møbelsnedkeren i mig er virkelig glad! 🥳 	wagtail.publish	{}	2025-09-11 18:13:58.584838+02	t	f	58	29	25	\N	\N
56	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵	wagtail.create	{}	2025-09-11 18:13:58.615952+02	t	f	58	30	\N	\N	\N
57	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵	wagtail.publish	{}	2025-09-11 18:13:58.62838+02	t	f	58	30	26	\N	\N
58	Fundament/beton/whatever skjuler. 	wagtail.publish	{}	2025-09-11 18:13:58.683541+02	t	f	58	19	27	\N	\N
59	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!	wagtail.create	{}	2025-09-11 18:13:58.716997+02	t	f	58	31	\N	\N	\N
60	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!	wagtail.publish	{}	2025-09-11 18:13:58.732369+02	t	f	58	31	28	\N	\N
61	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔	wagtail.create	{}	2025-09-11 18:13:58.813295+02	t	f	58	32	\N	\N	\N
62	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔	wagtail.publish	{}	2025-09-11 18:13:58.834504+02	t	f	58	32	29	\N	\N
63	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸	wagtail.create	{}	2025-09-11 18:13:58.894887+02	t	f	58	33	\N	\N	\N
64	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸	wagtail.publish	{}	2025-09-11 18:13:58.921758+02	t	f	58	33	30	\N	\N
65	En opgradering af TV alteret hos min kammerat🦔	wagtail.publish	{}	2025-09-11 18:13:58.995106+02	t	f	58	23	31	\N	\N
\.


--
-- TOC entry 4652 (class 0 OID 26837)
-- Dependencies: 277
-- Data for Name: wagtailcore_pagesubscription; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pagesubscription (id, comment_notifications, page_id, user_id) FROM stdin;
1	f	3	1
\.


--
-- TOC entry 4614 (class 0 OID 26419)
-- Dependencies: 239
-- Data for Name: wagtailcore_pageviewrestriction; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pageviewrestriction (id, password, page_id, restriction_type) FROM stdin;
\.


--
-- TOC entry 4624 (class 0 OID 26547)
-- Dependencies: 249
-- Data for Name: wagtailcore_pageviewrestriction_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pageviewrestriction_groups (id, pageviewrestriction_id, group_id) FROM stdin;
\.


--
-- TOC entry 4656 (class 0 OID 27006)
-- Dependencies: 281
-- Data for Name: wagtailcore_referenceindex; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_referenceindex (id, object_id, to_object_id, model_path, content_path, content_path_hash, base_content_type_id, content_type_id, to_content_type_id) FROM stdin;
1	1	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
3	2	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
5	3	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
7	4	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
9	5	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
11	6	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
13	7	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
15	8	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
17	9	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
19	10	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
20	10	10	images.item.image	images.10.image	d0b160c2-0045-5a6d-b01f-2274ec307420	41	41	26
21	11	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
22	11	11	images.item.image	images.11.image	d879c17f-a9a2-5422-ba38-60e8e1a54ecf	41	41	26
23	12	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
24	12	12	images.item.image	images.12.image	d1b52978-a9ef-5ef8-8e2c-404890e9cfcf	41	41	26
25	13	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
26	13	13	images.item.image	images.13.image	63107060-1686-56a7-aed7-3b05c67d45cb	41	41	26
27	14	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
28	14	14	images.item.image	images.14.image	c9a4713e-9c60-5b66-8931-33896b5c8685	41	41	26
29	3	4	body.hero_v2.secondary_page	body.3475c607-30ae-48b8-bbd5-93b14c9218cb.secondary_page	c88541a7-0fd6-59ab-95e7-d371505ebebb	1	49	1
30	3	5	body.hero_v2.primary_page	body.3475c607-30ae-48b8-bbd5-93b14c9218cb.primary_page	ee82076a-62d6-5bcc-99ce-7f20a76ae718	1	49	1
31	3	4	body.featured_projects.all_projects_page	body.90037c54-259e-4132-8d90-128931be7ceb.all_projects_page	2c1ef3ad-825a-5542-91b1-97e24f28545a	1	49	1
32	6	10	project_images.item.image	project_images.1.image	98347e3f-e3fd-58dd-af92-52462b427b49	1	58	26
33	7	11	project_images.item.image	project_images.2.image	928c41ca-eec0-5121-a557-827a3f22993c	1	58	26
34	8	12	project_images.item.image	project_images.3.image	52c97588-106b-590f-800c-24d2854e8979	1	58	26
35	9	13	project_images.item.image	project_images.4.image	b7756211-c0b1-541e-8757-982783d11485	1	58	26
36	10	14	project_images.item.image	project_images.5.image	59612e61-feef-5ad6-a26e-d243c8447069	1	58	26
37	12	15	project_images.item.image	project_images.6.image	59dee3e3-991f-5b5b-9777-77e334c81857	1	58	26
38	15	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
39	13	16	project_images.item.image	project_images.7.image	94e3bb5d-00d3-5957-823c-ca8fffbf81c9	1	58	26
40	13	17	project_images.item.image	project_images.8.image	b98ce3f1-0200-5172-8f7e-6c091c01220d	1	58	26
41	16	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
42	17	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
43	14	18	project_images.item.image	project_images.9.image	e54a6321-60d4-54b9-a0db-bb0e7d92ed3b	1	58	26
44	14	19	project_images.item.image	project_images.10.image	0126fb59-c0e6-5488-a861-eec6e3b5e364	1	58	26
45	14	20	project_images.item.image	project_images.11.image	322b344f-9bb8-5125-928d-e269082bf7e2	1	58	26
46	14	21	project_images.item.image	project_images.12.image	79ea0536-c95c-5470-89ba-2dfb44354b9b	1	58	26
47	18	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
48	19	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
49	20	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
50	21	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
51	15	22	project_images.item.image	project_images.13.image	0dbecd85-5743-56a2-a43d-27a4fc2e09b6	1	58	26
52	15	24	project_images.item.image	project_images.15.image	ada891ef-4ef7-5bd4-9364-26d4d6cea857	1	58	26
53	15	23	project_images.item.image	project_images.14.image	bc251f84-4e15-5207-b300-344a87f9c223	1	58	26
54	22	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
55	23	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
56	24	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
57	16	26	project_images.item.image	project_images.17.image	79d33103-0b28-5627-b655-79ed278024f8	1	58	26
58	16	25	project_images.item.image	project_images.16.image	34dfca19-927e-568f-8484-6b958c2dc7ab	1	58	26
59	25	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
60	26	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
61	17	27	project_images.item.image	project_images.18.image	fc5e20a9-c695-58b6-a134-02310f429103	1	58	26
62	17	28	project_images.item.image	project_images.19.image	cedb235c-7974-5b38-8e8c-1d35f9227559	1	58	26
63	27	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
64	28	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
65	18	29	project_images.item.image	project_images.20.image	f07c92f7-d1ee-599d-b04e-6d8ec5d3264e	1	58	26
66	18	30	project_images.item.image	project_images.21.image	4f7a7e97-5d44-5032-99eb-5bc86bbbaef3	1	58	26
67	29	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
68	30	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
69	19	33	project_images.item.image	project_images.24.image	0e2c36b9-e57e-5299-ad3b-cb168262f105	1	58	26
70	19	31	project_images.item.image	project_images.22.image	2c1a47a5-2f52-5ba8-b7e6-987181e78870	1	58	26
71	19	32	project_images.item.image	project_images.23.image	5e5e29a7-051a-56b9-b2ab-3564585f1036	1	58	26
72	31	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
73	32	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
74	33	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
75	20	37	project_images.item.image	project_images.28.image	5640f831-f3f1-5aa7-81f7-d05b53b71b31	1	58	26
76	20	38	project_images.item.image	project_images.29.image	b13ac191-863e-53dc-9838-4f8098addbf5	1	58	26
77	20	35	project_images.item.image	project_images.26.image	860d0219-b1c6-5d5e-9d50-2bde5c5e824c	1	58	26
78	20	34	project_images.item.image	project_images.25.image	7dfa1eea-f4b6-51be-b754-794527298bf5	1	58	26
79	20	36	project_images.item.image	project_images.27.image	052b6952-af91-5eb5-a1fc-088c908fdfa0	1	58	26
80	34	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
81	35	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
82	36	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
83	37	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
84	38	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
85	21	40	project_images.item.image	project_images.31.image	2c437eb3-786b-5103-8907-4c60e8e0a10c	1	58	26
86	21	39	project_images.item.image	project_images.30.image	ce90154a-2ce7-5b34-80fd-8e3f88ec45eb	1	58	26
87	39	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
88	40	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
89	22	41	project_images.item.image	project_images.32.image	ed27fc2d-5c14-5c76-8b98-046b764de9b2	1	58	26
90	22	42	project_images.item.image	project_images.33.image	5a3f905b-e6a6-5600-bbb8-352fe63678ac	1	58	26
91	41	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
92	42	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
93	23	43	project_images.item.image	project_images.34.image	3e13807a-3403-5c25-a97b-4cec6bd851d6	1	58	26
94	23	44	project_images.item.image	project_images.35.image	3dc40c28-1770-5294-9e68-e23eab850588	1	58	26
95	43	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
96	44	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
97	24	45	project_images.item.image	project_images.36.image	aef49c1c-1348-5fe8-9fe7-aa33b1a307bb	1	58	26
98	45	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
99	25	46	project_images.item.image	project_images.37.image	c83d6677-ca74-53b0-8506-299d85101f13	1	58	26
100	25	47	project_images.item.image	project_images.38.image	573dd3c4-15b1-50e1-a7cf-63eb6b408019	1	58	26
101	46	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
102	47	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
103	26	49	project_images.item.image	project_images.40.image	55ae542d-2ffb-5b25-993b-4cae98b98c03	1	58	26
104	26	51	project_images.item.image	project_images.42.image	5ba5fd28-f351-5b79-ab0e-6fbe80c32fc9	1	58	26
105	26	50	project_images.item.image	project_images.41.image	d3964dc0-7bfb-5aec-880a-60c43ec9201f	1	58	26
106	26	48	project_images.item.image	project_images.39.image	7df58dda-24af-559f-8c39-0dad4a27206f	1	58	26
107	48	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
108	49	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
109	50	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
110	51	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
111	27	53	project_images.item.image	project_images.44.image	aec7af10-6575-5ee8-ad94-c93f58dbb9f1	1	58	26
112	27	52	project_images.item.image	project_images.43.image	44a3ca38-9010-528a-81f9-827277eddb79	1	58	26
113	27	54	project_images.item.image	project_images.45.image	c8c3e580-c47c-5fc7-b463-27b83785b33a	1	58	26
114	52	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
115	53	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
116	54	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
117	28	55	project_images.item.image	project_images.46.image	682c11a9-df34-592a-9b29-7b033a02da76	1	58	26
118	28	56	project_images.item.image	project_images.47.image	ce023164-f553-51ad-be44-524f27db559f	1	58	26
119	55	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
120	56	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
121	29	57	project_images.item.image	project_images.48.image	e2eab3ec-2b67-52ad-9357-4fc45ffeb7cf	1	58	26
122	29	58	project_images.item.image	project_images.49.image	a4d144da-f73e-5059-8a6b-9c6a13f17912	1	58	26
123	57	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
124	58	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
125	30	59	project_images.item.image	project_images.50.image	aa84cc3e-4b82-569e-a090-5a387a90b106	1	58	26
126	30	60	project_images.item.image	project_images.51.image	bb801e79-95f8-58ca-8477-e335df64d2c3	1	58	26
127	59	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
128	60	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
129	61	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
130	62	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
131	63	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
132	31	68	project_images.item.image	project_images.56.image	98d7f2db-79d4-5629-ba21-d96f04101293	1	58	26
133	31	65	project_images.item.image	project_images.53.image	9224daac-77c0-5242-8e49-adea3d29b9e3	1	58	26
134	31	67	project_images.item.image	project_images.55.image	6ba9e2e0-9eea-5fd1-8743-9ca9f717dbed	1	58	26
135	31	66	project_images.item.image	project_images.54.image	ebc7c322-d0af-5bf3-a9e1-f9a9f3c0c211	1	58	26
136	31	64	project_images.item.image	project_images.52.image	00d675a1-d0f0-5547-b18b-5e297c7dcd0e	1	58	26
137	64	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
138	65	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
139	66	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
140	67	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
141	68	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
142	32	69	project_images.item.image	project_images.57.image	0456b05c-9b88-5b31-ba6a-a0e5b8706e39	1	58	26
143	32	70	project_images.item.image	project_images.58.image	17b2a963-1b7a-55b9-a69a-4cb3140f3afe	1	58	26
144	69	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
145	70	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
146	33	72	project_images.item.image	project_images.60.image	007e881e-63f6-54f3-bafe-8d3c94ce24c2	1	58	26
147	33	71	project_images.item.image	project_images.59.image	da7f9911-135c-521a-8c5e-b0c19ed59f02	1	58	26
148	71	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
149	72	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
150	73	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
151	74	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
152	6	1	tagged_items.item.tag	tagged_items.1.tag	0a1d4af4-028a-541c-9ba8-bcfab5741d17	1	58	47
153	6	2	tagged_items.item.tag	tagged_items.2.tag	a9eb266d-9dd8-582f-a856-e7fe4b63349e	1	58	47
154	6	3	tagged_items.item.tag	tagged_items.3.tag	f661f16a-9d05-595f-abde-4c81bf50f724	1	58	47
155	6	4	tagged_items.item.tag	tagged_items.4.tag	29866ef1-63db-5c6e-bc0a-27ed379ad913	1	58	47
156	7	7	tagged_items.item.tag	tagged_items.7.tag	a4245cab-1223-5258-8e09-836cdc37835a	1	58	47
157	7	6	tagged_items.item.tag	tagged_items.6.tag	a5f5907a-6cc6-50d1-bdd7-41a35ef79ab0	1	58	47
158	7	8	tagged_items.item.tag	tagged_items.8.tag	cc756bbf-cf49-5f28-aed2-1244b0e04866	1	58	47
159	7	5	tagged_items.item.tag	tagged_items.5.tag	d680323b-4169-5aff-9d07-d41818c67436	1	58	47
160	8	3	tagged_items.item.tag	tagged_items.9.tag	6192591c-068e-5695-9ce2-96b9b1848275	1	58	47
161	8	9	tagged_items.item.tag	tagged_items.10.tag	9307753f-f405-523b-a62e-db17e076048a	1	58	47
162	8	10	tagged_items.item.tag	tagged_items.11.tag	55d5a30f-3e7f-5401-b8e4-cca376197cce	1	58	47
163	9	11	tagged_items.item.tag	tagged_items.12.tag	f20410c7-a795-5a86-a6ee-f72f2ba927e0	1	58	47
164	9	5	tagged_items.item.tag	tagged_items.13.tag	66d59944-fb9e-5553-9b4d-45ad8b1b11bf	1	58	47
165	9	12	tagged_items.item.tag	tagged_items.14.tag	4d274764-40ae-53d7-8a77-867edeb0fee3	1	58	47
166	10	15	tagged_items.item.tag	tagged_items.17.tag	eb103135-181c-5e1a-97e1-23b48d4d6bc7	1	58	47
167	10	16	tagged_items.item.tag	tagged_items.18.tag	1168b2b4-720e-5a16-bbf5-271d0bb7bfe4	1	58	47
168	10	14	tagged_items.item.tag	tagged_items.16.tag	2e447b0c-bf70-508c-b946-eed69a297109	1	58	47
169	10	13	tagged_items.item.tag	tagged_items.15.tag	8eff711f-e02b-5b2e-bbe8-e0fd9a55d76a	1	58	47
\.


--
-- TOC entry 4612 (class 0 OID 26411)
-- Dependencies: 237
-- Data for Name: wagtailcore_revision; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_revision (id, created_at, content, approved_go_live_at, object_id, user_id, content_type_id, base_content_type_id, object_str) FROM stdin;
1	2025-09-11 15:45:14.515774+02	{"pk": 3, "body": "[]", "live": true, "path": "00010002", "slug": "home-1", "depth": 2, "intro": "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>", "owner": null, "title": "Velkommen til JCleemannByg", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 0, "url_path": "/home-1/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Velkommen til JCleemannByg", "content_type": 49, "live_revision": null, "show_in_menus": false, "latest_revision": null, "translation_key": "3fc166df-3682-476a-ba86-e93c617785c0", "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	3	\N	49	1	Velkommen til JCleemannByg
2	2025-09-11 15:45:14.577423+02	{"pk": 4, "live": true, "path": "00010003", "slug": "galleri", "depth": 2, "intro": "<p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>", "owner": null, "title": "Projekt Galleri", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 0, "url_path": "/galleri/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Projekt Galleri", "content_type": 51, "live_revision": null, "show_in_menus": false, "latest_revision": null, "translation_key": "f18d5f96-a655-4c41-bc93-ba827d7e972d", "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	4	\N	51	1	Projekt Galleri
3	2025-09-11 15:45:14.640185+02	{"pk": 5, "live": true, "path": "00010004", "slug": "kontakt", "depth": 2, "intro": "<p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>", "owner": null, "title": "Kontakt Os", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 0, "url_path": "/kontakt/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Kontakt Os", "content_type": 50, "live_revision": null, "show_in_menus": false, "latest_revision": null, "translation_key": "1c559f5d-212e-44d6-893a-0163fe51b483", "last_published_at": null, "show_contact_form": true, "contact_form_intro": "<p>Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>", "contact_form_title": "Send os en besked", "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	5	\N	50	1	Kontakt Os
4	2025-09-11 15:45:56.742682+02	{"pk": 3, "body": "[]", "live": true, "path": "00010002", "slug": "home-1", "depth": 2, "intro": "<p>Professionelle bygge- og renoveringsløsninger med fokus på kvalitet og håndværk</p>", "owner": null, "title": "Velkommen til JCleemannByg", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 0, "url_path": "/home-1/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Velkommen til JCleemannByg", "content_type": 49, "live_revision": 1, "show_in_menus": false, "latest_revision": 1, "translation_key": "3fc166df-3682-476a-ba86-e93c617785c0", "last_published_at": "2025-09-11T13:45:14.529Z", "first_published_at": "2025-09-11T13:45:14.529Z", "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": "2025-09-11T13:45:14.515Z"}	\N	3	\N	49	1	Velkommen til JCleemannByg
5	2025-09-11 15:59:35.636113+02	{"pk": 3, "body": "[{\\"type\\": \\"hero_v2\\", \\"value\\": {\\"heading\\": \\"Professionelle byggel\\\\u00f8sninger i K\\\\u00f8benhavn og omegn\\", \\"subheading\\": \\"Fra k\\\\u00f8kkenrenovering til komplette nybyggerier - vi leverer h\\\\u00e5ndv\\\\u00e6rk af h\\\\u00f8jeste kvalitet med fokus p\\\\u00e5 kundetilfredshed og termintro fastholding.\\", \\"primary_text\\": \\"F\\\\u00e5 et uforpligtende tilbud\\", \\"primary_page\\": 5, \\"secondary_text\\": \\"Se vores projekter\\", \\"secondary_page\\": 4, \\"image\\": null, \\"style\\": {\\"background\\": \\"hero\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"3475c607-30ae-48b8-bbd5-93b14c9218cb\\"}, {\\"type\\": \\"trust_badges\\", \\"value\\": {\\"heading\\": \\"Derfor v\\\\u00e6lger kunder JCleemannByg\\", \\"items\\": [{\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"Kvalitet i hver detalje\\", \\"description\\": \\"Vi g\\\\u00e5r aldrig p\\\\u00e5 kompromis med kvaliteten. Alle materialer og h\\\\u00e5ndv\\\\u00e6rk lever op til de h\\\\u00f8jeste standarder.\\", \\"icon\\": \\"star\\"}, \\"id\\": \\"01c444da-75ef-4754-9251-081ae07a8dcd\\"}, {\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"Altid til tiden\\", \\"description\\": \\"Vi overholder altid vores deadlines og leverer projekter til tiden. Planl\\\\u00e6gning og p\\\\u00e5lidelighed er i h\\\\u00f8js\\\\u00e6det.\\", \\"icon\\": \\"clock\\"}, \\"id\\": \\"95a47f2f-fad0-4b0e-a08e-7ad574fee53d\\"}], \\"columns\\": \\"4\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"fb18f1d7-0f6c-4b13-8d42-38eef9aa72d9\\"}, {\\"type\\": \\"featured_projects\\", \\"value\\": {\\"heading\\": \\"Udvalgte projekter\\", \\"subheading\\": \\"Se eksempler p\\\\u00e5 vores seneste arbejde og f\\\\u00e5 inspiration til dit n\\\\u00e6ste projekt\\", \\"show_all_link\\": true, \\"all_projects_page\\": 4, \\"columns\\": \\"3\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"90037c54-259e-4132-8d90-128931be7ceb\\"}, {\\"type\\": \\"services_grid_inline\\", \\"value\\": {\\"heading\\": \\"Vores services\\", \\"items\\": [{\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"K\\\\u00f8kkenrenovering\\", \\"description\\": \\"Totalrenovering af k\\\\u00f8kkener med skr\\\\u00e6ddersyede l\\\\u00f8sninger, kvalitetsmaterialer og moderne design\\", \\"icon\\": \\"check\\"}, \\"id\\": \\"338dfc7d-5ee7-433d-927d-42d4d25005f1\\"}], \\"columns\\": \\"3\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"3d581778-17de-45f9-b911-fa5da29ca790\\"}]", "live": true, "path": "00010002", "slug": "home-1", "depth": 2, "intro": "<p data-block-key=\\"fichi\\">Professionelle bygge- og renoveringsløsninger med fokus på kvalitet og håndværk</p>", "owner": null, "title": "Velkommen til JCleemannByg", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 1, "url_path": "/home-1/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Velkommen til JCleemannByg", "content_type": 49, "live_revision": 4, "show_in_menus": false, "latest_revision": 4, "translation_key": "3fc166df-3682-476a-ba86-e93c617785c0", "last_published_at": "2025-09-11T13:45:56.761Z", "first_published_at": "2025-09-11T13:45:14.529Z", "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": "2025-09-11T13:45:56.742Z"}	\N	3	1	49	1	Velkommen til JCleemannByg
6	2025-09-11 16:01:51.176786+02	{"pk": 3, "body": "[{\\"type\\": \\"hero_v2\\", \\"value\\": {\\"heading\\": \\"Professionelle byggel\\\\u00f8sninger i K\\\\u00f8benhavn og omegn\\", \\"subheading\\": \\"Fra k\\\\u00f8kkenrenovering til komplette nybyggerier - vi leverer h\\\\u00e5ndv\\\\u00e6rk af h\\\\u00f8jeste kvalitet med fokus p\\\\u00e5 kundetilfredshed og termintro fastholding.\\", \\"primary_text\\": \\"F\\\\u00e5 et uforpligtende tilbud\\", \\"primary_page\\": 5, \\"secondary_text\\": \\"Se vores projekter\\", \\"secondary_page\\": 4, \\"image\\": null, \\"style\\": {\\"background\\": \\"hero\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"3475c607-30ae-48b8-bbd5-93b14c9218cb\\"}, {\\"type\\": \\"trust_badges\\", \\"value\\": {\\"heading\\": \\"Derfor v\\\\u00e6lger kunder JCleemannByg\\", \\"items\\": [{\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"Kvalitet i hver detalje\\", \\"description\\": \\"Vi g\\\\u00e5r aldrig p\\\\u00e5 kompromis med kvaliteten. Alle materialer og h\\\\u00e5ndv\\\\u00e6rk lever op til de h\\\\u00f8jeste standarder.\\", \\"icon\\": \\"star\\"}, \\"id\\": \\"01c444da-75ef-4754-9251-081ae07a8dcd\\"}, {\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"Altid til tiden\\", \\"description\\": \\"Vi overholder altid vores deadlines og leverer projekter til tiden. Planl\\\\u00e6gning og p\\\\u00e5lidelighed er i h\\\\u00f8js\\\\u00e6det.\\", \\"icon\\": \\"clock\\"}, \\"id\\": \\"95a47f2f-fad0-4b0e-a08e-7ad574fee53d\\"}], \\"columns\\": \\"4\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"fb18f1d7-0f6c-4b13-8d42-38eef9aa72d9\\"}, {\\"type\\": \\"featured_projects\\", \\"value\\": {\\"heading\\": \\"Udvalgte projekter\\", \\"subheading\\": \\"Se eksempler p\\\\u00e5 vores seneste arbejde og f\\\\u00e5 inspiration til dit n\\\\u00e6ste projekt\\", \\"show_all_link\\": true, \\"all_projects_page\\": 4, \\"columns\\": \\"3\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"90037c54-259e-4132-8d90-128931be7ceb\\"}, {\\"type\\": \\"services_grid_inline\\", \\"value\\": {\\"heading\\": \\"Vores services\\", \\"items\\": [{\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"K\\\\u00f8kkenrenovering\\", \\"description\\": \\"Totalrenovering af k\\\\u00f8kkener med skr\\\\u00e6ddersyede l\\\\u00f8sninger, kvalitetsmaterialer og moderne design\\", \\"icon\\": \\"check\\"}, \\"id\\": \\"338dfc7d-5ee7-433d-927d-42d4d25005f1\\"}], \\"columns\\": \\"3\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"3d581778-17de-45f9-b911-fa5da29ca790\\"}]", "live": true, "path": "00010002", "slug": "home-1", "depth": 2, "intro": "<p data-block-key=\\"fichi\\">Professionelle bygge- og renoveringsløsninger med fokus på kvalitet og håndværk</p>", "owner": null, "title": "Velkommen til JCleemannByg", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 1, "url_path": "/home-1/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Velkommen til JCleemannByg", "content_type": 49, "live_revision": 4, "show_in_menus": false, "latest_revision": 5, "translation_key": "3fc166df-3682-476a-ba86-e93c617785c0", "last_published_at": "2025-09-11T13:45:56.761Z", "first_published_at": "2025-09-11T13:45:14.529Z", "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": true, "latest_revision_created_at": "2025-09-11T13:59:35.636Z"}	\N	3	1	49	1	Velkommen til JCleemannByg
7	2025-09-11 18:11:15.398621+02	{"pk": 11, "live": true, "path": "000100020003", "slug": "galleri-2", "depth": 3, "intro": "", "owner": null, "title": "Galleri", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 0, "url_path": "/home-1/galleri-2/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Galleri", "content_type": 51, "live_revision": null, "show_in_menus": false, "latest_revision": null, "translation_key": "30b3ba81-500c-4a39-8c66-7bdedbae6461", "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	11	\N	51	1	Galleri
8	2025-09-11 18:11:15.437926+02	{"pk": 12, "live": true, "path": "0001000200030001", "slug": "lille-trin-udført-i-jatoba", "depth": 4, "owner": null, "title": "Lille trin udført i jatoba", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/lille-trin-udført-i-jatoba/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "Lille trin udført i jatoba", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "7808fd2a-0673-49e5-8320-8e55c192d7f3", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	12	\N	58	1	Lille trin udført i jatoba
9	2025-09-11 18:11:15.729171+02	{"pk": 13, "live": true, "path": "0001000200030002", "slug": "nogen-gange-kan-man-spare-stilladset-det-kræver-bare-man-kan-lokke-nogen-til-at-sikre-den-anden-ende-af-det-reb-der-holder-dig", "depth": 4, "owner": null, "title": "Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/nogen-gange-kan-man-spare-stilladset-det-kræver-bare-man-kan-lokke-nogen-til-at-sikre-den-anden-ende-af-det-reb-der-holder-dig/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "0a8e680e-975b-4a33-8e8c-dd365d01cc81", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	13	\N	58	1	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗
10	2025-09-11 18:11:15.793913+02	{"pk": 14, "live": true, "path": "0001000200030003", "slug": "fugen-skulle-skiftes-på-disse-døre", "depth": 4, "owner": null, "title": "Fugen skulle skiftes på disse døre. ", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/fugen-skulle-skiftes-på-disse-døre/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "Fugen skulle skiftes på disse døre. ", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "472b744d-7fde-482c-8bdf-633f80f5c515", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	14	\N	58	1	Fugen skulle skiftes på disse døre. 
11	2025-09-11 18:11:15.881307+02	{"pk": 15, "live": true, "path": "0001000200030004", "slug": "lærepladsen-bliver-også-passet", "depth": 4, "owner": null, "title": "Lærepladsen bliver også passet🦦", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/lærepladsen-bliver-også-passet/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "Lærepladsen bliver også passet🦦", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "7414ddd0-e21d-4d7c-a06f-83547ffea0b2", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	15	\N	58	1	Lærepladsen bliver også passet🦦
12	2025-09-11 18:11:15.957311+02	{"pk": 16, "live": true, "path": "0001000200030005", "slug": "har-jeg-glemt-at-tage-et-før-billede-det-har-jeg-vist-nok-lige", "depth": 4, "owner": null, "title": "Har jeg glemt at tage et før billede? Det har jeg vist nok lige. ", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/har-jeg-glemt-at-tage-et-før-billede-det-har-jeg-vist-nok-lige/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "Har jeg glemt at tage et før billede? Det har jeg vist nok lige. ", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "0b874f60-8116-4588-b54c-c0e3df2dfdcf", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	16	\N	58	1	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 
13	2025-09-11 18:11:16.007831+02	{"pk": 17, "live": true, "path": "0001000200030006", "slug": "møbelsnedkeren-i-mig-er-virkelig-glad", "depth": 4, "owner": null, "title": "Møbelsnedkeren i mig er virkelig glad! 🥳 ", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/møbelsnedkeren-i-mig-er-virkelig-glad/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "Møbelsnedkeren i mig er virkelig glad! 🥳 ", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "a3f42928-f74e-44de-9de4-68668ee82f8b", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	17	\N	58	1	Møbelsnedkeren i mig er virkelig glad! 🥳 
14	2025-09-11 18:11:16.061863+02	{"pk": 18, "live": true, "path": "0001000200030007", "slug": "bevaringsværdige-vinduer-4-sæt-færdige-4-sæt-tilbage", "depth": 4, "owner": null, "title": "Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/bevaringsværdige-vinduer-4-sæt-færdige-4-sæt-tilbage/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "b37a742c-5400-4a0e-9a5a-ae10a428d871", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	18	\N	58	1	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵
16	2025-09-11 18:11:16.180067+02	{"pk": 20, "live": true, "path": "0001000200030009", "slug": "havde-søde-tihizebra-med-ude-for-at-fikse-vinduer-samt-udvide-min-viden-om-linolie-og-linoliemaling-det-var-super-hyggeligt", "depth": 4, "owner": null, "title": "Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/havde-søde-tihizebra-med-ude-for-at-fikse-vinduer-samt-udvide-min-viden-om-linolie-og-linoliemaling-det-var-super-hyggeligt/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "2260ddb6-041f-4269-b162-3fcb0d52b54e", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	20	\N	58	1	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!
17	2025-09-11 18:11:16.297376+02	{"pk": 21, "live": true, "path": "000100020003000A", "slug": "en-uheldig-undertags-gennemføring-eller-mangel-på-gennemføring-så-er-det-heldigt-at-det-kan-laves-korrekt-indefra", "depth": 4, "owner": null, "title": "En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/en-uheldig-undertags-gennemføring-eller-mangel-på-gennemføring-så-er-det-heldigt-at-det-kan-laves-korrekt-indefra/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "5131ad23-a85c-40b7-839f-ce00cacda23b", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	21	\N	58	1	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔
15	2025-09-11 18:11:16.123405+02	{"pk": 19, "live": true, "path": "0001000200030008", "slug": "fundamentbetonwhatever-skjuler", "depth": 4, "owner": null, "title": "Fundament/beton/whatever skjuler. ", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/fundamentbetonwhatever-skjuler/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "Fundament/beton/whatever skjuler. ", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "4b009bd0-e2ba-439c-8b10-e4253fbef55d", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	19	\N	58	1	Fundament/beton/whatever skjuler. 
18	2025-09-11 18:11:16.351757+02	{"pk": 22, "live": true, "path": "000100020003000B", "slug": "udskiftning-af-punkteret-rude-dejligt-at-finde-et-lille-hul-i-det-ellers-meget-grå-vejr", "depth": 4, "owner": null, "title": "Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/udskiftning-af-punkteret-rude-dejligt-at-finde-et-lille-hul-i-det-ellers-meget-grå-vejr/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "d482a385-1bb2-46d5-b45f-d328e94d5fef", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	22	\N	58	1	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸
20	2025-09-11 18:13:58.260847+02	{"pk": 24, "live": true, "path": "000100020003000D", "slug": "lille-trin-udført-i-jatoba-2", "depth": 4, "owner": null, "title": "Lille trin udført i jatoba", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/lille-trin-udført-i-jatoba-2/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "Lille trin udført i jatoba", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "2deacdfa-7c0c-4c16-8ea7-0a9f3e863413", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	24	\N	58	1	Lille trin udført i jatoba
21	2025-09-11 18:13:58.317675+02	{"pk": 25, "live": true, "path": "000100020003000E", "slug": "nogen-gange-kan-man-spare-stilladset-det-kræver-bare-man-kan-lokke-nogen-til-at-sikre-den-anden-ende-af-det-reb-der-holder-dig-2", "depth": 4, "owner": null, "title": "Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/nogen-gange-kan-man-spare-stilladset-det-kræver-bare-man-kan-lokke-nogen-til-at-sikre-den-anden-ende-af-det-reb-der-holder-dig-2/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "b25769e5-8b2e-4951-beae-2e456922bcca", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	25	\N	58	1	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗
22	2025-09-11 18:13:58.370132+02	{"pk": 26, "live": true, "path": "000100020003000F", "slug": "fugen-skulle-skiftes-på-disse-døre-2", "depth": 4, "owner": null, "title": "Fugen skulle skiftes på disse døre. ", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/fugen-skulle-skiftes-på-disse-døre-2/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "Perfekt tidspunkt at få fjernet råd og lavet en lus! 🦔\\n#tømrer", "draft_title": "Fugen skulle skiftes på disse døre. ", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "4ad408f2-6cfc-4455-8cad-e2f92c4c4c4c", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	26	\N	58	1	Fugen skulle skiftes på disse døre. 
23	2025-09-11 18:13:58.453697+02	{"pk": 27, "live": true, "path": "000100020003000G", "slug": "lærepladsen-bliver-også-passet-2", "depth": 4, "owner": null, "title": "Lærepladsen bliver også passet🦦", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/lærepladsen-bliver-også-passet-2/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "Trods byger og blæst har vi fået lavet undertag, kvist og nyt solstrålerne!😎🌞\\nNu en lang weekend til mig!🍺", "draft_title": "Lærepladsen bliver også passet🦦", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "3f41bf6f-190c-4646-89ee-c91c98f7e382", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	27	\N	58	1	Lærepladsen bliver også passet🦦
19	2025-09-11 18:11:16.41579+02	{"pk": 23, "live": true, "path": "000100020003000C", "slug": "en-opgradering-af-tv-alteret-hos-min-kammerat", "depth": 4, "owner": null, "title": "En opgradering af TV alteret hos min kammerat🦔", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/en-opgradering-af-tv-alteret-hos-min-kammerat/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "En opgradering af TV alteret hos min kammerat🦔", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "b9dbf9b6-bb5b-4e7a-966d-5acd8c768969", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	23	\N	58	1	En opgradering af TV alteret hos min kammerat🦔
24	2025-09-11 18:13:58.531466+02	{"pk": 28, "live": true, "path": "000100020003000H", "slug": "har-jeg-glemt-at-tage-et-før-billede-det-har-jeg-vist-nok-lige-2", "depth": 4, "owner": null, "title": "Har jeg glemt at tage et før billede? Det har jeg vist nok lige. ", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/har-jeg-glemt-at-tage-et-før-billede-det-har-jeg-vist-nok-lige-2/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "Men ruden var knust, det er den ikke længere. Det er en succes i min bog 🐳\\nGod dag derude", "draft_title": "Har jeg glemt at tage et før billede? Det har jeg vist nok lige. ", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "b590cb22-e762-4d39-9bbd-3aa0b942bfd5", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	28	\N	58	1	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 
25	2025-09-11 18:13:58.576824+02	{"pk": 29, "live": true, "path": "000100020003000I", "slug": "møbelsnedkeren-i-mig-er-virkelig-glad-2", "depth": 4, "owner": null, "title": "Møbelsnedkeren i mig er virkelig glad! 🥳 ", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/møbelsnedkeren-i-mig-er-virkelig-glad-2/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "Mit første møbel er et simpelt sofabord til min egen stue, det næste bliver at give sig i kast med to runde linoleumsborde🌚", "draft_title": "Møbelsnedkeren i mig er virkelig glad! 🥳 ", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "86f705af-96d5-4474-b0a9-064505430110", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	29	\N	58	1	Møbelsnedkeren i mig er virkelig glad! 🥳 
26	2025-09-11 18:13:58.621082+02	{"pk": 30, "live": true, "path": "000100020003000J", "slug": "bevaringsværdige-vinduer-4-sæt-færdige-4-sæt-tilbage-2", "depth": 4, "owner": null, "title": "Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/bevaringsværdige-vinduer-4-sæt-færdige-4-sæt-tilbage-2/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "Behandlet med linolie og linoliemaling.🖌️", "draft_title": "Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "605da428-9e78-4227-9d48-9f76d3cd806b", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	30	\N	58	1	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵
27	2025-09-11 18:13:58.67146+02	{"pk": 19, "live": true, "path": "0001000200030008", "slug": "fundamentbetonwhatever-skjuler", "depth": 4, "owner": null, "title": "Fundament/beton/whatever skjuler. ", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/fundamentbetonwhatever-skjuler/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "Dejligt at kunne være semi indenfor nu efteråret for alvor er sat ind 🍁🦔", "draft_title": "Fundament/beton/whatever skjuler. ", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": 15, "show_in_menus": false, "project_images": [{"pk": 22, "image": 31, "caption": "", "alt_text": "", "sort_order": null, "project_page": 19}, {"pk": 23, "image": 32, "caption": "", "alt_text": "", "sort_order": null, "project_page": 19}, {"pk": 24, "image": 33, "caption": "", "alt_text": "", "sort_order": null, "project_page": 19}], "project_status": "planning", "latest_revision": 15, "translation_key": "4b009bd0-e2ba-439c-8b10-e4253fbef55d", "estimated_budget": null, "last_published_at": "2025-09-11T16:11:16.127Z", "first_published_at": "2025-09-11T16:11:16.127Z", "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": "2025-09-11T16:11:16.123Z"}	\N	19	\N	58	1	Fundament/beton/whatever skjuler. 
28	2025-09-11 18:13:58.723494+02	{"pk": 31, "live": true, "path": "000100020003000K", "slug": "havde-søde-tihizebra-med-ude-for-at-fikse-vinduer-samt-udvide-min-viden-om-linolie-og-linoliemaling-det-var-super-hyggeligt-2", "depth": 4, "owner": null, "title": "Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/havde-søde-tihizebra-med-ude-for-at-fikse-vinduer-samt-udvide-min-viden-om-linolie-og-linoliemaling-det-var-super-hyggeligt-2/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "ca32e560-306b-4d05-935e-dd0f508da631", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	31	\N	58	1	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!
29	2025-09-11 18:13:58.821925+02	{"pk": 32, "live": true, "path": "000100020003000L", "slug": "en-uheldig-undertags-gennemføring-eller-mangel-på-gennemføring-så-er-det-heldigt-at-det-kan-laves-korrekt-indefra-2", "depth": 4, "owner": null, "title": "En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/en-uheldig-undertags-gennemføring-eller-mangel-på-gennemføring-så-er-det-heldigt-at-det-kan-laves-korrekt-indefra-2/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "Så kommer der ikke vand ind der længere 🥸", "draft_title": "En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "b9941157-b0a6-450d-8261-7fd1c866c0e4", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	32	\N	58	1	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔
30	2025-09-11 18:13:58.907985+02	{"pk": 33, "live": true, "path": "000100020003000M", "slug": "udskiftning-af-punkteret-rude-dejligt-at-finde-et-lille-hul-i-det-ellers-meget-grå-vejr-2", "depth": 4, "owner": null, "title": "Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/udskiftning-af-punkteret-rude-dejligt-at-finde-et-lille-hul-i-det-ellers-meget-grå-vejr-2/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "", "draft_title": "Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": null, "show_in_menus": false, "project_images": [], "project_status": "planning", "latest_revision": null, "translation_key": "9e71348c-b508-41c3-a02a-8d88cfd576be", "estimated_budget": null, "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	33	\N	58	1	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸
31	2025-09-11 18:13:58.977304+02	{"pk": 23, "live": true, "path": "000100020003000C", "slug": "en-opgradering-af-tv-alteret-hos-min-kammerat", "depth": 4, "owner": null, "title": "En opgradering af TV alteret hos min kammerat🦔", "locale": 1, "locked": false, "expired": false, "alias_of": null, "featured": false, "location": "", "numchild": 0, "priority": "medium", "url_path": "/home-1/galleri-2/en-opgradering-af-tv-alteret-hos-min-kammerat/", "expire_at": null, "locked_at": null, "locked_by": null, "materials": "", "seo_title": "", "collection": null, "go_live_at": null, "client_name": "", "description": "Efter og før", "draft_title": "En opgradering af TV alteret hos min kammerat🦔", "content_type": 58, "project_date": null, "tagged_items": [], "live_revision": 19, "show_in_menus": false, "project_images": [{"pk": 34, "image": 43, "caption": "", "alt_text": "", "sort_order": null, "project_page": 23}, {"pk": 35, "image": 44, "caption": "", "alt_text": "", "sort_order": null, "project_page": 23}], "project_status": "planning", "latest_revision": 19, "translation_key": "b9dbf9b6-bb5b-4e7a-966d-5acd8c768969", "estimated_budget": null, "last_published_at": "2025-09-11T16:11:16.419Z", "first_published_at": "2025-09-11T16:11:16.419Z", "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": "2025-09-11T16:11:16.415Z"}	\N	23	\N	58	1	En opgradering af TV alteret hos min kammerat🦔
\.


--
-- TOC entry 4616 (class 0 OID 26425)
-- Dependencies: 241
-- Data for Name: wagtailcore_site; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_site (id, hostname, port, is_default_site, root_page_id, site_name) FROM stdin;
1	localhost	80	t	3	
\.


--
-- TOC entry 4630 (class 0 OID 26615)
-- Dependencies: 255
-- Data for Name: wagtailcore_task; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_task (id, name, active, content_type_id) FROM stdin;
1	Moderators approval	t	2
\.


--
-- TOC entry 4632 (class 0 OID 26621)
-- Dependencies: 257
-- Data for Name: wagtailcore_taskstate; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_taskstate (id, status, started_at, finished_at, content_type_id, revision_id, task_id, workflow_state_id, finished_by_id, comment) FROM stdin;
\.


--
-- TOC entry 4659 (class 0 OID 27103)
-- Dependencies: 284
-- Data for Name: wagtailcore_uploadedfile; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_uploadedfile (id, file, for_content_type_id, uploaded_by_user_id) FROM stdin;
\.


--
-- TOC entry 4634 (class 0 OID 26627)
-- Dependencies: 259
-- Data for Name: wagtailcore_workflow; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflow (id, name, active) FROM stdin;
1	Moderators approval	t
\.


--
-- TOC entry 4657 (class 0 OID 27070)
-- Dependencies: 282
-- Data for Name: wagtailcore_workflowcontenttype; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflowcontenttype (content_type_id, workflow_id) FROM stdin;
\.


--
-- TOC entry 4638 (class 0 OID 26645)
-- Dependencies: 263
-- Data for Name: wagtailcore_workflowpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflowpage (page_id, workflow_id) FROM stdin;
1	1
\.


--
-- TOC entry 4637 (class 0 OID 26638)
-- Dependencies: 262
-- Data for Name: wagtailcore_workflowstate; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflowstate (id, status, created_at, current_task_state_id, object_id, requested_by_id, workflow_id, content_type_id, base_content_type_id) FROM stdin;
\.


--
-- TOC entry 4640 (class 0 OID 26656)
-- Dependencies: 265
-- Data for Name: wagtailcore_workflowtask; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflowtask (id, sort_order, task_id, workflow_id) FROM stdin;
1	0	1	1
\.


--
-- TOC entry 4696 (class 0 OID 27474)
-- Dependencies: 321
-- Data for Name: wagtaildocs_document; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtaildocs_document (id, title, file, created_at, uploaded_by_user_id, collection_id, file_size, file_hash) FROM stdin;
\.


--
-- TOC entry 4698 (class 0 OID 27514)
-- Dependencies: 323
-- Data for Name: wagtailembeds_embed; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailembeds_embed (id, url, max_width, type, html, title, author_name, provider_name, thumbnail_url, width, height, last_updated, hash, cache_until) FROM stdin;
\.


--
-- TOC entry 4700 (class 0 OID 27530)
-- Dependencies: 325
-- Data for Name: wagtailforms_formsubmission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailforms_formsubmission (id, form_data, submit_time, page_id) FROM stdin;
\.


--
-- TOC entry 4667 (class 0 OID 27178)
-- Dependencies: 292
-- Data for Name: wagtailimages_image; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailimages_image (id, title, file, width, height, created_at, focal_point_x, focal_point_y, focal_point_width, focal_point_height, uploaded_by_user_id, file_size, collection_id, file_hash, description) FROM stdin;
1	Stock billede stock-image-1	original_images/stock-image-1_0A2NUWQ.jpg	800	600	2025-09-11 15:45:14.692991+02	\N	\N	\N	\N	\N	\N	1		
2	Stock billede stock-image-2	original_images/stock-image-2_FnfE1HR.jpg	600	800	2025-09-11 15:45:14.733636+02	\N	\N	\N	\N	\N	\N	1		
3	Stock billede stock-image-3	original_images/stock-image-3_3qmAojx.jpg	1200	400	2025-09-11 15:45:14.763981+02	\N	\N	\N	\N	\N	\N	1		
4	Stock billede stock-image-4	original_images/stock-image-4_EsykVBU.jpg	900	600	2025-09-11 15:45:14.792573+02	\N	\N	\N	\N	\N	\N	1		
5	Træ terrasse og udendørs køkken - Projekt billede	original_images/live-project-1_iyzcC0q.jpg	800	600	2025-09-11 15:45:21.196383+02	\N	\N	\N	\N	\N	\N	1		
6	Villa renovering i København - Projekt billede	original_images/live-project-2_ejBqhTh.jpg	800	600	2025-09-11 15:45:21.234743+02	\N	\N	\N	\N	\N	\N	1		
7	Skræddersyet køkken installation - Projekt billede	original_images/live-project-3_Ggpn4bp.jpg	800	600	2025-09-11 15:45:21.260764+02	\N	\N	\N	\N	\N	\N	1		
8	Badeværelse renovering - Projekt billede	original_images/live-project-4_LVh7JDF.jpg	800	600	2025-09-11 15:45:21.288901+02	\N	\N	\N	\N	\N	\N	1		
9	Moderne kontorbygning - Projekt billede	original_images/live-project-5_S0Y1mdY.jpg	800	600	2025-09-11 15:45:21.315703+02	\N	\N	\N	\N	\N	\N	1		
10	Træ terrasse og udendørs køkken - Projekt billede	original_images/live-project-1_QLyVan7.jpg	800	600	2025-09-11 15:45:56.796864+02	\N	\N	\N	\N	\N	\N	1		
11	Villa renovering i København - Projekt billede	original_images/live-project-2_rQ4CJhe.jpg	800	600	2025-09-11 15:45:56.832212+02	\N	\N	\N	\N	\N	\N	1		
12	Skræddersyet køkken installation - Projekt billede	original_images/live-project-3_uCenhLA.jpg	800	600	2025-09-11 15:45:56.861074+02	\N	\N	\N	\N	\N	\N	1		
13	Badeværelse renovering - Projekt billede	original_images/live-project-4_eRFcsUN.jpg	800	600	2025-09-11 15:45:56.888252+02	\N	\N	\N	\N	\N	\N	1		
14	Moderne kontorbygning - Projekt billede	original_images/live-project-5_Nx6pxPJ.jpg	800	600	2025-09-11 15:45:56.91837+02	\N	\N	\N	\N	\N	\N	1		
15	2024-08-09_16-50-48_UTC_C-dN1qANwwt	original_images/2024-08-09_16-50-48_UTC_C-dN1qANwwt.jpg	1839	1839	2025-09-11 18:11:15.711383+02	\N	\N	\N	\N	\N	\N	1		
16	2024-08-10_14-17-46_UTC_C-fhHqFNKWI_1	original_images/2024-08-10_14-17-46_UTC_C-fhHqFNKWI_1.jpg	1440	1800	2025-09-11 18:11:15.76509+02	\N	\N	\N	\N	\N	\N	1		
17	2024-08-10_14-17-46_UTC_C-fhHqFNKWI_2	original_images/2024-08-10_14-17-46_UTC_C-fhHqFNKWI_2.jpg	1440	1800	2025-09-11 18:11:15.779164+02	\N	\N	\N	\N	\N	\N	1		
18	2024-08-13_17-25-18_UTC_C-nk927N_qi_1	original_images/2024-08-13_17-25-18_UTC_C-nk927N_qi_1.jpg	1440	1440	2025-09-11 18:11:15.823916+02	\N	\N	\N	\N	\N	\N	1		
19	2024-08-13_17-25-18_UTC_C-nk927N_qi_2	original_images/2024-08-13_17-25-18_UTC_C-nk927N_qi_2.jpg	1440	1440	2025-09-11 18:11:15.838269+02	\N	\N	\N	\N	\N	\N	1		
20	2024-08-13_17-25-18_UTC_C-nk927N_qi_3	original_images/2024-08-13_17-25-18_UTC_C-nk927N_qi_3.jpg	1440	1440	2025-09-11 18:11:15.853504+02	\N	\N	\N	\N	\N	\N	1		
21	2024-08-13_17-25-18_UTC_C-nk927N_qi_4	original_images/2024-08-13_17-25-18_UTC_C-nk927N_qi_4.jpg	1440	1440	2025-09-11 18:11:15.866539+02	\N	\N	\N	\N	\N	\N	1		
22	2024-08-22_15-01-07_UTC_C--fnqvINx0_1	original_images/2024-08-22_15-01-07_UTC_C--fnqvINx0_1.jpg	1440	1800	2025-09-11 18:11:15.911021+02	\N	\N	\N	\N	\N	\N	1		
23	2024-08-22_15-01-07_UTC_C--fnqvINx0_2	original_images/2024-08-22_15-01-07_UTC_C--fnqvINx0_2.jpg	1440	1800	2025-09-11 18:11:15.927379+02	\N	\N	\N	\N	\N	\N	1		
24	2024-08-22_15-01-07_UTC_C--fnqvINx0_3	original_images/2024-08-22_15-01-07_UTC_C--fnqvINx0_3.jpg	1440	1800	2025-09-11 18:11:15.944053+02	\N	\N	\N	\N	\N	\N	1		
25	2024-09-03_14-13-17_UTC_C_dTrzno1AU_1	original_images/2024-09-03_14-13-17_UTC_C_dTrzno1AU_1.jpg	1440	1800	2025-09-11 18:11:15.983222+02	\N	\N	\N	\N	\N	\N	1		
26	2024-09-03_14-13-17_UTC_C_dTrzno1AU_2	original_images/2024-09-03_14-13-17_UTC_C_dTrzno1AU_2.jpg	1440	1800	2025-09-11 18:11:15.993763+02	\N	\N	\N	\N	\N	\N	1		
27	2024-09-04_14-37-08_UTC_C_f7NXgITY1_1	original_images/2024-09-04_14-37-08_UTC_C_f7NXgITY1_1.jpg	1440	1799	2025-09-11 18:11:16.033469+02	\N	\N	\N	\N	\N	\N	1		
28	2024-09-04_14-37-08_UTC_C_f7NXgITY1_2	original_images/2024-09-04_14-37-08_UTC_C_f7NXgITY1_2.jpg	1440	1800	2025-09-11 18:11:16.048124+02	\N	\N	\N	\N	\N	\N	1		
29	2024-10-01_16-48-29_UTC_DAlrtEQoLJm_1	original_images/2024-10-01_16-48-29_UTC_DAlrtEQoLJm_1.jpg	1440	1800	2025-09-11 18:11:16.091289+02	\N	\N	\N	\N	\N	\N	1		
30	2024-10-01_16-48-29_UTC_DAlrtEQoLJm_2	original_images/2024-10-01_16-48-29_UTC_DAlrtEQoLJm_2.jpg	1440	1800	2025-09-11 18:11:16.109882+02	\N	\N	\N	\N	\N	\N	1		
31	2024-10-16_14-52-52_UTC_DBMGZUBIB-7_1	original_images/2024-10-16_14-52-52_UTC_DBMGZUBIB-7_1.jpg	1440	1080	2025-09-11 18:11:16.147626+02	\N	\N	\N	\N	\N	\N	1		
32	2024-10-16_14-52-52_UTC_DBMGZUBIB-7_2	original_images/2024-10-16_14-52-52_UTC_DBMGZUBIB-7_2.jpg	1440	1080	2025-09-11 18:11:16.156743+02	\N	\N	\N	\N	\N	\N	1		
33	2024-10-16_14-52-52_UTC_DBMGZUBIB-7_3	original_images/2024-10-16_14-52-52_UTC_DBMGZUBIB-7_3.jpg	1440	1080	2025-09-11 18:11:16.166464+02	\N	\N	\N	\N	\N	\N	1		
34	2024-10-30_14-08-14_UTC_DBwEasFIpEa_1	original_images/2024-10-30_14-08-14_UTC_DBwEasFIpEa_1.jpg	1440	1800	2025-09-11 18:11:16.211077+02	\N	\N	\N	\N	\N	\N	1		
35	2024-10-30_14-08-14_UTC_DBwEasFIpEa_2	original_images/2024-10-30_14-08-14_UTC_DBwEasFIpEa_2.jpg	1440	1800	2025-09-11 18:11:16.226829+02	\N	\N	\N	\N	\N	\N	1		
36	2024-10-30_14-08-14_UTC_DBwEasFIpEa_3	original_images/2024-10-30_14-08-14_UTC_DBwEasFIpEa_3.jpg	1440	1800	2025-09-11 18:11:16.241838+02	\N	\N	\N	\N	\N	\N	1		
37	2024-10-30_14-08-14_UTC_DBwEasFIpEa_4	original_images/2024-10-30_14-08-14_UTC_DBwEasFIpEa_4.jpg	1440	1800	2025-09-11 18:11:16.266379+02	\N	\N	\N	\N	\N	\N	1		
38	2024-10-30_14-08-14_UTC_DBwEasFIpEa_5	original_images/2024-10-30_14-08-14_UTC_DBwEasFIpEa_5.jpg	1440	1800	2025-09-11 18:11:16.283029+02	\N	\N	\N	\N	\N	\N	1		
39	2024-11-19_08-08-55_UTC_DCi7MhRoUba_1	original_images/2024-11-19_08-08-55_UTC_DCi7MhRoUba_1.jpg	1440	1800	2025-09-11 18:11:16.325215+02	\N	\N	\N	\N	\N	\N	1		
40	2024-11-19_08-08-55_UTC_DCi7MhRoUba_2	original_images/2024-11-19_08-08-55_UTC_DCi7MhRoUba_2.jpg	1440	1799	2025-09-11 18:11:16.337712+02	\N	\N	\N	\N	\N	\N	1		
41	2024-12-15_12-13-25_UTC_DDmT2CBIH9o_1	original_images/2024-12-15_12-13-25_UTC_DDmT2CBIH9o_1.jpg	1440	1800	2025-09-11 18:11:16.387222+02	\N	\N	\N	\N	\N	\N	1		
42	2024-12-15_12-13-25_UTC_DDmT2CBIH9o_2	original_images/2024-12-15_12-13-25_UTC_DDmT2CBIH9o_2.jpg	1440	1796	2025-09-11 18:11:16.406733+02	\N	\N	\N	\N	\N	\N	1		
43	2025-01-20_19-21-48_UTC_DFDxfDbI92Z_1	original_images/2025-01-20_19-21-48_UTC_DFDxfDbI92Z_1.jpg	1440	1800	2025-09-11 18:11:16.442695+02	\N	\N	\N	\N	\N	\N	1		
44	2025-01-20_19-21-48_UTC_DFDxfDbI92Z_2	original_images/2025-01-20_19-21-48_UTC_DFDxfDbI92Z_2.jpg	1440	1800	2025-09-11 18:11:16.454659+02	\N	\N	\N	\N	\N	\N	1		
45	2024-08-09_16-50-48_UTC_C-dN1qANwwt	original_images/2024-08-09_16-50-48_UTC_C-dN1qANwwt_IAuQcHU.jpg	1839	1839	2025-09-11 18:13:58.298423+02	\N	\N	\N	\N	\N	\N	1		
46	2024-08-10_14-17-46_UTC_C-fhHqFNKWI_1	original_images/2024-08-10_14-17-46_UTC_C-fhHqFNKWI_1_fj3zXeI.jpg	1440	1800	2025-09-11 18:13:58.341934+02	\N	\N	\N	\N	\N	\N	1		
47	2024-08-10_14-17-46_UTC_C-fhHqFNKWI_2	original_images/2024-08-10_14-17-46_UTC_C-fhHqFNKWI_2_rM6wGJy.jpg	1440	1800	2025-09-11 18:13:58.354456+02	\N	\N	\N	\N	\N	\N	1		
48	2024-08-13_17-25-18_UTC_C-nk927N_qi_1	original_images/2024-08-13_17-25-18_UTC_C-nk927N_qi_1_H4leCm4.jpg	1440	1440	2025-09-11 18:13:58.390603+02	\N	\N	\N	\N	\N	\N	1		
49	2024-08-13_17-25-18_UTC_C-nk927N_qi_2	original_images/2024-08-13_17-25-18_UTC_C-nk927N_qi_2_3n5Zac6.jpg	1440	1440	2025-09-11 18:13:58.40753+02	\N	\N	\N	\N	\N	\N	1		
50	2024-08-13_17-25-18_UTC_C-nk927N_qi_3	original_images/2024-08-13_17-25-18_UTC_C-nk927N_qi_3_cooR8QO.jpg	1440	1440	2025-09-11 18:13:58.422545+02	\N	\N	\N	\N	\N	\N	1		
51	2024-08-13_17-25-18_UTC_C-nk927N_qi_4	original_images/2024-08-13_17-25-18_UTC_C-nk927N_qi_4_5VfzZLD.jpg	1440	1440	2025-09-11 18:13:58.440336+02	\N	\N	\N	\N	\N	\N	1		
52	2024-08-22_15-01-07_UTC_C--fnqvINx0_1	original_images/2024-08-22_15-01-07_UTC_C--fnqvINx0_1_mBvuXVz.jpg	1440	1800	2025-09-11 18:13:58.482831+02	\N	\N	\N	\N	\N	\N	1		
53	2024-08-22_15-01-07_UTC_C--fnqvINx0_2	original_images/2024-08-22_15-01-07_UTC_C--fnqvINx0_2_sUPt1Zt.jpg	1440	1800	2025-09-11 18:13:58.500196+02	\N	\N	\N	\N	\N	\N	1		
54	2024-08-22_15-01-07_UTC_C--fnqvINx0_3	original_images/2024-08-22_15-01-07_UTC_C--fnqvINx0_3_b5CpRTR.jpg	1440	1800	2025-09-11 18:13:58.5181+02	\N	\N	\N	\N	\N	\N	1		
55	2024-09-03_14-13-17_UTC_C_dTrzno1AU_1	original_images/2024-09-03_14-13-17_UTC_C_dTrzno1AU_1_6S5tDaB.jpg	1440	1800	2025-09-11 18:13:58.550033+02	\N	\N	\N	\N	\N	\N	1		
56	2024-09-03_14-13-17_UTC_C_dTrzno1AU_2	original_images/2024-09-03_14-13-17_UTC_C_dTrzno1AU_2_LIrwuUV.jpg	1440	1800	2025-09-11 18:13:58.560602+02	\N	\N	\N	\N	\N	\N	1		
57	2024-09-04_14-37-08_UTC_C_f7NXgITY1_1	original_images/2024-09-04_14-37-08_UTC_C_f7NXgITY1_1_Uo3rly7.jpg	1440	1799	2025-09-11 18:13:58.594997+02	\N	\N	\N	\N	\N	\N	1		
58	2024-09-04_14-37-08_UTC_C_f7NXgITY1_2	original_images/2024-09-04_14-37-08_UTC_C_f7NXgITY1_2_ealF048.jpg	1440	1800	2025-09-11 18:13:58.609457+02	\N	\N	\N	\N	\N	\N	1		
59	2024-10-01_16-48-29_UTC_DAlrtEQoLJm_1	original_images/2024-10-01_16-48-29_UTC_DAlrtEQoLJm_1_PlNeL18.jpg	1440	1800	2025-09-11 18:13:58.643104+02	\N	\N	\N	\N	\N	\N	1		
60	2024-10-01_16-48-29_UTC_DAlrtEQoLJm_2	original_images/2024-10-01_16-48-29_UTC_DAlrtEQoLJm_2_hVK50qa.jpg	1440	1800	2025-09-11 18:13:58.662166+02	\N	\N	\N	\N	\N	\N	1		
61	2024-10-16_14-52-52_UTC_DBMGZUBIB-7_1	original_images/2024-10-16_14-52-52_UTC_DBMGZUBIB-7_1_3ruUEOL.jpg	1440	1080	2025-09-11 18:13:58.691855+02	\N	\N	\N	\N	\N	\N	1		
62	2024-10-16_14-52-52_UTC_DBMGZUBIB-7_2	original_images/2024-10-16_14-52-52_UTC_DBMGZUBIB-7_2_ND7dYg0.jpg	1440	1080	2025-09-11 18:13:58.700686+02	\N	\N	\N	\N	\N	\N	1		
63	2024-10-16_14-52-52_UTC_DBMGZUBIB-7_3	original_images/2024-10-16_14-52-52_UTC_DBMGZUBIB-7_3_6xhAuR1.jpg	1440	1080	2025-09-11 18:13:58.709684+02	\N	\N	\N	\N	\N	\N	1		
64	2024-10-30_14-08-14_UTC_DBwEasFIpEa_1	original_images/2024-10-30_14-08-14_UTC_DBwEasFIpEa_1_WIolPrG.jpg	1440	1800	2025-09-11 18:13:58.747507+02	\N	\N	\N	\N	\N	\N	1		
65	2024-10-30_14-08-14_UTC_DBwEasFIpEa_2	original_images/2024-10-30_14-08-14_UTC_DBwEasFIpEa_2_88vKNfO.jpg	1440	1800	2025-09-11 18:13:58.763526+02	\N	\N	\N	\N	\N	\N	1		
66	2024-10-30_14-08-14_UTC_DBwEasFIpEa_3	original_images/2024-10-30_14-08-14_UTC_DBwEasFIpEa_3_oWasLxo.jpg	1440	1800	2025-09-11 18:13:58.777182+02	\N	\N	\N	\N	\N	\N	1		
67	2024-10-30_14-08-14_UTC_DBwEasFIpEa_4	original_images/2024-10-30_14-08-14_UTC_DBwEasFIpEa_4_CxmjuPK.jpg	1440	1800	2025-09-11 18:13:58.791997+02	\N	\N	\N	\N	\N	\N	1		
68	2024-10-30_14-08-14_UTC_DBwEasFIpEa_5	original_images/2024-10-30_14-08-14_UTC_DBwEasFIpEa_5_1YETlwP.jpg	1440	1800	2025-09-11 18:13:58.805212+02	\N	\N	\N	\N	\N	\N	1		
69	2024-11-19_08-08-55_UTC_DCi7MhRoUba_1	original_images/2024-11-19_08-08-55_UTC_DCi7MhRoUba_1_XVNfq19.jpg	1440	1800	2025-09-11 18:13:58.846896+02	\N	\N	\N	\N	\N	\N	1		
70	2024-11-19_08-08-55_UTC_DCi7MhRoUba_2	original_images/2024-11-19_08-08-55_UTC_DCi7MhRoUba_2_Z71bb33.jpg	1440	1799	2025-09-11 18:13:58.858686+02	\N	\N	\N	\N	\N	\N	1		
71	2024-12-15_12-13-25_UTC_DDmT2CBIH9o_1	original_images/2024-12-15_12-13-25_UTC_DDmT2CBIH9o_1_uf1ocs3.jpg	1440	1800	2025-09-11 18:13:58.944794+02	\N	\N	\N	\N	\N	\N	1		
72	2024-12-15_12-13-25_UTC_DDmT2CBIH9o_2	original_images/2024-12-15_12-13-25_UTC_DDmT2CBIH9o_2_YM0YwPs.jpg	1440	1796	2025-09-11 18:13:58.965329+02	\N	\N	\N	\N	\N	\N	1		
73	2025-01-20_19-21-48_UTC_DFDxfDbI92Z_1	original_images/2025-01-20_19-21-48_UTC_DFDxfDbI92Z_1_bIMp8FD.jpg	1440	1800	2025-09-11 18:13:59.008368+02	\N	\N	\N	\N	\N	\N	1		
74	2025-01-20_19-21-48_UTC_DFDxfDbI92Z_2	original_images/2025-01-20_19-21-48_UTC_DFDxfDbI92Z_2_OYcW7om.jpg	1440	1800	2025-09-11 18:13:59.0201+02	\N	\N	\N	\N	\N	\N	1		
\.


--
-- TOC entry 4669 (class 0 OID 27189)
-- Dependencies: 294
-- Data for Name: wagtailimages_rendition; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailimages_rendition (id, file, width, height, focal_point_key, filter_spec, image_id) FROM stdin;
1	images/live-project-1_QLyVan7.width-800.jpg	800	600		width-800	10
2	images/live-project-1_QLyVan7.width-400.jpg	400	300		width-400	10
3	images/live-project-2_rQ4CJhe.width-800.jpg	800	600		width-800	11
4	images/live-project-2_rQ4CJhe.width-400.jpg	400	300		width-400	11
5	images/live-project-3_uCenhLA.width-800.jpg	800	600		width-800	12
6	images/live-project-3_uCenhLA.width-400.jpg	400	300		width-400	12
7	images/live-project-4_eRFcsUN.width-800.jpg	800	600		width-800	13
8	images/live-project-4_eRFcsUN.width-400.jpg	400	300		width-400	13
9	images/live-project-5_Nx6pxPJ.width-800.jpg	800	600		width-800	14
10	images/live-project-5_Nx6pxPJ.width-400.jpg	400	300		width-400	14
11	images/live-project-1_QLyVan7.2e16d0ba.fill-60x60.jpg	60	60	2e16d0ba	fill-60x60	10
12	images/live-project-2_rQ4CJhe.2e16d0ba.fill-60x60.jpg	60	60	2e16d0ba	fill-60x60	11
13	images/live-project-3_uCenhLA.2e16d0ba.fill-60x60.jpg	60	60	2e16d0ba	fill-60x60	12
14	images/live-project-4_eRFcsUN.2e16d0ba.fill-60x60.jpg	60	60	2e16d0ba	fill-60x60	13
15	images/live-project-5_Nx6pxPJ.2e16d0ba.fill-60x60.jpg	60	60	2e16d0ba	fill-60x60	14
16	images/live-project-5_Nx6pxPJ.max-165x165.jpg	165	123		max-165x165	14
17	images/live-project-4_eRFcsUN.max-165x165.jpg	165	123		max-165x165	13
18	images/live-project-3_uCenhLA.max-165x165.jpg	165	123		max-165x165	12
19	images/live-project-2_rQ4CJhe.max-165x165.jpg	165	123		max-165x165	11
20	images/live-project-1_QLyVan7.max-165x165.jpg	165	123		max-165x165	10
21	images/live-project-5_S0Y1mdY.max-165x165.jpg	165	123		max-165x165	9
22	images/live-project-4_LVh7JDF.max-165x165.jpg	165	123		max-165x165	8
23	images/live-project-3_Ggpn4bp.max-165x165.jpg	165	123		max-165x165	7
24	images/live-project-2_ejBqhTh.max-165x165.jpg	165	123		max-165x165	6
25	images/live-project-1_iyzcC0q.max-165x165.jpg	165	123		max-165x165	5
26	images/stock-image-4_EsykVBU.max-165x165.jpg	165	109		max-165x165	4
27	images/stock-image-3_3qmAojx.max-165x165.jpg	165	55		max-165x165	3
28	images/stock-image-2_FnfE1HR.max-165x165.jpg	123	165		max-165x165	2
29	images/stock-image-1_0A2NUWQ.max-165x165.jpg	165	123		max-165x165	1
30	images/stock-image-1_0A2NUWQ.width-40.jpg	40	30		width-40	1
31	images/live-project-2_rQ4CJhe.2e16d0ba.fill-400x300.jpg	400	300	2e16d0ba	fill-400x300	11
32	images/live-project-3_uCenhLA.2e16d0ba.fill-400x300.jpg	400	300	2e16d0ba	fill-400x300	12
33	images/live-project-4_eRFcsUN.2e16d0ba.fill-400x300.jpg	400	300	2e16d0ba	fill-400x300	13
34	images/live-project-5_Nx6pxPJ.2e16d0ba.fill-400x300.jpg	400	300	2e16d0ba	fill-400x300	14
35	images/stock-image-1_0A2NUWQ.width-1200.jpg	800	600		width-1200	1
36	images/stock-image-1_0A2NUWQ.width-600.jpg	600	450		width-600	1
37	images/live-project-1_QLyVan7.width-1200.jpg	800	600		width-1200	10
38	images/live-project-2_rQ4CJhe.width-1200.jpg	800	600		width-1200	11
39	images/live-project-1_QLyVan7.2e16d0ba.fill-400x300.jpg	400	300	2e16d0ba	fill-400x300	10
\.


--
-- TOC entry 4702 (class 0 OID 27551)
-- Dependencies: 327
-- Data for Name: wagtailredirects_redirect; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailredirects_redirect (id, old_path, is_permanent, redirect_link, redirect_page_id, site_id, automatically_created, created_at, redirect_page_route_path) FROM stdin;
\.


--
-- TOC entry 4704 (class 0 OID 27623)
-- Dependencies: 329
-- Data for Name: wagtailsearch_indexentry; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailsearch_indexentry (id, object_id, title_norm, content_type_id, autocomplete, title, body) FROM stdin;
98	21	0.4666666666666667	26	'-08':2 '-13':3 '-18':6 '-25':5 '17':4 '2024':1 '4':12 'c':9 'c-nk927n':8 'nk927n':10 'qi':11 'utc':7	'-08':2A '-13':3A '-18':6A '-25':5A '17':4A '2024':1A '4':12A 'c':9A 'c-nk927n':8A 'nk927n':10A 'qi':11A 'utc':7A	
87	13	0.2135642135642135	58	'af':20 'anden':18 'at':15 'bare':9 'den':17 'der':23 'det':7,21 'dig':25 'ende':19 'gange':2 'holder':24 'kan':3,11 'kræver':8 'lokke':12 'man':4,10 'nogen':1,13 'reb':22 'sikre':16 'spare':5 'stilladset':6 'til':14 '🧗':26	'af':20B 'anden':18B 'bare':9B 'den':17B 'der':23B 'det':7B,21B 'dig':25B 'end':19B 'gang':2B 'holder':24B 'kan':3B,11B 'kræver':8B 'lokk':12B 'man':4B,10B 'nogen':1B,13B 'reb':22B 'sikr':16B 'spare':5B 'stilladset':6B 'til':14B '🧗':26B	
90	16	0.42513368983957217	26	'-08':2 '-10':3 '-17':5 '-46':6 '1':11 '14':4 '2024':1 'c':9 'c-fhhqfnkwi':8 'fhhqfnkwi':10 'utc':7	'-08':2A '-10':3A '-17':5A '-46':6A '1':11A '14':4A '2024':1A 'c':9A 'c-fhhqfnkwi':8A 'fhhqfnkwi':10A 'utc':7A	
80	11	3.7666666666666666	51	'galleri':1	'galleri':1B	
91	17	0.44155844155844154	26	'-08':2 '-10':3 '-17':5 '-46':6 '14':4 '2':11 '2024':1 'c':9 'c-fhhqfnkwi':8 'fhhqfnkwi':10 'utc':7	'-08':2A '-10':3A '-17':5A '-46':6A '14':4A '2':11A '2024':1A 'c':9A 'c-fhhqfnkwi':8A 'fhhqfnkwi':10A 'utc':7A	
92	14	0.8148148148148149	58	'disse':5 'døre':6 'fugen':1 'på':4 'skiftes':3 'skulle':2	'diss':5B 'døre':6B 'fugen':1B 'på':4B 'skift':3B 'skull':2B	
83	12	0.9435483870967742	58	'i':4 'jatoba':5 'lille':1 'trin':2 'udført':3	'jatoba':5B 'lill':1B 'trin':2B 'udført':3B	
86	15	0.396875	26	'-08':2 '-09':3 '-48':6 '-50':5 '16':4 '2024':1 'c':9 'c-dn1qanwwt':8 'dn1qanwwt':10 'utc':7	'-08':2A '-09':3A '-48':6A '-50':5A '16':4A '2024':1A 'c':9A 'c-dn1qanwwt':8A 'dn1qanwwt':10A 'utc':7A	
95	18	0.42342342342342343	26	'-08':2 '-13':3 '-18':6 '-25':5 '1':12 '17':4 '2024':1 'c':9 'c-nk927n':8 'nk927n':10 'qi':11 'utc':7	'-08':2A '-13':3A '-18':6A '-25':5A '1':12A '17':4A '2024':1A 'c':9A 'c-nk927n':8A 'nk927n':10A 'qi':11A 'utc':7A	
96	19	0.4385964912280702	26	'-08':2 '-13':3 '-18':6 '-25':5 '17':4 '2':12 '2024':1 'c':9 'c-nk927n':8 'nk927n':10 'qi':11 'utc':7	'-08':2A '-13':3A '-18':6A '-25':5A '17':4A '2':12A '2024':1A 'c':9A 'c-nk927n':8A 'nk927n':10A 'qi':11A 'utc':7A	
97	20	0.452991452991453	26	'-08':2 '-13':3 '-18':6 '-25':5 '17':4 '2024':1 '3':12 'c':9 'c-nk927n':8 'nk927n':10 'qi':11 'utc':7	'-08':2A '-13':3A '-18':6A '-25':5A '17':4A '2024':1A '3':12A 'c':9A 'c-nk927n':8A 'nk927n':10A 'qi':11A 'utc':7A	
99	15	1.3902439024390243	58	'bliver':2 'lærepladsen':1 'også':3 'passet🦦':4	'bliver':2B 'lærepladsen':1B 'også':3B 'passet🦦':4B	
102	22	0.5666666666666667	26	'-01':5 '-07':6 '-08':2 '-22':3 '1':10 '15':4 '2024':1 'c':8 'fnqvinx0':9 'utc':7	'-01':5A '-07':6A '-08':2A '-22':3A '1':10A '15':4A '2024':1A 'c':8A 'fnqvinx0':9A 'utc':7A	
103	23	0.5767441860465116	26	'-01':5 '-07':6 '-08':2 '-22':3 '15':4 '2':10 '2024':1 'c':8 'fnqvinx0':9 'utc':7	'-01':5A '-07':6A '-08':2A '-22':3A '15':4A '2':10A '2024':1A 'c':8A 'fnqvinx0':9A 'utc':7A	
104	24	0.5863636363636363	26	'-01':5 '-07':6 '-08':2 '-22':3 '15':4 '2024':1 '3':10 'c':8 'fnqvinx0':9 'utc':7	'-01':5A '-07':6A '-08':2A '-22':3A '15':4A '2024':1A '3':10A 'c':8A 'fnqvinx0':9A 'utc':7A	
105	16	0.5434343434343435	58	'at':4 'billede':8 'det':9 'et':6 'før':7 'glemt':3 'har':1,10 'jeg':2,11 'lige':14 'nok':13 'tage':5 'vist':12	'billed':8B 'det':9B 'et':6B 'før':7B 'glemt':3B 'har':1B,10B 'jeg':2B,11B 'lige':14B 'nok':13B 'tage':5B 'vist':12B	
10	1	0.7724137931034483	26	'1':6 'billede':2 'image':5 'stock':1,4 'stock-image':3	'1':6A 'billed':2A 'imag':5A 'stock':1A,4A 'stock-imag':3A	
32	10	0.7724137931034483	41		'køkken':5 'og':3 'terrass':2 'træ':1 'udendør':4	'45m²':21 'aftentim':34 'belysn':32 'blev':42 'brugt':36 'budget':48 'bygget':8 'en':9 'fantastisk':10 'færdiggjort':43 'grill':23 'har':7 'indbygget':22 'integreret':13 'kogezon':25 'køkken':3,15 'led':31 'led-belysn':30 'lærketræ':18,37 'material':35 'med':12 'natursten':40 'og':4,24,46 'omfatt':17 'opbevaringsløsning':26 'projektet':16,41 'på':20 'rustfrit':38 'smukt':1 'stål':39 'terrass':5,19 'tiden':45 'til':33,44 'træ':29 'træterrass':11 'udendør':2,14 'vejrbestandigt':28 'vi':6 'within':47
12	2	0.7724137931034483	26	'2':6 'billede':2 'image':5 'stock':1,4 'stock-image':3	'2':6A 'billed':2A 'imag':5A 'stock':1A,4A 'stock-imag':3A	
14	3	0.7724137931034483	26	'3':6 'billede':2 'image':5 'stock':1,4 'stock-image':3	'3':6A 'billed':2A 'imag':5A 'stock':1A,4A 'stock-imag':3A	
16	4	0.7724137931034483	26	'4':6 'billede':2 'image':5 'stock':1,4 'stock-image':3	'4':6A 'billed':2A 'imag':5A 'stock':1A,4A 'stock-imag':3A	
18	5	0.5517241379310345	26	'billede':7 'køkken':5 'og':3 'projekt':6 'terrasse':2 'træ':1 'udendørs':4	'billed':7A 'køkken':5A 'og':3A 'projekt':6A 'terrass':2A 'træ':1A 'udendør':4A	
4	4	1.9310344827586208	51	'ad':5 'aliquip':15 'commodo':18 'consequat':19 'ea':17 'enim':4 'ex':16 'exercitation':10 'galleri':2 'laboris':12 'minim':6 'nisi':13 'nostrud':9 'projekt':1 'quis':8 'ullamco':11 'ut':3,14 'veniam':7	'galleri':2B 'projekt':1B	'ad':3 'aliquip':13 'commodo':16 'consequat':17 'ea':15 'enim':2 'ex':14 'exercit':8 'labori':10 'minim':4 'nisi':11 'nostrud':7 'qui':6 'ullamco':9 'ut':1,12 'veniam':5
37	13	0.9655172413793104	26	'badeværelse':1 'billede':4 'projekt':3 'renovering':2	'badeværels':1A 'billed':4A 'projekt':3A 'renov':2A	
39	14	0.9655172413793104	26	'billede':4 'kontorbygning':2 'moderne':1 'projekt':3	'billed':4A 'kontorbygn':2A 'modern':1A 'projekt':3A	
38	13	1.9310344827586208	41		'badeværels':1 'renov':2	'af':5,26 'badekar':12 'badeværels':2,7,23 'der':24 'et':19 'fliser':10 'fritståend':11 'fuldstændig':3 'italiensk':8 'komfort':29 'lignend':22 'luksuriøst':1 'luksus':27 'marmor':9 'master':6 'med':14 'møbel':18 'og':28 'oser':25 'regnbrus':13 'renov':4 'skræddersyet':16 'spa':21 'spa-lignend':20 'termostat':15 'vask':17
40	14	1.9310344827586208	41		'kontorbygn':2 'modern':1	'af':7 'arbejdsmiljø':36 'byggeriet':17 'bæredygtig':13 'bæredygtigh':5 'der':29 'energieffektiv':23 'erhvervsprojekt':1 'et':32 'fleksibl':27 'fokus':3 'glasparti':19 'hele':16 'kan':30 'kontorbygn':9 'kontorrum':28 'lys':22 'material':14 'med':2 'miljøvenligt':35 'mindr':11 'modern':8,33 'naturligt':21 'og':25,34 'opførels':6 'på':4 'store':18 'tilpass':31 'varm':24 'ventilationsystem':26 'virksomh':12
108	25	0.6065217391304348	26	'-03':3 '-09':2 '-13':5 '-17':6 '1':10 '14':4 '2024':1 'c':8 'dtrzno1au':9 'utc':7	'-03':3A '-09':2A '-13':5A '-17':6A '1':10A '14':4A '2024':1A 'c':8A 'dtrzno1au':9A 'utc':7A	
109	26	0.6148936170212767	26	'-03':3 '-09':2 '-13':5 '-17':6 '14':4 '2':10 '2024':1 'c':8 'dtrzno1au':9 'utc':7	'-03':3A '-09':2A '-13':5A '-17':6A '14':4A '2':10A '2024':1A 'c':8A 'dtrzno1au':9A 'utc':7A	
118	29	0.7072649572649572	26	'-01':3 '-10':2 '-29':6 '-48':5 '1':9 '16':4 '2024':1 'dalrteqoljm':8 'utc':7	'-01':3A '-10':2A '-29':6A '-48':5A '1':9A '16':4A '2024':1A 'dalrteqoljm':8A 'utc':7A	
119	30	0.7127882599580714	26	'-01':3 '-10':2 '-29':6 '-48':5 '16':4 '2':9 '2024':1 'dalrteqoljm':8 'utc':7	'-01':3A '-10':2A '-29':6A '-48':5A '16':4A '2':9A '2024':1A 'dalrteqoljm':8A 'utc':7A	
110	17	1.0243055555555556	58	'er':4 'glad':6 'i':2 'mig':3 'møbelsnedkeren':1 'virkelig':5 '🥳':7	'er':4B 'glad':6B 'mig':3B 'møbelsnedkeren':1B 'virkelig':5B '🥳':7B	
113	27	0.6224489795918366	26	'-04':3 '-08':6 '-09':2 '-37':5 '1':10 '14':4 '2024':1 'c':8 'f7nxgity1':9 'utc':7	'-04':3A '-08':6A '-09':2A '-37':5A '1':10A '14':4A '2024':1A 'c':8A 'f7nxgity1':9A 'utc':7A	
114	28	0.63	26	'-04':3 '-08':6 '-09':2 '-37':5 '14':4 '2':10 '2024':1 'c':8 'f7nxgity1':9 'utc':7	'-04':3A '-08':6A '-09':2A '-37':5A '14':4A '2':10A '2024':1A 'c':8A 'f7nxgity1':9A 'utc':7A	
130	35	0.7518518518518519	26	'-08':5 '-10':2 '-14':6 '-30':3 '14':4 '2':9 '2024':1 'dbweasfipea':8 'utc':7	'-08':5A '-10':2A '-14':6A '-30':3A '14':4A '2':9A '2024':1A 'dbweasfipea':8A 'utc':7A	
126	20	0.35208711433756806	58	'at':7 'det':18 'fikse':8 'for':6 'havde':1 'hyggeligt':21 'linolie':15 'linoliemaling':17 'med':4 'min':12 'og':16 'om':14 'samt':10 'super':20 'søde':2 'tihizebra':3 'ude':5 'udvide':11 'var':19 'viden':13 'vinduer':9	'det':18B 'fiks':8B 'havd':1B 'hyggeligt':21B 'linoli':15B 'linoliem':17B 'med':4B 'min':12B 'og':16B 'om':14B 'samt':10B 'super':20B 'søde':2B 'tihizebra':3B 'ude':5B 'udvid':11B 'var':19B 'viden':13B 'vinduer':9B	
115	18	0.9019607843137254	58	'4':3,6 'bevaringsværdige':1 'færdige':5 'sæt':4,7 'tilbage':8 'vinduer':2 '🪵':9	'4':3B,6B 'bevaringsværdig':1B 'færdige':5B 'sæt':4B,7B 'tilbag':8B 'vinduer':2B '🪵':9B	
123	31	0.7090909090909091	26	'-10':2 '-16':3 '-52':5,6 '-7':9 '1':10 '14':4 '2024':1 'dbmgzubib':8 'utc':7	'-10':2A '-16':3A '-52':5A,6A '-7':9A '1':10A '14':4A '2024':1A 'dbmgzubib':8A 'utc':7A	
124	32	0.7142857142857143	26	'-10':2 '-16':3 '-52':5,6 '-7':9 '14':4 '2':10 '2024':1 'dbmgzubib':8 'utc':7	'-10':2A '-16':3A '-52':5A,6A '-7':9A '14':4A '2':10A '2024':1A 'dbmgzubib':8A 'utc':7A	
125	33	0.7192982456140351	26	'-10':2 '-16':3 '-52':5,6 '-7':9 '14':4 '2024':1 '3':10 'dbmgzubib':8 'utc':7	'-10':2A '-16':3A '-52':5A,6A '-7':9A '14':4A '2024':1A '3':10A 'dbmgzubib':8A 'utc':7A	
129	34	0.7476459510357816	26	'-08':5 '-10':2 '-14':6 '-30':3 '1':9 '14':4 '2024':1 'dbweasfipea':8 'utc':7	'-08':5A '-10':2A '-14':6A '-30':3A '1':9A '14':4A '2024':1A 'dbweasfipea':8A 'utc':7A	
131	36	0.75591985428051	26	'-08':5 '-10':2 '-14':6 '-30':3 '14':4 '2024':1 '3':9 'dbweasfipea':8 'utc':7	'-08':5A '-10':2A '-14':6A '-30':3A '14':4A '2024':1A '3':9A 'dbweasfipea':8A 'utc':7A	
132	37	0.7598566308243728	26	'-08':5 '-10':2 '-14':6 '-30':3 '14':4 '2024':1 '4':9 'dbweasfipea':8 'utc':7	'-08':5A '-10':2A '-14':6A '-30':3A '14':4A '2024':1A '4':9A 'dbweasfipea':8A 'utc':7A	
133	38	0.763668430335097	26	'-08':5 '-10':2 '-14':6 '-30':3 '14':4 '2024':1 '5':9 'dbweasfipea':8 'utc':7	'-08':5A '-10':2A '-14':6A '-30':3A '14':4A '2024':1A '5':9A 'dbweasfipea':8A 'utc':7A	
134	21	0.4384765625	58	'at':13 'det':11,14 'eller':5 'en':1 'er':10 'gennemføring':4,8 'heldigt':12 'indefra':18 'kan':15 'korrekt':17 'laves':16 'mangel':6 'på':7 'så':9 'uheldig':2 'undertags':3 '🦔':19	'det':11B,14B 'eller':5B 'en':1B 'er':10B 'gennemfør':4B,8B 'heldigt':12B 'indefra':18B 'kan':15B 'korrekt':17B 'lave':16B 'mangel':6B 'på':7B 'så':9B 'uheldig':2B 'undertag':3B '🦔':19B	
137	39	0.7829059829059829	26	'-08':5 '-11':2 '-19':3 '-55':6 '08':4 '1':9 '2024':1 'dci7mhrouba':8 'utc':7	'-08':5A '-11':2A '-19':3A '-55':6A '08':4A '1':9A '2024':1A 'dci7mhrouba':8A 'utc':7A	
138	40	0.7861952861952862	26	'-08':5 '-11':2 '-19':3 '-55':6 '08':4 '2':9 '2024':1 'dci7mhrouba':8 'utc':7	'-08':5A '-11':2A '-19':3A '-55':6A '08':4A '2':9A '2024':1A 'dci7mhrouba':8A 'utc':7A	
143	42	0.8051529790660226	26	'-12':2 '-13':5 '-15':3 '-25':6 '12':4 '2':9 '2024':1 'ddmt2cbih9o':8 'utc':7	'-12':2A '-13':5A '-15':3A '-25':6A '12':4A '2':9A '2024':1A 'ddmt2cbih9o':8A 'utc':7A	
148	44	0.8117283950617283	26	'-01':2 '-20':3 '-21':5 '-48':6 '19':4 '2':9 '2025':1 'dfdxfdbi92z':8 'utc':7	'-01':2A '-20':3A '-21':5A '-48':6A '19':4A '2':9A '2025':1A 'dfdxfdbi92z':8A 'utc':7A	
139	22	0.47960199004975124	58	'af':2 'at':6 'dejligt':5 'det':12 'ellers':13 'et':8 'finde':7 'grå':15 'hul':10 'i':11 'lille':9 'meget':14 'punkteret':3 'rude':4 'udskiftning':1 'vejr':16 '🥸':17	'af':2B 'dejligt':5B 'det':12B 'eller':13B 'et':8B 'find':7B 'grå':15B 'hul':10B 'lill':9B 'meget':14B 'punkteret':3B 'rude':4B 'udskiftn':1B 'vejr':16B '🥸':17B	
142	41	0.8022875816993464	26	'-12':2 '-13':5 '-15':3 '-25':6 '1':9 '12':4 '2024':1 'ddmt2cbih9o':8 'utc':7	'-12':2A '-13':5A '-15':3A '-25':6A '1':9A '12':4A '2024':1A 'ddmt2cbih9o':8A 'utc':7A	
203	64	0.8977777777777778	26	'-08':5 '-10':2 '-14':6 '-30':3 '1':9 '14':4 '2024':1 'dbweasfipea':8 'utc':7	'-08':5A '-10':2A '-14':6A '-30':3A '1':9A '14':4A '2024':1A 'dbweasfipea':8A 'utc':7A	
199	31	0.42477405635300375	58	'at':7 'det':18 'fikse':8 'for':6 'havde':1 'hyggeligt':21 'linolie':15 'linoliemaling':17 'med':4 'min':12 'og':16 'om':14 'samt':10 'super':20 'søde':2 'tihizebra':3 'ude':5 'udvide':11 'var':19 'viden':13 'vinduer':9	'det':18B 'fiks':8B 'havd':1B 'hyggeligt':21B 'linoli':15B 'linoliem':17B 'med':4B 'min':12B 'og':16B 'om':14B 'samt':10B 'super':20B 'søde':2B 'tihizebra':3B 'ude':5B 'udvid':11B 'var':19B 'viden':13B 'vinduer':9B	
144	23	1.0352272727272727	58	'af':3 'alteret':5 'efter':9 'en':1 'før':11 'hos':6 'kammerat🦔':8 'min':7 'og':10 'opgradering':2 'tv':4	'af':3B 'alteret':5B 'en':1B 'hos':6B 'kammerat🦔':8B 'min':7B 'opgrad':2B 'tv':4B	'efter':1 'før':3 'og':2
20	6	0.7724137931034483	26	'billede':6 'i':3 'københavn':4 'projekt':5 'renovering':2 'villa':1	'billed':6A 'københavn':4A 'projekt':5A 'renov':2A 'villa':1A	
22	7	0.7724137931034483	26	'billede':5 'installation':3 'køkken':2 'projekt':4 'skræddersyet':1	'billed':5A 'instal':3A 'køkken':2A 'projekt':4A 'skræddersyet':1A	
24	8	0.9655172413793104	26	'badeværelse':1 'billede':4 'projekt':3 'renovering':2	'badeværels':1A 'billed':4A 'projekt':3A 'renov':2A	
26	9	0.9655172413793104	26	'billede':4 'kontorbygning':2 'moderne':1 'projekt':3	'billed':4A 'kontorbygn':2A 'modern':1A 'projekt':3A	
31	10	0.5517241379310345	26	'billede':7 'køkken':5 'og':3 'projekt':6 'terrasse':2 'træ':1 'udendørs':4	'billed':7A 'køkken':5A 'og':3A 'projekt':6A 'terrass':2A 'træ':1A 'udendør':4A	
33	11	0.7724137931034483	26	'billede':6 'i':3 'københavn':4 'projekt':5 'renovering':2 'villa':1	'billed':6A 'københavn':4A 'projekt':5A 'renov':2A 'villa':1A	
35	12	0.7724137931034483	26	'billede':5 'installation':3 'køkken':2 'projekt':4 'skræddersyet':1	'billed':5A 'instal':3A 'køkken':2A 'projekt':4A 'skræddersyet':1A	
65	1	3.8620689655172415	1	'root':1	'root':1B	
66	2	0.9655172413793104	1	'new':4 'site':6 'to':2 'wagtail':5 'welcome':1 'your':3	'new':4B 'site':6B 'wagtail':5B 'welcom':1B	
147	43	0.8090766823161188	26	'-01':2 '-20':3 '-21':5 '-48':6 '1':9 '19':4 '2025':1 'dfdxfdbi92z':8 'utc':7	'-01':2A '-20':3A '-21':5A '-48':6A '1':9A '19':4A '2025':1A 'dfdxfdbi92z':8A 'utc':7A	
204	65	0.8987898789878986	26	'-08':5 '-10':2 '-14':6 '-30':3 '14':4 '2':9 '2024':1 'dbweasfipea':8 'utc':7	'-08':5A '-10':2A '-14':6A '-30':3A '14':4A '2':9A '2024':1A 'dbweasfipea':8A 'utc':7A	
205	66	0.8997821350762527	26	'-08':5 '-10':2 '-14':6 '-30':3 '14':4 '2024':1 '3':9 'dbweasfipea':8 'utc':7	'-08':5A '-10':2A '-14':6A '-30':3A '14':4A '2024':1A '3':9A 'dbweasfipea':8A 'utc':7A	
206	67	0.900755124056095	26	'-08':5 '-10':2 '-14':6 '-30':3 '14':4 '2024':1 '4':9 'dbweasfipea':8 'utc':7	'-08':5A '-10':2A '-14':6A '-30':3A '14':4A '2024':1A '4':9A 'dbweasfipea':8A 'utc':7A	
207	68	0.9017094017094016	26	'-08':5 '-10':2 '-14':6 '-30':3 '14':4 '2024':1 '5':9 'dbweasfipea':8 'utc':7	'-08':5A '-10':2A '-14':6A '-30':3A '14':4A '2024':1A '5':9A 'dbweasfipea':8A 'utc':7A	
159	47	0.6883116883116883	26	'-08':2 '-10':3 '-17':5 '-46':6 '14':4 '2':11 '2024':1 'c':9 'c-fhhqfnkwi':8 'fhhqfnkwi':10 'utc':7	'-08':2A '-10':3A '-17':5A '-46':6A '14':4A '2':11A '2024':1A 'c':9A 'c-fhhqfnkwi':8A 'fhhqfnkwi':10A 'utc':7A	
164	48	0.6339662447257384	26	'-08':2 '-13':3 '-18':6 '-25':5 '1':12 '17':4 '2024':1 'c':9 'c-nk927n':8 'nk927n':10 'qi':11 'utc':7	'-08':2A '-13':3A '-18':6A '-25':5A '1':12A '17':4A '2024':1A 'c':9A 'c-nk927n':8A 'nk927n':10A 'qi':11A 'utc':7A	
154	25	0.35619047619047617	58	'af':20 'anden':18 'at':15 'bare':9 'den':17 'der':23 'det':7,21 'dig':25 'ende':19 'gange':2 'holder':24 'kan':3,11 'kræver':8 'lokke':12 'man':4,10 'nogen':1,13 'reb':22 'sikre':16 'spare':5 'stilladset':6 'til':14 '🧗':26	'af':20B 'anden':18B 'bare':9B 'den':17B 'der':23B 'det':7B,21B 'dig':25B 'end':19B 'gang':2B 'holder':24B 'kan':3B,11B 'kræver':8B 'lokk':12B 'man':4B,10B 'nogen':1B,13B 'reb':22B 'sikr':16B 'spare':5B 'stilladset':6B 'til':14B '🧗':26B	
158	46	0.6842105263157895	26	'-08':2 '-10':3 '-17':5 '-46':6 '1':11 '14':4 '2024':1 'c':9 'c-fhhqfnkwi':8 'fhhqfnkwi':10 'utc':7	'-08':2A '-10':3A '-17':5A '-46':6A '1':11A '14':4A '2024':1A 'c':9A 'c-fhhqfnkwi':8A 'fhhqfnkwi':10A 'utc':7A	
149	24	1.8150684931506849	58	'i':4 'jatoba':5 'lille':1 'trin':2 'udført':3	'jatoba':5B 'lill':1B 'trin':2B 'udført':3B	
153	45	0.7297297297297297	26	'-08':2 '-09':3 '-48':6 '-50':5 '16':4 '2024':1 'c':9 'c-dn1qanwwt':8 'dn1qanwwt':10 'utc':7	'-08':2A '-09':3A '-48':6A '-50':5A '16':4A '2024':1A 'c':9A 'c-dn1qanwwt':8A 'dn1qanwwt':10A 'utc':7A	
165	49	0.6385416666666667	26	'-08':2 '-13':3 '-18':6 '-25':5 '17':4 '2':12 '2024':1 'c':9 'c-nk927n':8 'nk927n':10 'qi':11 'utc':7	'-08':2A '-13':3A '-18':6A '-25':5A '17':4A '2':12A '2024':1A 'c':9A 'c-nk927n':8A 'nk927n':10A 'qi':11A 'utc':7A	
160	26	1.2585470085470085	58	'at':9 'disse':5 'døre':6 'en':15 'fjernet':11 'fugen':1 'få':10 'lavet':14 'lus':16 'og':13 'perfekt':7 'på':4 'råd':12 'skiftes':3 'skulle':2 'tidspunkt':8 'tømrer':18 '🦔':17	'diss':5B 'døre':6B 'fugen':1B 'på':4B 'skift':3B 'skull':2B	'en':9 'fjernet':5 'få':4 'lavet':8 'lus':10 'og':7 'perfekt':1 'råd':6 'tidspunkt':2 'tømrer':12 '🦔':11
166	50	0.6430041152263374	26	'-08':2 '-13':3 '-18':6 '-25':5 '17':4 '2024':1 '3':12 'c':9 'c-nk927n':8 'nk927n':10 'qi':11 'utc':7	'-08':2A '-13':3A '-18':6A '-25':5A '17':4A '2024':1A '3':12A 'c':9A 'c-nk927n':8A 'nk927n':10A 'qi':11A 'utc':7A	
167	51	0.6473577235772358	26	'-08':2 '-13':3 '-18':6 '-25':5 '17':4 '2024':1 '4':12 'c':9 'c-nk927n':8 'nk927n':10 'qi':11 'utc':7	'-08':2A '-13':3A '-18':6A '-25':5A '17':4A '2024':1A '4':12A 'c':9A 'c-nk927n':8A 'nk927n':10A 'qi':11A 'utc':7A	
7	5	1.9310344827586208	50	'besked':6 'en':5 'kontakt':1 'os':2,4 'send':3	'kontakt':1B 'os':2B	'anim':34 'aut':2 'besk':20 'cillum':11 'culpa':29 'cupidatat':24 'deserunt':32 'dolor':4,12 'dui':1 'en':19 'ess':10 'est':36 'eu':13 'excepteur':21 'fugiat':14 'id':35 'irur':3 'laborum':37 'mollit':33 'non':25 'nulla':15 'occaecat':23 'officia':31 'os':18 'pariatur':16 'proident':26 'qui':30 'reprehenderit':6 'send':17 'sint':22 'sunt':27 'velit':9 'volupt':8
34	11	1.2873563218390804	41		'københavn':4 'renov':2 'villa':1	'1920':10 'af':2,7,19,23,32 'arkitektur':17 'badeværels':26 'den':15 'eksempel':37 'energioptim':27 'ern':11 'et':35 'familierum':34 'foren':45 'fra':9 'harmonisk':46 'histori':40 'historisk':3 'hvordan':39 'kan':44 'komfort':43 'komplet':5 'køkken':24 'med':12,28 'modern':33,42 'modernis':22 'nye':29 'og':25,41 'oprindelig':16 'original':20 'på':38 'renov':6 'respekt':13 'restaur':18 'smukt':36 'tilbygn':31 'totalrenov':1 'trægulv':21 'villa':4,8 'vinduer':30
1	3	1.2873563218390804	49	'bygge':5 'fokus':9 'håndværk':13 'jcleemannbyg':3 'kvalitet':11 'med':8 'og':6,12 'professionelle':4 'på':10 'renoveringsløsninger':7 'til':2 'velkommen':1	'jcleemannbyg':3B 'til':2B 'velkommen':1B	'3':113,131 '4':94 'af':25,121 'aldrig':56 'all':61 'altid':73,78 'arbejd':105 'bygg':2 'byggeløsning':12 'check':130 'clock':92 'de':68 'deadlin':80 'derfor':46 'design':129 'detalj':53 'dit':110 'eksempl':101 'er':89 'et':36 'fasthold':34 'fokus':6,29 'fra':17 'få':35,107 'gradient':43 'går':55 'hero':42 'hver':52 'håndværk':10,24,64 'højest':26,69 'højsædet':91 'inspir':108 'jcleemannbyg':49 'komplett':20 'kompromi':58 'kunder':48 'kundetilfredsh':31 'kvalitet':8,27,50 'kvaliteten':60 'kvalitetsmaterial':126 'københavn':14 'køkkener':122 'køkkenrenov':18,119 'lever':23,65,82 'løsninger':125 'material':62 'med':5,28,59,123 'medium':44,96,115,133 'modern':128 'normal':45,97,116,134 'nybyggeri':21 'næste':111 'og':3,9,15,32,63,81,87,106,127 'omegn':16 'op':66 'overhold':77 'planlægn':86 'professionell':1,11 'projekt':41,83,99,112 'på':7,30,57,102 'pålideligh':88 'qualiti':72 'renoveringsløsning':4 'se':39,100 'senest':104 'servic':118 'skræddersyed':124 'standard':70 'star':71 'surfac':95,114,132 'termintro':33 'tiden':75,85 'til':19,67,74,84,109 'tilbud':38 'time':93 'totalrenov':120 'udvalgt':98 'uforpligtend':37 'vi':22,54,76 'vore':40,79,103,117 'vælger':47
36	12	1.2873563218390804	41		'instal':3 'køkken':2 'skræddersyet':1	'af':30 'all':26 'behov':16 'belysn':36 'bordplad':22 'bygget':7 'både':41 'corian':21 'der':11 'designet':5 'efter':3 'eg':18 'er':40 'et':8 'funktionelt':42 'hvidevar':29 'håndlavet':1 'højder':27 'højest':31 'integrered':28 'kunden':15 'kvalitet':32 'køkken':2,10 'køkkenet':39 'køkkenø':19 'led':35 'led-belysn':34 'massiv':17 'med':20 'mål':4 'og':6,43 'passer':12 'perfekt':13 'skabe':24,38 'skjult':33 'skræddersyed':23 'smukt':45 'til':14 'unikt':9 'æstetisk':44
168	27	1.930722891566265	58	'bliver':2 'blæst':8 'byger':6 'en':20 'fået':11 'har':9 'kvist':14 'lang':21 'lavet':12 'lærepladsen':1 'mig':24 'nu':19 'nyt':16 'og':7,15 'også':3 'passet🦦':4 'solstrålerne':17 'til':23 'trods':5 'undertag':13 'vi':10 'weekend':22 '🍺':25 '😎🌞':18	'bliver':2B 'lærepladsen':1B 'også':3B 'passet🦦':4B	'blæst':4 'byger':2 'en':16 'fået':7 'har':5 'kvist':10 'lang':17 'lavet':8 'mig':20 'nu':15 'nyt':12 'og':3,11 'solstrålern':13 'til':19 'trod':1 'undertag':9 'vi':6 'weekend':18 '🍺':21 '😎🌞':14
172	52	0.775	26	'-01':5 '-07':6 '-08':2 '-22':3 '1':10 '15':4 '2024':1 'c':8 'fnqvinx0':9 'utc':7	'-01':5A '-07':6A '-08':2A '-22':3A '1':10A '15':4A '2024':1A 'c':8A 'fnqvinx0':9A 'utc':7A	
173	53	0.7776470588235294	26	'-01':5 '-07':6 '-08':2 '-22':3 '15':4 '2':10 '2024':1 'c':8 'fnqvinx0':9 'utc':7	'-01':5A '-07':6A '-08':2A '-22':3A '15':4A '2':10A '2024':1A 'c':8A 'fnqvinx0':9A 'utc':7A	
174	54	0.7802325581395348	26	'-01':5 '-07':6 '-08':2 '-22':3 '15':4 '2024':1 '3':10 'c':8 'fnqvinx0':9 'utc':7	'-01':5A '-07':6A '-08':2A '-22':3A '15':4A '2024':1A '3':10A 'c':8A 'fnqvinx0':9A 'utc':7A	
192	60	0.8807017543859649	26	'-01':3 '-10':2 '-29':6 '-48':5 '16':4 '2':9 '2024':1 'dalrteqoljm':8 'utc':7	'-01':3A '-10':2A '-29':6A '-48':5A '16':4A '2':9A '2024':1A 'dalrteqoljm':8A 'utc':7A	
175	28	0.7126436781609194	58	'at':4 'billede':8 'bog':30 'dag':33 'den':21 'derude':34 'det':9,19,24 'en':26 'er':20,25 'et':6 'før':7 'glemt':3 'god':32 'har':1,10 'i':28 'ikke':22 'jeg':2,11 'knust':18 'lige':14 'længere':23 'men':15 'min':29 'nok':13 'ruden':16 'succes':27 'tage':5 'var':17 'vist':12 '🐳':31	'billed':8B 'det':9B 'et':6B 'før':7B 'glemt':3B 'har':1B,10B 'jeg':2B,11B 'lige':14B 'nok':13B 'tage':5B 'vist':12B	'bog':16 'dag':19 'den':7 'derud':20 'det':5,10 'en':12 'er':6,11 'god':18 'ikk':8 'knust':4 'længere':9 'men':1 'min':15 'ruden':2 'succ':13 'var':3 '🐳':17
179	55	0.7863636363636363	26	'-03':3 '-09':2 '-13':5 '-17':6 '1':10 '14':4 '2024':1 'c':8 'dtrzno1au':9 'utc':7	'-03':3A '-09':2A '-13':5A '-17':6A '1':10A '14':4A '2024':1A 'c':8A 'dtrzno1au':9A 'utc':7A	
181	29	1.3111111111111111	58	'at':22 'bliver':21 'det':19 'egen':17 'er':4,11 'et':12 'første':9 'give':23 'glad':6 'i':2,25 'kast':26 'linoleumsborde🌚':30 'med':27 'mig':3 'min':16 'mit':8 'møbel':10 'møbelsnedkeren':1 'næste':20 'runde':29 'sig':24 'simpelt':13 'sofabord':14 'stue':18 'til':15 'to':28 'virkelig':5 '🥳':7	'er':4B 'glad':6B 'mig':3B 'møbelsnedkeren':1B 'virkelig':5B '🥳':7B	'bliver':14 'det':12 'egen':10 'er':4 'et':5 'første':2 'give':16 'kast':19 'linoleumsborde🌚':23 'med':20 'min':9 'mit':1 'møbel':3 'næste':13 'rund':22 'sig':17 'simpelt':6 'sofabord':7 'stue':11 'til':8
180	56	0.7887640449438202	26	'-03':3 '-09':2 '-13':5 '-17':6 '14':4 '2':10 '2024':1 'c':8 'dtrzno1au':9 'utc':7	'-03':3A '-09':2A '-13':5A '-17':6A '14':4A '2':10A '2024':1A 'c':8A 'dtrzno1au':9A 'utc':7A	
185	57	0.7890109890109891	26	'-04':3 '-08':6 '-09':2 '-37':5 '1':10 '14':4 '2024':1 'c':8 'f7nxgity1':9 'utc':7	'-04':3A '-08':6A '-09':2A '-37':5A '1':10A '14':4A '2024':1A 'c':8A 'f7nxgity1':9A 'utc':7A	
186	58	0.7913043478260869	26	'-04':3 '-08':6 '-09':2 '-37':5 '14':4 '2':10 '2024':1 'c':8 'f7nxgity1':9 'utc':7	'-04':3A '-08':6A '-09':2A '-37':5A '14':4A '2':10A '2024':1A 'c':8A 'f7nxgity1':9A 'utc':7A	
187	30	1.1290322580645162	58	'4':3,6 'behandlet':10 'bevaringsværdige':1 'færdige':5 'linolie':12 'linoliemaling':14 'med':11 'og':13 'sæt':4,7 'tilbage':8 'vinduer':2 '🖌️':15 '🪵':9	'4':3B,6B 'bevaringsværdig':1B 'færdige':5B 'sæt':4B,7B 'tilbag':8B 'vinduer':2B '🪵':9B	'behandlet':1 'linoli':3 'linoliem':5 'med':2 'og':4 '🖌️':6
120	19	3.963157894736842	58	'alvor':12 'at':4 'dejligt':3 'efteråret':10 'er':13 'for':11 'fundament/beton/whatever':1 'ind':15 'indenfor':8 'kunne':5 'nu':9 'sat':14 'semi':7 'skjuler':2 'være':6 '🍁🦔':16	'fundament/beton/whatever':1B 'skjuler':2B	'alvor':10 'dejligt':1 'efteråret':8 'er':11 'ind':13 'indenfor':6 'kunn':3 'nu':7 'sat':12 'semi':5 'være':4 '🍁🦔':14
191	59	0.8794326241134752	26	'-01':3 '-10':2 '-29':6 '-48':5 '1':9 '16':4 '2024':1 'dalrteqoljm':8 'utc':7	'-01':3A '-10':2A '-29':6A '-48':5A '1':9A '16':4A '2024':1A 'dalrteqoljm':8A 'utc':7A	
196	61	0.8819444444444444	26	'-10':2 '-16':3 '-52':5,6 '-7':9 '1':10 '14':4 '2024':1 'dbmgzubib':8 'utc':7	'-10':2A '-16':3A '-52':5A,6A '-7':9A '1':10A '14':4A '2024':1A 'dbmgzubib':8A 'utc':7A	
197	62	0.8831615120274915	26	'-10':2 '-16':3 '-52':5,6 '-7':9 '14':4 '2':10 '2024':1 'dbmgzubib':8 'utc':7	'-10':2A '-16':3A '-52':5A,6A '-7':9A '14':4A '2':10A '2024':1A 'dbmgzubib':8A 'utc':7A	
198	63	0.8843537414965986	26	'-10':2 '-16':3 '-52':5,6 '-7':9 '14':4 '2024':1 '3':10 'dbmgzubib':8 'utc':7	'-10':2A '-16':3A '-52':5A,6A '-7':9A '14':4A '2024':1A '3':10A 'dbmgzubib':8A 'utc':7A	
45	6	1.6589285714285715	58	'45m²':26 'aftentimer':39 'belysning':37 'blev':47 'brugt':41 'budget':53 'bygget':13 'en':14 'fantastisk':15 'færdiggjort':48 'grill':28 'har':12 'i':32 'indbygget':27 'integreret':18 'kogezone':30 'køkken':5,8,20 'led':36 'led-belysning':35 'lærketræ':23,42 'materialer':40 'med':17 'natursten':45 'og':3,9,29,51 'omfatter':22 'opbevaringsløsninger':31 'projektet':21,46 'på':25 'rustfrit':43 'smukt':6 'stål':44 'terrasse':2,10,24 'tiden':50 'til':38,49 'træ':1,34 'træterrasse':16 'udendørs':4,7,19 'vejrbestandigt':33 'vi':11 'within':52	'køkken':5B 'og':3B 'terrass':2B 'træ':1B 'udendør':4B	'45m²':21 'aftentim':34 'belysn':32 'blev':42 'brugt':36 'budget':48 'bygget':8 'en':9 'famili':56 'fantastisk':10 'færdiggjort':43 'grill':23 'hansen':57 'har':7 'indbygget':22 'integreret':13 'koekken':60 'kogezon':25 'køkken':3,15 'led':31 'led-belysn':30 'lærketræ':18,37,49 'material':35 'med':12 'natursten':40,52 'nordsjælland':55 'og':4,24,46 'omfatt':17 'opbevaringsløsning':26 'privat':53 'projektet':16,41 'på':20 'rustfrit':38,50 'smukt':1 'stål':39,51 'terrass':5,19,59 'tiden':45 'til':33,44 'traeterr':61 'træ':29 'træterrass':11 'udendo':58 'udendør':2,14 'vejrbestandigt':28 'vi':6 'villa':54 'within':47
46	7	2.7648809523809526	58	'1920':14 'af':6,11,23,27,36 'arkitektur':21 'badeværelser':30 'den':19 'eksempel':41 'energioptimering':31 'erne':15 'et':39 'familierum':38 'for':18 'forenes':49 'fra':13 'harmonisk':50 'historie':44 'historisk':7 'hvordan':43 'i':3 'kan':48 'komfort':47 'komplet':9 'københavn':4 'køkken':28 'med':16,32 'moderne':37,46 'modernisering':26 'nye':33 'og':29,45 'oprindelige':20 'originale':24 'på':42 'renovering':2,10 'respekt':17 'restaurering':22 'smukt':40 'tilbygning':35 'totalrenovering':5 'trægulve':25 'villa':1,8,12 'vinduer':34	'københavn':4B 'renov':2B 'villa':1B	'1920':10 'af':2,7,19,23,32 'arkitektur':17 'badeværels':26 'den':15 'eg':47 'eksempel':37 'energioptim':27 'ern':11 'et':35 'familierum':34 'foren':45 'fra':9 'glas':49 'harmonisk':46 'histori':40 'historisk':3,57 'hvordan':39 'indr':51 'kan':44 'koebenhavn':58 'komfort':43 'komplet':5 'kund':54 'københavn':52 'køkken':24 'marmor':48 'med':12,28 'modern':33,42 'modernis':22 'nye':29 'og':25,41 'oprindelig':16 'original':20 'privat':53 'på':38 'renov':6,55 'respekt':13 'restaur':18 'smukt':36 'tegl':50 'tilbygn':31 'totalrenov':1 'trægulv':21 'villa':4,8,56 'vinduer':30
47	8	2.7648809523809526	58	'af':33 'alle':29 'behov':19 'belysning':39 'bordplade':25 'bygget':10 'både':44 'corian':24 'der':14 'designet':8 'efter':6 'eg':21 'er':43 'et':11 'funktionelt':45 'hvidevarer':32 'håndlavet':4 'højder':30 'højeste':34 'i':28 'installation':3 'integrerede':31 'kundens':18 'kvalitet':35 'køkken':2,5,13 'køkkenet':42 'køkkenø':22 'led':38 'led-belysning':37 'massiv':20 'med':23 'mål':7 'og':9,46 'passer':15 'perfekt':16 'skabe':27,41 'skjult':36 'skræddersyede':26 'skræddersyet':1 'smukt':48 'til':17 'under':40 'unikt':12 'æstetisk':47	'instal':3B 'køkken':2B 'skræddersyet':1B	'af':30 'all':26 'behov':16 'belysn':36 'bordplad':22 'bygget':7 'både':41 'corian':21,48 'der':11 'designet':5 'efter':3 'eg':18,47 'er':40 'et':8 'frederiksberg':51 'funktionelt':42 'hvidevar':29 'håndlavet':1 'højder':27 'højest':31 'instal':54 'integrered':28 'koekken':52 'kunden':15 'kvalitet':32 'køkken':2,10 'køkkenet':39 'køkkenø':19 'led':35 'led-belysn':34 'massiv':17,46 'med':20 'mål':4 'og':6,43 'passer':12 'perfekt':13 'rustfrit':49 'skabe':24,38 'skjult':33 'skreddersyet':53 'skræddersyed':23 'smukt':45 'stål':50 'til':14 'unikt':9 'æstetisk':44
208	32	0.5119047619047619	58	'at':13 'der':22,26 'det':11,14 'eller':5 'en':1 'er':10 'gennemføring':4,8 'heldigt':12 'ikke':23 'ind':25 'indefra':18 'kan':15 'kommer':21 'korrekt':17 'laves':16 'længere':27 'mangel':6 'på':7 'så':9,20 'uheldig':2 'undertags':3 'vand':24 '🥸':28 '🦔':19	'det':11B,14B 'eller':5B 'en':1B 'er':10B 'gennemfør':4B,8B 'heldigt':12B 'indefra':18B 'kan':15B 'korrekt':17B 'lave':16B 'mangel':6B 'på':7B 'så':9B 'uheldig':2B 'undertag':3B '🦔':19B	'der':3,7 'ikk':4 'ind':6 'kommer':2 'længere':8 'så':1 'vand':5 '🥸':9
212	69	0.9109014675052411	26	'-08':5 '-11':2 '-19':3 '-55':6 '08':4 '1':9 '2024':1 'dci7mhrouba':8 'utc':7	'-08':5A '-11':2A '-19':3A '-55':6A '08':4A '1':9A '2024':1A 'dci7mhrouba':8A 'utc':7A	
213	70	0.9117341640706127	26	'-08':5 '-11':2 '-19':3 '-55':6 '08':4 '2':9 '2024':1 'dci7mhrouba':8 'utc':7	'-08':5A '-11':2A '-19':3A '-55':6A '08':4A '2':9A '2024':1A 'dci7mhrouba':8A 'utc':7A	
214	33	0.5512345679012346	58	'af':2 'at':6 'dejligt':5 'det':12 'ellers':13 'et':8 'finde':7 'grå':15 'hul':10 'i':11 'lille':9 'meget':14 'punkteret':3 'rude':4 'udskiftning':1 'vejr':16 '🥸':17	'af':2B 'dejligt':5B 'det':12B 'eller':13B 'et':8B 'find':7B 'grå':15B 'hul':10B 'lill':9B 'meget':14B 'punkteret':3B 'rude':4B 'udskiftn':1B 'vejr':16B '🥸':17B	
218	71	0.9194699286442407	26	'-12':2 '-13':5 '-15':3 '-25':6 '1':9 '12':4 '2024':1 'ddmt2cbih9o':8 'utc':7	'-12':2A '-13':5A '-15':3A '-25':6A '1':9A '12':4A '2024':1A 'ddmt2cbih9o':8A 'utc':7A	
219	72	0.9202020202020201	26	'-12':2 '-13':5 '-15':3 '-25':6 '12':4 '2':9 '2024':1 'ddmt2cbih9o':8 'utc':7	'-12':2A '-13':5A '-15':3A '-25':6A '12':4A '2':9A '2024':1A 'ddmt2cbih9o':8A 'utc':7A	
223	73	0.920920920920921	26	'-01':2 '-20':3 '-21':5 '-48':6 '1':9 '19':4 '2025':1 'dfdxfdbi92z':8 'utc':7	'-01':2A '-20':3A '-21':5A '-48':6A '1':9A '19':4A '2025':1A 'dfdxfdbi92z':8A 'utc':7A	
224	74	0.9216269841269842	26	'-01':2 '-20':3 '-21':5 '-48':6 '19':4 '2':9 '2025':1 'dfdxfdbi92z':8 'utc':7	'-01':2A '-20':3A '-21':5A '-48':6A '19':4A '2':9A '2025':1A 'dfdxfdbi92z':8A 'utc':7A	
48	9	4.147321428571429	58	'af':7,28 'badekar':14 'badeværelse':1,4,9,25 'der':26 'et':21 'fliser':12 'fritstående':13 'fuldstændig':5 'italienske':10 'komfort':31 'lignende':24 'luksuriøst':3 'luksus':29 'marmor':11 'master':8 'med':16 'møbel':20 'og':30 'oser':27 'regnbruser':15 'renovering':2,6 'skræddersyet':18 'spa':23 'spa-lignende':22 'termostat':17 'vask':19	'badeværels':1B 'renov':2B	'af':5,26 'badekar':12 'badevaerels':34 'badeværels':2,7,23 'der':24 'et':19 'fliser':10 'fritståend':11 'fuldstændig':3 'gentoft':33 'glas':32 'italiensk':8 'komfort':29 'lignend':22 'luksurio':36 'luksuriøst':1 'luksus':27 'marmor':9,30 'master':6 'med':14 'mess':31 'møbel':18 'og':28 'oser':25 'regnbrus':13 'renov':4,35 'skræddersyet':16 'spa':21 'spa-lignend':20 'termostat':15 'vask':17
49	10	4.147321428571429	58	'af':9 'arbejdsmiljø':38 'byggeriet':19 'bæredygtige':15 'bæredygtighed':7 'der':31 'energieffektiv':25 'erhvervsprojekt':3 'et':34 'fleksible':29 'fokus':5 'for':12,22 'glaspartier':21 'hele':18 'i':17 'kan':32 'kontorbygning':2,11 'kontorrum':30 'lys':24 'materialer':16 'med':4 'miljøvenligt':37 'mindre':13 'moderne':1,10,35 'naturligt':23 'og':27,36 'opførelse':8 'på':6 'store':20 'tilpasses':33 'varme':26 'ventilationsystem':28 'virksomhed':14	'kontorbygn':2B 'modern':1B	'af':7 'ap':44 'arbejdsmiljø':36 'baeredygtig':48 'beton':39 'byggeriet':17 'bæredygtig':13 'bæredygtigh':5 'der':29 'energieffektiv':23 'erhverv':47 'erhvervsområd':41 'erhvervsprojekt':1 'et':32 'fleksibl':27 'fokus':3 'glas':38 'glasparti':19 'glostrup':42 'hele':16 'kan':30 'kontor':45 'kontorbygn':9 'kontorrum':28 'lys':22 'material':14 'med':2 'miljøvenligt':35 'mindr':11 'modern':8,33,46 'naturligt':21 'og':25,34 'opførels':6 'på':4 'store':18 'stål':40 'techstart':43 'tilpass':31 'træ':37 'varm':24 'ventilationsystem':26 'virksomh':12
\.


--
-- TOC entry 4715 (class 0 OID 27739)
-- Dependencies: 340
-- Data for Name: wagtailsearchpromotions_query; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailsearchpromotions_query (id, query_string) FROM stdin;
1	project
2	hej
\.


--
-- TOC entry 4717 (class 0 OID 27747)
-- Dependencies: 342
-- Data for Name: wagtailsearchpromotions_querydailyhits; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailsearchpromotions_querydailyhits (id, date, hits, query_id) FROM stdin;
1	2025-09-11	6	1
2	2025-09-11	1	2
\.


--
-- TOC entry 4713 (class 0 OID 27719)
-- Dependencies: 338
-- Data for Name: wagtailsearchpromotions_searchpromotion; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailsearchpromotions_searchpromotion (id, sort_order, description, page_id, query_id, external_link_text, external_link_url) FROM stdin;
\.


--
-- TOC entry 4706 (class 0 OID 27642)
-- Dependencies: 331
-- Data for Name: wagtailusers_userprofile; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailusers_userprofile (id, submitted_notifications, approved_notifications, rejected_notifications, user_id, preferred_language, current_time_zone, avatar, updated_comments_notifications, dismissibles, theme, density, contrast, keyboard_shortcuts) FROM stdin;
\.


--
-- TOC entry 4723 (class 0 OID 0)
-- Dependencies: 220
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 2, true);


--
-- TOC entry 4724 (class 0 OID 0)
-- Dependencies: 222
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 18, true);


--
-- TOC entry 4725 (class 0 OID 0)
-- Dependencies: 218
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 254, true);


--
-- TOC entry 4726 (class 0 OID 0)
-- Dependencies: 226
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- TOC entry 4727 (class 0 OID 0)
-- Dependencies: 224
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- TOC entry 4728 (class 0 OID 0)
-- Dependencies: 228
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 4729 (class 0 OID 0)
-- Dependencies: 242
-- Name: contacts_contactsubmission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.contacts_contactsubmission_id_seq', 1, false);


--
-- TOC entry 4730 (class 0 OID 0)
-- Dependencies: 230
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- TOC entry 4731 (class 0 OID 0)
-- Dependencies: 216
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 63, true);


--
-- TOC entry 4732 (class 0 OID 0)
-- Dependencies: 214
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 250, true);


--
-- TOC entry 4733 (class 0 OID 0)
-- Dependencies: 314
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_site_id_seq', 1, true);


--
-- TOC entry 4734 (class 0 OID 0)
-- Dependencies: 303
-- Name: pages_logo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pages_logo_id_seq', 1, false);


--
-- TOC entry 4735 (class 0 OID 0)
-- Dependencies: 299
-- Name: pages_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pages_service_id_seq', 1, false);


--
-- TOC entry 4736 (class 0 OID 0)
-- Dependencies: 305
-- Name: pages_sitesettings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pages_sitesettings_id_seq', 1, true);


--
-- TOC entry 4737 (class 0 OID 0)
-- Dependencies: 301
-- Name: pages_testimonial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pages_testimonial_id_seq', 1, false);


--
-- TOC entry 4738 (class 0 OID 0)
-- Dependencies: 307
-- Name: projects_project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.projects_project_id_seq', 14, true);


--
-- TOC entry 4739 (class 0 OID 0)
-- Dependencies: 311
-- Name: projects_projectimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.projects_projectimage_id_seq', 14, true);


--
-- TOC entry 4740 (class 0 OID 0)
-- Dependencies: 333
-- Name: projects_projectpageimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.projects_projectpageimage_id_seq', 60, true);


--
-- TOC entry 4741 (class 0 OID 0)
-- Dependencies: 335
-- Name: projects_projectpagetag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.projects_projectpagetag_id_seq', 18, true);


--
-- TOC entry 4742 (class 0 OID 0)
-- Dependencies: 309
-- Name: projects_projecttag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.projects_projecttag_id_seq', 1, false);


--
-- TOC entry 4743 (class 0 OID 0)
-- Dependencies: 287
-- Name: taggit_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.taggit_tag_id_seq', 16, true);


--
-- TOC entry 4744 (class 0 OID 0)
-- Dependencies: 289
-- Name: taggit_taggeditem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.taggit_taggeditem_id_seq', 1, false);


--
-- TOC entry 4745 (class 0 OID 0)
-- Dependencies: 316
-- Name: wagtailadmin_admin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailadmin_admin_id_seq', 1, false);


--
-- TOC entry 4746 (class 0 OID 0)
-- Dependencies: 318
-- Name: wagtailadmin_editingsession_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailadmin_editingsession_id_seq', 5, true);


--
-- TOC entry 4747 (class 0 OID 0)
-- Dependencies: 244
-- Name: wagtailcore_collection_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_collection_id_seq', 1, true);


--
-- TOC entry 4748 (class 0 OID 0)
-- Dependencies: 252
-- Name: wagtailcore_collectionviewrestriction_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_collectionviewrestriction_groups_id_seq', 1, false);


--
-- TOC entry 4749 (class 0 OID 0)
-- Dependencies: 250
-- Name: wagtailcore_collectionviewrestriction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_collectionviewrestriction_id_seq', 1, false);


--
-- TOC entry 4750 (class 0 OID 0)
-- Dependencies: 272
-- Name: wagtailcore_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_comment_id_seq', 1, false);


--
-- TOC entry 4751 (class 0 OID 0)
-- Dependencies: 274
-- Name: wagtailcore_commentreply_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_commentreply_id_seq', 1, false);


--
-- TOC entry 4752 (class 0 OID 0)
-- Dependencies: 266
-- Name: wagtailcore_groupapprovaltask_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_groupapprovaltask_groups_id_seq', 1, true);


--
-- TOC entry 4753 (class 0 OID 0)
-- Dependencies: 246
-- Name: wagtailcore_groupcollectionpermission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_groupcollectionpermission_id_seq', 12, true);


--
-- TOC entry 4754 (class 0 OID 0)
-- Dependencies: 234
-- Name: wagtailcore_grouppagepermission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_grouppagepermission_id_seq', 7, true);


--
-- TOC entry 4755 (class 0 OID 0)
-- Dependencies: 285
-- Name: wagtailcore_groupsitepermission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_groupsitepermission_id_seq', 1, false);


--
-- TOC entry 4756 (class 0 OID 0)
-- Dependencies: 270
-- Name: wagtailcore_locale_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_locale_id_seq', 1, true);


--
-- TOC entry 4757 (class 0 OID 0)
-- Dependencies: 278
-- Name: wagtailcore_modellogentry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_modellogentry_id_seq', 1, true);


--
-- TOC entry 4758 (class 0 OID 0)
-- Dependencies: 232
-- Name: wagtailcore_page_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_page_id_seq', 33, true);


--
-- TOC entry 4759 (class 0 OID 0)
-- Dependencies: 268
-- Name: wagtailcore_pagelogentry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pagelogentry_id_seq', 65, true);


--
-- TOC entry 4760 (class 0 OID 0)
-- Dependencies: 236
-- Name: wagtailcore_pagerevision_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pagerevision_id_seq', 31, true);


--
-- TOC entry 4761 (class 0 OID 0)
-- Dependencies: 276
-- Name: wagtailcore_pagesubscription_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pagesubscription_id_seq', 1, true);


--
-- TOC entry 4762 (class 0 OID 0)
-- Dependencies: 248
-- Name: wagtailcore_pageviewrestriction_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pageviewrestriction_groups_id_seq', 1, false);


--
-- TOC entry 4763 (class 0 OID 0)
-- Dependencies: 238
-- Name: wagtailcore_pageviewrestriction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pageviewrestriction_id_seq', 1, false);


--
-- TOC entry 4764 (class 0 OID 0)
-- Dependencies: 280
-- Name: wagtailcore_referenceindex_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_referenceindex_id_seq', 169, true);


--
-- TOC entry 4765 (class 0 OID 0)
-- Dependencies: 240
-- Name: wagtailcore_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_site_id_seq', 1, true);


--
-- TOC entry 4766 (class 0 OID 0)
-- Dependencies: 254
-- Name: wagtailcore_task_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_task_id_seq', 1, true);


--
-- TOC entry 4767 (class 0 OID 0)
-- Dependencies: 256
-- Name: wagtailcore_taskstate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_taskstate_id_seq', 1, false);


--
-- TOC entry 4768 (class 0 OID 0)
-- Dependencies: 283
-- Name: wagtailcore_uploadedfile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_uploadedfile_id_seq', 1, false);


--
-- TOC entry 4769 (class 0 OID 0)
-- Dependencies: 258
-- Name: wagtailcore_workflow_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_workflow_id_seq', 1, true);


--
-- TOC entry 4770 (class 0 OID 0)
-- Dependencies: 261
-- Name: wagtailcore_workflowstate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_workflowstate_id_seq', 1, false);


--
-- TOC entry 4771 (class 0 OID 0)
-- Dependencies: 264
-- Name: wagtailcore_workflowtask_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_workflowtask_id_seq', 1, true);


--
-- TOC entry 4772 (class 0 OID 0)
-- Dependencies: 320
-- Name: wagtaildocs_document_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtaildocs_document_id_seq', 1, false);


--
-- TOC entry 4773 (class 0 OID 0)
-- Dependencies: 322
-- Name: wagtailembeds_embed_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailembeds_embed_id_seq', 1, false);


--
-- TOC entry 4774 (class 0 OID 0)
-- Dependencies: 324
-- Name: wagtailforms_formsubmission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailforms_formsubmission_id_seq', 1, false);


--
-- TOC entry 4775 (class 0 OID 0)
-- Dependencies: 291
-- Name: wagtailimages_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailimages_image_id_seq', 74, true);


--
-- TOC entry 4776 (class 0 OID 0)
-- Dependencies: 293
-- Name: wagtailimages_rendition_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailimages_rendition_id_seq', 39, true);


--
-- TOC entry 4777 (class 0 OID 0)
-- Dependencies: 326
-- Name: wagtailredirects_redirect_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailredirects_redirect_id_seq', 1, false);


--
-- TOC entry 4778 (class 0 OID 0)
-- Dependencies: 328
-- Name: wagtailsearch_indexentry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailsearch_indexentry_id_seq', 229, true);


--
-- TOC entry 4779 (class 0 OID 0)
-- Dependencies: 339
-- Name: wagtailsearchpromotions_query_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailsearchpromotions_query_id_seq', 2, true);


--
-- TOC entry 4780 (class 0 OID 0)
-- Dependencies: 341
-- Name: wagtailsearchpromotions_querydailyhits_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailsearchpromotions_querydailyhits_id_seq', 2, true);


--
-- TOC entry 4781 (class 0 OID 0)
-- Dependencies: 337
-- Name: wagtailsearchpromotions_searchpromotion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailsearchpromotions_searchpromotion_id_seq', 1, false);


--
-- TOC entry 4782 (class 0 OID 0)
-- Dependencies: 330
-- Name: wagtailusers_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailusers_userprofile_id_seq', 1, false);


--
-- TOC entry 3999 (class 2606 OID 26386)
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 4004 (class 2606 OID 26317)
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- TOC entry 4007 (class 2606 OID 26286)
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 4001 (class 2606 OID 26278)
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 3994 (class 2606 OID 26308)
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- TOC entry 3996 (class 2606 OID 26272)
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 4015 (class 2606 OID 26300)
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 4018 (class 2606 OID 26332)
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- TOC entry 4009 (class 2606 OID 26292)
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- TOC entry 4021 (class 2606 OID 26306)
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 4024 (class 2606 OID 26346)
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- TOC entry 4012 (class 2606 OID 26381)
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- TOC entry 4073 (class 2606 OID 26492)
-- Name: contacts_contactsubmission contacts_contactsubmission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contacts_contactsubmission
    ADD CONSTRAINT contacts_contactsubmission_pkey PRIMARY KEY (id);


--
-- TOC entry 4027 (class 2606 OID 26367)
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 3989 (class 2606 OID 26266)
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- TOC entry 3991 (class 2606 OID 26264)
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 3987 (class 2606 OID 26258)
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 4271 (class 2606 OID 27435)
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 4275 (class 2606 OID 27445)
-- Name: django_site django_site_domain_a2e37b91_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE (domain);


--
-- TOC entry 4277 (class 2606 OID 27443)
-- Name: django_site django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- TOC entry 4238 (class 2606 OID 27252)
-- Name: pages_contactpage pages_contactpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_contactpage
    ADD CONSTRAINT pages_contactpage_pkey PRIMARY KEY (page_ptr_id);


--
-- TOC entry 4240 (class 2606 OID 27259)
-- Name: pages_gallerypage pages_gallerypage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_gallerypage
    ADD CONSTRAINT pages_gallerypage_pkey PRIMARY KEY (page_ptr_id);


--
-- TOC entry 4236 (class 2606 OID 27240)
-- Name: pages_homepage pages_homepage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_homepage
    ADD CONSTRAINT pages_homepage_pkey PRIMARY KEY (page_ptr_id);


--
-- TOC entry 4249 (class 2606 OID 27298)
-- Name: pages_logo pages_logo_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_logo
    ADD CONSTRAINT pages_logo_pkey PRIMARY KEY (id);


--
-- TOC entry 4242 (class 2606 OID 27276)
-- Name: pages_modularpage pages_modularpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_modularpage
    ADD CONSTRAINT pages_modularpage_pkey PRIMARY KEY (page_ptr_id);


--
-- TOC entry 4244 (class 2606 OID 27284)
-- Name: pages_service pages_service_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_service
    ADD CONSTRAINT pages_service_pkey PRIMARY KEY (id);


--
-- TOC entry 4253 (class 2606 OID 27330)
-- Name: pages_sitesettings pages_sitesettings_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_sitesettings
    ADD CONSTRAINT pages_sitesettings_pkey PRIMARY KEY (id);


--
-- TOC entry 4255 (class 2606 OID 27332)
-- Name: pages_sitesettings pages_sitesettings_site_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_sitesettings
    ADD CONSTRAINT pages_sitesettings_site_id_key UNIQUE (site_id);


--
-- TOC entry 4246 (class 2606 OID 27292)
-- Name: pages_testimonial pages_testimonial_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_testimonial
    ADD CONSTRAINT pages_testimonial_pkey PRIMARY KEY (id);


--
-- TOC entry 4257 (class 2606 OID 27377)
-- Name: projects_project projects_project_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_project
    ADD CONSTRAINT projects_project_pkey PRIMARY KEY (id);


--
-- TOC entry 4260 (class 2606 OID 27379)
-- Name: projects_project projects_project_slug_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_project
    ADD CONSTRAINT projects_project_slug_key UNIQUE (slug);


--
-- TOC entry 4267 (class 2606 OID 27416)
-- Name: projects_projectimage projects_projectimage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectimage
    ADD CONSTRAINT projects_projectimage_pkey PRIMARY KEY (id);


--
-- TOC entry 4319 (class 2606 OID 27674)
-- Name: projects_projectpage projects_projectpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpage
    ADD CONSTRAINT projects_projectpage_pkey PRIMARY KEY (page_ptr_id);


--
-- TOC entry 4322 (class 2606 OID 27682)
-- Name: projects_projectpageimage projects_projectpageimage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpageimage
    ADD CONSTRAINT projects_projectpageimage_pkey PRIMARY KEY (id);


--
-- TOC entry 4326 (class 2606 OID 27688)
-- Name: projects_projectpagetag projects_projectpagetag_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpagetag
    ADD CONSTRAINT projects_projectpagetag_pkey PRIMARY KEY (id);


--
-- TOC entry 4263 (class 2606 OID 27385)
-- Name: projects_projecttag projects_projecttag_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projecttag
    ADD CONSTRAINT projects_projecttag_pkey PRIMARY KEY (id);


--
-- TOC entry 4207 (class 2606 OID 27153)
-- Name: taggit_tag taggit_tag_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_tag
    ADD CONSTRAINT taggit_tag_name_key UNIQUE (name);


--
-- TOC entry 4209 (class 2606 OID 27151)
-- Name: taggit_tag taggit_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_tag
    ADD CONSTRAINT taggit_tag_pkey PRIMARY KEY (id);


--
-- TOC entry 4212 (class 2606 OID 27155)
-- Name: taggit_tag taggit_tag_slug_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_tag
    ADD CONSTRAINT taggit_tag_slug_key UNIQUE (slug);


--
-- TOC entry 4216 (class 2606 OID 27369)
-- Name: taggit_taggeditem taggit_taggeditem_content_type_id_object_id_tag_id_4bb97a8e_uni; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_content_type_id_object_id_tag_id_4bb97a8e_uni UNIQUE (content_type_id, object_id, tag_id);


--
-- TOC entry 4219 (class 2606 OID 27161)
-- Name: taggit_taggeditem taggit_taggeditem_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_pkey PRIMARY KEY (id);


--
-- TOC entry 4047 (class 2606 OID 27094)
-- Name: wagtailcore_grouppagepermission unique_permission; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission
    ADD CONSTRAINT unique_permission UNIQUE (group_id, page_id, permission_id);


--
-- TOC entry 4279 (class 2606 OID 27452)
-- Name: wagtailadmin_admin wagtailadmin_admin_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailadmin_admin
    ADD CONSTRAINT wagtailadmin_admin_pkey PRIMARY KEY (id);


--
-- TOC entry 4283 (class 2606 OID 27458)
-- Name: wagtailadmin_editingsession wagtailadmin_editingsession_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailadmin_editingsession
    ADD CONSTRAINT wagtailadmin_editingsession_pkey PRIMARY KEY (id);


--
-- TOC entry 4077 (class 2606 OID 26543)
-- Name: wagtailcore_collection wagtailcore_collection_path_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collection
    ADD CONSTRAINT wagtailcore_collection_path_key UNIQUE (path);


--
-- TOC entry 4079 (class 2606 OID 26512)
-- Name: wagtailcore_collection wagtailcore_collection_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collection
    ADD CONSTRAINT wagtailcore_collection_pkey PRIMARY KEY (id);


--
-- TOC entry 4097 (class 2606 OID 26592)
-- Name: wagtailcore_collectionviewrestriction_groups wagtailcore_collectionvi_collectionviewrestrictio_988995ae_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction_groups
    ADD CONSTRAINT wagtailcore_collectionvi_collectionviewrestrictio_988995ae_uniq UNIQUE (collectionviewrestriction_id, group_id);


--
-- TOC entry 4101 (class 2606 OID 26584)
-- Name: wagtailcore_collectionviewrestriction_groups wagtailcore_collectionviewrestriction_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction_groups
    ADD CONSTRAINT wagtailcore_collectionviewrestriction_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 4095 (class 2606 OID 26578)
-- Name: wagtailcore_collectionviewrestriction wagtailcore_collectionviewrestriction_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction
    ADD CONSTRAINT wagtailcore_collectionviewrestriction_pkey PRIMARY KEY (id);


--
-- TOC entry 4159 (class 2606 OID 26827)
-- Name: wagtailcore_comment wagtailcore_comment_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_comment
    ADD CONSTRAINT wagtailcore_comment_pkey PRIMARY KEY (id);


--
-- TOC entry 4165 (class 2606 OID 26835)
-- Name: wagtailcore_commentreply wagtailcore_commentreply_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_commentreply
    ADD CONSTRAINT wagtailcore_commentreply_pkey PRIMARY KEY (id);


--
-- TOC entry 4137 (class 2606 OID 26747)
-- Name: wagtailcore_groupapprovaltask_groups wagtailcore_groupapprova_groupapprovaltask_id_gro_bb5ee7eb_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupapprovaltask_groups
    ADD CONSTRAINT wagtailcore_groupapprova_groupapprovaltask_id_gro_bb5ee7eb_uniq UNIQUE (groupapprovaltask_id, group_id);


--
-- TOC entry 4141 (class 2606 OID 26667)
-- Name: wagtailcore_groupapprovaltask_groups wagtailcore_groupapprovaltask_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupapprovaltask_groups
    ADD CONSTRAINT wagtailcore_groupapprovaltask_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 4115 (class 2606 OID 26636)
-- Name: wagtailcore_groupapprovaltask wagtailcore_groupapprovaltask_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupapprovaltask
    ADD CONSTRAINT wagtailcore_groupapprovaltask_pkey PRIMARY KEY (task_ptr_id);


--
-- TOC entry 4081 (class 2606 OID 26523)
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcollect_group_id_collection_id_p_a21cefe9_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcollect_group_id_collection_id_p_a21cefe9_uniq UNIQUE (group_id, collection_id, permission_id);


--
-- TOC entry 4086 (class 2606 OID 26521)
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcollectionpermission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcollectionpermission_pkey PRIMARY KEY (id);


--
-- TOC entry 4052 (class 2606 OID 26407)
-- Name: wagtailcore_grouppagepermission wagtailcore_grouppagepermission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppagepermission_pkey PRIMARY KEY (id);


--
-- TOC entry 4199 (class 2606 OID 27127)
-- Name: wagtailcore_groupsitepermission wagtailcore_groupsiteper_group_id_site_id_permiss_a58ee30d_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupsitepermission
    ADD CONSTRAINT wagtailcore_groupsiteper_group_id_site_id_permiss_a58ee30d_uniq UNIQUE (group_id, site_id, permission_id);


--
-- TOC entry 4203 (class 2606 OID 27125)
-- Name: wagtailcore_groupsitepermission wagtailcore_groupsitepermission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupsitepermission
    ADD CONSTRAINT wagtailcore_groupsitepermission_pkey PRIMARY KEY (id);


--
-- TOC entry 4154 (class 2606 OID 26797)
-- Name: wagtailcore_locale wagtailcore_locale_language_code_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_locale
    ADD CONSTRAINT wagtailcore_locale_language_code_key UNIQUE (language_code);


--
-- TOC entry 4156 (class 2606 OID 26795)
-- Name: wagtailcore_locale wagtailcore_locale_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_locale
    ADD CONSTRAINT wagtailcore_locale_pkey PRIMARY KEY (id);


--
-- TOC entry 4180 (class 2606 OID 26899)
-- Name: wagtailcore_modellogentry wagtailcore_modellogentry_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_modellogentry
    ADD CONSTRAINT wagtailcore_modellogentry_pkey PRIMARY KEY (id);


--
-- TOC entry 4039 (class 2606 OID 26401)
-- Name: wagtailcore_page wagtailcore_page_path_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_path_key UNIQUE (path);


--
-- TOC entry 4041 (class 2606 OID 26397)
-- Name: wagtailcore_page wagtailcore_page_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_pkey PRIMARY KEY (id);


--
-- TOC entry 4045 (class 2606 OID 26805)
-- Name: wagtailcore_page wagtailcore_page_translation_key_locale_id_9b041bad_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_translation_key_locale_id_9b041bad_uniq UNIQUE (translation_key, locale_id);


--
-- TOC entry 4148 (class 2606 OID 26777)
-- Name: wagtailcore_pagelogentry wagtailcore_pagelogentry_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagelogentry
    ADD CONSTRAINT wagtailcore_pagelogentry_pkey PRIMARY KEY (id);


--
-- TOC entry 4058 (class 2606 OID 26417)
-- Name: wagtailcore_revision wagtailcore_pagerevision_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_revision
    ADD CONSTRAINT wagtailcore_pagerevision_pkey PRIMARY KEY (id);


--
-- TOC entry 4169 (class 2606 OID 26879)
-- Name: wagtailcore_pagesubscription wagtailcore_pagesubscription_page_id_user_id_0cef73ed_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagesubscription
    ADD CONSTRAINT wagtailcore_pagesubscription_page_id_user_id_0cef73ed_uniq UNIQUE (page_id, user_id);


--
-- TOC entry 4171 (class 2606 OID 26841)
-- Name: wagtailcore_pagesubscription wagtailcore_pagesubscription_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagesubscription
    ADD CONSTRAINT wagtailcore_pagesubscription_pkey PRIMARY KEY (id);


--
-- TOC entry 4088 (class 2606 OID 26554)
-- Name: wagtailcore_pageviewrestriction_groups wagtailcore_pageviewrest_pageviewrestriction_id_g_d23f80bb_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction_groups
    ADD CONSTRAINT wagtailcore_pageviewrest_pageviewrestriction_id_g_d23f80bb_uniq UNIQUE (pageviewrestriction_id, group_id);


--
-- TOC entry 4092 (class 2606 OID 26551)
-- Name: wagtailcore_pageviewrestriction_groups wagtailcore_pageviewrestriction_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction_groups
    ADD CONSTRAINT wagtailcore_pageviewrestriction_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 4064 (class 2606 OID 26423)
-- Name: wagtailcore_pageviewrestriction wagtailcore_pageviewrestriction_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction
    ADD CONSTRAINT wagtailcore_pageviewrestriction_pkey PRIMARY KEY (id);


--
-- TOC entry 4185 (class 2606 OID 27014)
-- Name: wagtailcore_referenceindex wagtailcore_referenceind_base_content_type_id_obj_9e6ccd6a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_referenceindex
    ADD CONSTRAINT wagtailcore_referenceind_base_content_type_id_obj_9e6ccd6a_uniq UNIQUE (base_content_type_id, object_id, to_content_type_id, to_object_id, content_path_hash);


--
-- TOC entry 4189 (class 2606 OID 27012)
-- Name: wagtailcore_referenceindex wagtailcore_referenceindex_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_referenceindex
    ADD CONSTRAINT wagtailcore_referenceindex_pkey PRIMARY KEY (id);


--
-- TOC entry 4068 (class 2606 OID 26431)
-- Name: wagtailcore_site wagtailcore_site_hostname_port_2c626d70_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_site
    ADD CONSTRAINT wagtailcore_site_hostname_port_2c626d70_uniq UNIQUE (hostname, port);


--
-- TOC entry 4070 (class 2606 OID 26429)
-- Name: wagtailcore_site wagtailcore_site_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_site
    ADD CONSTRAINT wagtailcore_site_pkey PRIMARY KEY (id);


--
-- TOC entry 4104 (class 2606 OID 26619)
-- Name: wagtailcore_task wagtailcore_task_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_task
    ADD CONSTRAINT wagtailcore_task_pkey PRIMARY KEY (id);


--
-- TOC entry 4109 (class 2606 OID 26625)
-- Name: wagtailcore_taskstate wagtailcore_taskstate_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_taskstate
    ADD CONSTRAINT wagtailcore_taskstate_pkey PRIMARY KEY (id);


--
-- TOC entry 4196 (class 2606 OID 27107)
-- Name: wagtailcore_uploadedfile wagtailcore_uploadedfile_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_uploadedfile
    ADD CONSTRAINT wagtailcore_uploadedfile_pkey PRIMARY KEY (id);


--
-- TOC entry 4113 (class 2606 OID 26631)
-- Name: wagtailcore_workflow wagtailcore_workflow_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflow
    ADD CONSTRAINT wagtailcore_workflow_pkey PRIMARY KEY (id);


--
-- TOC entry 4192 (class 2606 OID 27074)
-- Name: wagtailcore_workflowcontenttype wagtailcore_workflowcontenttype_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowcontenttype
    ADD CONSTRAINT wagtailcore_workflowcontenttype_pkey PRIMARY KEY (content_type_id);


--
-- TOC entry 4128 (class 2606 OID 26649)
-- Name: wagtailcore_workflowpage wagtailcore_workflowpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowpage
    ADD CONSTRAINT wagtailcore_workflowpage_pkey PRIMARY KEY (page_id);


--
-- TOC entry 4120 (class 2606 OID 26644)
-- Name: wagtailcore_workflowstate wagtailcore_workflowstate_current_task_state_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowstate
    ADD CONSTRAINT wagtailcore_workflowstate_current_task_state_id_key UNIQUE (current_task_state_id);


--
-- TOC entry 4122 (class 2606 OID 26642)
-- Name: wagtailcore_workflowstate wagtailcore_workflowstate_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowstate
    ADD CONSTRAINT wagtailcore_workflowstate_pkey PRIMARY KEY (id);


--
-- TOC entry 4131 (class 2606 OID 26660)
-- Name: wagtailcore_workflowtask wagtailcore_workflowtask_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowtask
    ADD CONSTRAINT wagtailcore_workflowtask_pkey PRIMARY KEY (id);


--
-- TOC entry 4135 (class 2606 OID 26733)
-- Name: wagtailcore_workflowtask wagtailcore_workflowtask_workflow_id_task_id_4ec7a62b_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowtask
    ADD CONSTRAINT wagtailcore_workflowtask_workflow_id_task_id_4ec7a62b_uniq UNIQUE (workflow_id, task_id);


--
-- TOC entry 4287 (class 2606 OID 27478)
-- Name: wagtaildocs_document wagtaildocs_document_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtaildocs_document
    ADD CONSTRAINT wagtaildocs_document_pkey PRIMARY KEY (id);


--
-- TOC entry 4292 (class 2606 OID 27525)
-- Name: wagtailembeds_embed wagtailembeds_embed_hash_c9bd8c9a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailembeds_embed
    ADD CONSTRAINT wagtailembeds_embed_hash_c9bd8c9a_uniq UNIQUE (hash);


--
-- TOC entry 4294 (class 2606 OID 27520)
-- Name: wagtailembeds_embed wagtailembeds_embed_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailembeds_embed
    ADD CONSTRAINT wagtailembeds_embed_pkey PRIMARY KEY (id);


--
-- TOC entry 4297 (class 2606 OID 27536)
-- Name: wagtailforms_formsubmission wagtailforms_formsubmission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailforms_formsubmission
    ADD CONSTRAINT wagtailforms_formsubmission_pkey PRIMARY KEY (id);


--
-- TOC entry 4226 (class 2606 OID 27187)
-- Name: wagtailimages_image wagtailimages_image_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_image
    ADD CONSTRAINT wagtailimages_image_pkey PRIMARY KEY (id);


--
-- TOC entry 4232 (class 2606 OID 27195)
-- Name: wagtailimages_rendition wagtailimages_rendition_image_id_filter_spec_foc_323c8fe0_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_rendition
    ADD CONSTRAINT wagtailimages_rendition_image_id_filter_spec_foc_323c8fe0_uniq UNIQUE (image_id, filter_spec, focal_point_key);


--
-- TOC entry 4234 (class 2606 OID 27193)
-- Name: wagtailimages_rendition wagtailimages_rendition_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_rendition
    ADD CONSTRAINT wagtailimages_rendition_pkey PRIMARY KEY (id);


--
-- TOC entry 4301 (class 2606 OID 27573)
-- Name: wagtailredirects_redirect wagtailredirects_redirect_old_path_site_id_783622d7_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailredirects_redirect
    ADD CONSTRAINT wagtailredirects_redirect_old_path_site_id_783622d7_uniq UNIQUE (old_path, site_id);


--
-- TOC entry 4303 (class 2606 OID 27555)
-- Name: wagtailredirects_redirect wagtailredirects_redirect_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailredirects_redirect
    ADD CONSTRAINT wagtailredirects_redirect_pkey PRIMARY KEY (id);


--
-- TOC entry 4311 (class 2606 OID 27629)
-- Name: wagtailsearch_indexentry wagtailsearch_indexentry_content_type_id_object_i_bcd7ba73_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_indexentry
    ADD CONSTRAINT wagtailsearch_indexentry_content_type_id_object_i_bcd7ba73_uniq UNIQUE (content_type_id, object_id);


--
-- TOC entry 4313 (class 2606 OID 27627)
-- Name: wagtailsearch_indexentry wagtailsearch_indexentry_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_indexentry
    ADD CONSTRAINT wagtailsearch_indexentry_pkey PRIMARY KEY (id);


--
-- TOC entry 4338 (class 2606 OID 27754)
-- Name: wagtailsearchpromotions_querydailyhits wagtailsearchpromotions__query_id_date_b9f15515_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_querydailyhits
    ADD CONSTRAINT wagtailsearchpromotions__query_id_date_b9f15515_uniq UNIQUE (query_id, date);


--
-- TOC entry 4333 (class 2606 OID 27743)
-- Name: wagtailsearchpromotions_query wagtailsearchpromotions_query_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_query
    ADD CONSTRAINT wagtailsearchpromotions_query_pkey PRIMARY KEY (id);


--
-- TOC entry 4336 (class 2606 OID 27745)
-- Name: wagtailsearchpromotions_query wagtailsearchpromotions_query_query_string_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_query
    ADD CONSTRAINT wagtailsearchpromotions_query_query_string_key UNIQUE (query_string);


--
-- TOC entry 4340 (class 2606 OID 27751)
-- Name: wagtailsearchpromotions_querydailyhits wagtailsearchpromotions_querydailyhits_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_querydailyhits
    ADD CONSTRAINT wagtailsearchpromotions_querydailyhits_pkey PRIMARY KEY (id);


--
-- TOC entry 4330 (class 2606 OID 27725)
-- Name: wagtailsearchpromotions_searchpromotion wagtailsearchpromotions_searchpromotion_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_searchpromotion
    ADD CONSTRAINT wagtailsearchpromotions_searchpromotion_pkey PRIMARY KEY (id);


--
-- TOC entry 4315 (class 2606 OID 27646)
-- Name: wagtailusers_userprofile wagtailusers_userprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailusers_userprofile
    ADD CONSTRAINT wagtailusers_userprofile_pkey PRIMARY KEY (id);


--
-- TOC entry 4317 (class 2606 OID 27648)
-- Name: wagtailusers_userprofile wagtailusers_userprofile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailusers_userprofile
    ADD CONSTRAINT wagtailusers_userprofile_user_id_key UNIQUE (user_id);


--
-- TOC entry 3997 (class 1259 OID 26387)
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 4002 (class 1259 OID 26328)
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- TOC entry 4005 (class 1259 OID 26329)
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- TOC entry 3992 (class 1259 OID 26314)
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- TOC entry 4013 (class 1259 OID 26344)
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- TOC entry 4016 (class 1259 OID 26343)
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- TOC entry 4019 (class 1259 OID 26358)
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- TOC entry 4022 (class 1259 OID 26357)
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- TOC entry 4010 (class 1259 OID 26382)
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- TOC entry 4053 (class 1259 OID 26984)
-- Name: base_content_object_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX base_content_object_idx ON public.wagtailcore_revision USING btree (base_content_type_id, object_id);


--
-- TOC entry 4074 (class 1259 OID 26498)
-- Name: contacts_contactsubmission_site_id_66673466; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX contacts_contactsubmission_site_id_66673466 ON public.contacts_contactsubmission USING btree (site_id);


--
-- TOC entry 4054 (class 1259 OID 26983)
-- Name: content_object_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX content_object_idx ON public.wagtailcore_revision USING btree (content_type_id, object_id);


--
-- TOC entry 4025 (class 1259 OID 26378)
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- TOC entry 4028 (class 1259 OID 26379)
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- TOC entry 4269 (class 1259 OID 27437)
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- TOC entry 4272 (class 1259 OID 27436)
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 4273 (class 1259 OID 27446)
-- Name: django_site_domain_a2e37b91_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_site_domain_a2e37b91_like ON public.django_site USING btree (domain varchar_pattern_ops);


--
-- TOC entry 4247 (class 1259 OID 27317)
-- Name: pages_logo_image_id_375482c6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX pages_logo_image_id_375482c6 ON public.pages_logo USING btree (image_id);


--
-- TOC entry 4250 (class 1259 OID 27343)
-- Name: pages_sitesettings_logo_id_ef4fb98b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX pages_sitesettings_logo_id_ef4fb98b ON public.pages_sitesettings USING btree (logo_id);


--
-- TOC entry 4251 (class 1259 OID 27355)
-- Name: pages_sitesettings_navigation_cta_page_id_99fb3790; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX pages_sitesettings_navigation_cta_page_id_99fb3790 ON public.pages_sitesettings USING btree (navigation_cta_page_id);


--
-- TOC entry 4258 (class 1259 OID 27391)
-- Name: projects_project_slug_2d50067a_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_project_slug_2d50067a_like ON public.projects_project USING btree (slug varchar_pattern_ops);


--
-- TOC entry 4265 (class 1259 OID 27427)
-- Name: projects_projectimage_image_id_f5a991e8; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projectimage_image_id_f5a991e8 ON public.projects_projectimage USING btree (image_id);


--
-- TOC entry 4268 (class 1259 OID 27428)
-- Name: projects_projectimage_project_id_618ded0e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projectimage_project_id_618ded0e ON public.projects_projectimage USING btree (project_id);


--
-- TOC entry 4320 (class 1259 OID 27704)
-- Name: projects_projectpageimage_image_id_1e7b6756; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projectpageimage_image_id_1e7b6756 ON public.projects_projectpageimage USING btree (image_id);


--
-- TOC entry 4323 (class 1259 OID 27705)
-- Name: projects_projectpageimage_project_page_id_1f3f194b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projectpageimage_project_page_id_1f3f194b ON public.projects_projectpageimage USING btree (project_page_id);


--
-- TOC entry 4324 (class 1259 OID 27716)
-- Name: projects_projectpagetag_content_object_id_b258f16e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projectpagetag_content_object_id_b258f16e ON public.projects_projectpagetag USING btree (content_object_id);


--
-- TOC entry 4327 (class 1259 OID 27717)
-- Name: projects_projectpagetag_tag_id_d11386be; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projectpagetag_tag_id_d11386be ON public.projects_projectpagetag USING btree (tag_id);


--
-- TOC entry 4261 (class 1259 OID 27403)
-- Name: projects_projecttag_content_object_id_ac067992; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projecttag_content_object_id_ac067992 ON public.projects_projecttag USING btree (content_object_id);


--
-- TOC entry 4264 (class 1259 OID 27404)
-- Name: projects_projecttag_tag_id_d49ab282; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projecttag_tag_id_d49ab282 ON public.projects_projecttag USING btree (tag_id);


--
-- TOC entry 4205 (class 1259 OID 27162)
-- Name: taggit_tag_name_58eb2ed9_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_tag_name_58eb2ed9_like ON public.taggit_tag USING btree (name varchar_pattern_ops);


--
-- TOC entry 4210 (class 1259 OID 27163)
-- Name: taggit_tag_slug_6be58b2c_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_tag_slug_6be58b2c_like ON public.taggit_tag USING btree (slug varchar_pattern_ops);


--
-- TOC entry 4213 (class 1259 OID 27367)
-- Name: taggit_tagg_content_8fc721_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_tagg_content_8fc721_idx ON public.taggit_taggeditem USING btree (content_type_id, object_id);


--
-- TOC entry 4214 (class 1259 OID 27175)
-- Name: taggit_taggeditem_content_type_id_9957a03c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_taggeditem_content_type_id_9957a03c ON public.taggit_taggeditem USING btree (content_type_id);


--
-- TOC entry 4217 (class 1259 OID 27174)
-- Name: taggit_taggeditem_object_id_e2d7d1df; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_taggeditem_object_id_e2d7d1df ON public.taggit_taggeditem USING btree (object_id);


--
-- TOC entry 4220 (class 1259 OID 27176)
-- Name: taggit_taggeditem_tag_id_f4f5b767; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_taggeditem_tag_id_f4f5b767 ON public.taggit_taggeditem USING btree (tag_id);


--
-- TOC entry 4116 (class 1259 OID 27057)
-- Name: unique_in_progress_workflow; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX unique_in_progress_workflow ON public.wagtailcore_workflowstate USING btree (base_content_type_id, object_id) WHERE ((status)::text = ANY ((ARRAY['in_progress'::character varying, 'needs_changes'::character varying])::text[]));


--
-- TOC entry 4280 (class 1259 OID 27471)
-- Name: wagtailadmi_content_717955_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailadmi_content_717955_idx ON public.wagtailadmin_editingsession USING btree (content_type_id, object_id);


--
-- TOC entry 4281 (class 1259 OID 27469)
-- Name: wagtailadmin_editingsession_content_type_id_4df7730e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailadmin_editingsession_content_type_id_4df7730e ON public.wagtailadmin_editingsession USING btree (content_type_id);


--
-- TOC entry 4284 (class 1259 OID 27470)
-- Name: wagtailadmin_editingsession_user_id_6e1a9b70; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailadmin_editingsession_user_id_6e1a9b70 ON public.wagtailadmin_editingsession USING btree (user_id);


--
-- TOC entry 4075 (class 1259 OID 26544)
-- Name: wagtailcore_collection_path_d848dc19_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_collection_path_d848dc19_like ON public.wagtailcore_collection USING btree (path varchar_pattern_ops);


--
-- TOC entry 4098 (class 1259 OID 26603)
-- Name: wagtailcore_collectionview_collectionviewrestriction__47320efd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_collectionview_collectionviewrestriction__47320efd ON public.wagtailcore_collectionviewrestriction_groups USING btree (collectionviewrestriction_id);


--
-- TOC entry 4093 (class 1259 OID 26590)
-- Name: wagtailcore_collectionviewrestriction_collection_id_761908ec; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_collectionviewrestriction_collection_id_761908ec ON public.wagtailcore_collectionviewrestriction USING btree (collection_id);


--
-- TOC entry 4099 (class 1259 OID 26604)
-- Name: wagtailcore_collectionviewrestriction_groups_group_id_1823f2a3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_collectionviewrestriction_groups_group_id_1823f2a3 ON public.wagtailcore_collectionviewrestriction_groups USING btree (group_id);


--
-- TOC entry 4157 (class 1259 OID 26862)
-- Name: wagtailcore_comment_page_id_108444b5; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_comment_page_id_108444b5 ON public.wagtailcore_comment USING btree (page_id);


--
-- TOC entry 4160 (class 1259 OID 26863)
-- Name: wagtailcore_comment_resolved_by_id_a282aa0e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_comment_resolved_by_id_a282aa0e ON public.wagtailcore_comment USING btree (resolved_by_id);


--
-- TOC entry 4161 (class 1259 OID 26864)
-- Name: wagtailcore_comment_revision_created_id_1d058279; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_comment_revision_created_id_1d058279 ON public.wagtailcore_comment USING btree (revision_created_id);


--
-- TOC entry 4162 (class 1259 OID 26865)
-- Name: wagtailcore_comment_user_id_0c577ca6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_comment_user_id_0c577ca6 ON public.wagtailcore_comment USING btree (user_id);


--
-- TOC entry 4163 (class 1259 OID 26876)
-- Name: wagtailcore_commentreply_comment_id_afc7e027; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_commentreply_comment_id_afc7e027 ON public.wagtailcore_commentreply USING btree (comment_id);


--
-- TOC entry 4166 (class 1259 OID 26877)
-- Name: wagtailcore_commentreply_user_id_d0b3b9c3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_commentreply_user_id_d0b3b9c3 ON public.wagtailcore_commentreply USING btree (user_id);


--
-- TOC entry 4138 (class 1259 OID 26758)
-- Name: wagtailcore_groupapprovalt_groupapprovaltask_id_9a9255ea; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupapprovalt_groupapprovaltask_id_9a9255ea ON public.wagtailcore_groupapprovaltask_groups USING btree (groupapprovaltask_id);


--
-- TOC entry 4139 (class 1259 OID 26759)
-- Name: wagtailcore_groupapprovaltask_groups_group_id_2e64b61f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupapprovaltask_groups_group_id_2e64b61f ON public.wagtailcore_groupapprovaltask_groups USING btree (group_id);


--
-- TOC entry 4082 (class 1259 OID 26539)
-- Name: wagtailcore_groupcollectionpermission_collection_id_5423575a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupcollectionpermission_collection_id_5423575a ON public.wagtailcore_groupcollectionpermission USING btree (collection_id);


--
-- TOC entry 4083 (class 1259 OID 26540)
-- Name: wagtailcore_groupcollectionpermission_group_id_05d61460; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupcollectionpermission_group_id_05d61460 ON public.wagtailcore_groupcollectionpermission USING btree (group_id);


--
-- TOC entry 4084 (class 1259 OID 26541)
-- Name: wagtailcore_groupcollectionpermission_permission_id_1b626275; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupcollectionpermission_permission_id_1b626275 ON public.wagtailcore_groupcollectionpermission USING btree (permission_id);


--
-- TOC entry 4048 (class 1259 OID 26457)
-- Name: wagtailcore_grouppagepermission_group_id_fc07e671; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_grouppagepermission_group_id_fc07e671 ON public.wagtailcore_grouppagepermission USING btree (group_id);


--
-- TOC entry 4049 (class 1259 OID 26458)
-- Name: wagtailcore_grouppagepermission_page_id_710b114a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_grouppagepermission_page_id_710b114a ON public.wagtailcore_grouppagepermission USING btree (page_id);


--
-- TOC entry 4050 (class 1259 OID 27091)
-- Name: wagtailcore_grouppagepermission_permission_id_05acb22e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_grouppagepermission_permission_id_05acb22e ON public.wagtailcore_grouppagepermission USING btree (permission_id);


--
-- TOC entry 4200 (class 1259 OID 27143)
-- Name: wagtailcore_groupsitepermission_group_id_e5cdbee4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupsitepermission_group_id_e5cdbee4 ON public.wagtailcore_groupsitepermission USING btree (group_id);


--
-- TOC entry 4201 (class 1259 OID 27144)
-- Name: wagtailcore_groupsitepermission_permission_id_459b1f38; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupsitepermission_permission_id_459b1f38 ON public.wagtailcore_groupsitepermission USING btree (permission_id);


--
-- TOC entry 4204 (class 1259 OID 27145)
-- Name: wagtailcore_groupsitepermission_site_id_245de488; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupsitepermission_site_id_245de488 ON public.wagtailcore_groupsitepermission USING btree (site_id);


--
-- TOC entry 4152 (class 1259 OID 26798)
-- Name: wagtailcore_locale_language_code_03149338_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_locale_language_code_03149338_like ON public.wagtailcore_locale USING btree (language_code varchar_pattern_ops);


--
-- TOC entry 4173 (class 1259 OID 26905)
-- Name: wagtailcore_modellogentry_action_d2d856ee; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_action_d2d856ee ON public.wagtailcore_modellogentry USING btree (action);


--
-- TOC entry 4174 (class 1259 OID 26906)
-- Name: wagtailcore_modellogentry_action_d2d856ee_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_action_d2d856ee_like ON public.wagtailcore_modellogentry USING btree (action varchar_pattern_ops);


--
-- TOC entry 4175 (class 1259 OID 26907)
-- Name: wagtailcore_modellogentry_content_changed_8bc39742; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_content_changed_8bc39742 ON public.wagtailcore_modellogentry USING btree (content_changed);


--
-- TOC entry 4176 (class 1259 OID 26910)
-- Name: wagtailcore_modellogentry_content_type_id_68849e77; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_content_type_id_68849e77 ON public.wagtailcore_modellogentry USING btree (content_type_id);


--
-- TOC entry 4177 (class 1259 OID 26908)
-- Name: wagtailcore_modellogentry_object_id_e0e7d4ef; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_object_id_e0e7d4ef ON public.wagtailcore_modellogentry USING btree (object_id);


--
-- TOC entry 4178 (class 1259 OID 26909)
-- Name: wagtailcore_modellogentry_object_id_e0e7d4ef_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_object_id_e0e7d4ef_like ON public.wagtailcore_modellogentry USING btree (object_id varchar_pattern_ops);


--
-- TOC entry 4181 (class 1259 OID 27004)
-- Name: wagtailcore_modellogentry_revision_id_df6ca33a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_revision_id_df6ca33a ON public.wagtailcore_modellogentry USING btree (revision_id);


--
-- TOC entry 4182 (class 1259 OID 26912)
-- Name: wagtailcore_modellogentry_timestamp_9694521b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_timestamp_9694521b ON public.wagtailcore_modellogentry USING btree ("timestamp");


--
-- TOC entry 4183 (class 1259 OID 26911)
-- Name: wagtailcore_modellogentry_user_id_0278d1bf; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_user_id_0278d1bf ON public.wagtailcore_modellogentry USING btree (user_id);


--
-- TOC entry 4029 (class 1259 OID 26818)
-- Name: wagtailcore_page_alias_of_id_12945502; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_alias_of_id_12945502 ON public.wagtailcore_page USING btree (alias_of_id);


--
-- TOC entry 4030 (class 1259 OID 26445)
-- Name: wagtailcore_page_content_type_id_c28424df; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_content_type_id_c28424df ON public.wagtailcore_page USING btree (content_type_id);


--
-- TOC entry 4031 (class 1259 OID 26500)
-- Name: wagtailcore_page_first_published_at_2b5dd637; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_first_published_at_2b5dd637 ON public.wagtailcore_page USING btree (first_published_at);


--
-- TOC entry 4032 (class 1259 OID 27002)
-- Name: wagtailcore_page_latest_revision_id_e60fef51; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_latest_revision_id_e60fef51 ON public.wagtailcore_page USING btree (latest_revision_id);


--
-- TOC entry 4033 (class 1259 OID 26572)
-- Name: wagtailcore_page_live_revision_id_930bd822; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_live_revision_id_930bd822 ON public.wagtailcore_page USING btree (live_revision_id);


--
-- TOC entry 4034 (class 1259 OID 26806)
-- Name: wagtailcore_page_locale_id_3c7e30a6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_locale_id_3c7e30a6 ON public.wagtailcore_page USING btree (locale_id);


--
-- TOC entry 4035 (class 1259 OID 26612)
-- Name: wagtailcore_page_locked_by_id_bcb86245; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_locked_by_id_bcb86245 ON public.wagtailcore_page USING btree (locked_by_id);


--
-- TOC entry 4036 (class 1259 OID 26446)
-- Name: wagtailcore_page_owner_id_fbf7c332; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_owner_id_fbf7c332 ON public.wagtailcore_page USING btree (owner_id);


--
-- TOC entry 4037 (class 1259 OID 26442)
-- Name: wagtailcore_page_path_98eba2c8_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_path_98eba2c8_like ON public.wagtailcore_page USING btree (path varchar_pattern_ops);


--
-- TOC entry 4042 (class 1259 OID 26443)
-- Name: wagtailcore_page_slug_e7c11b8f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_slug_e7c11b8f ON public.wagtailcore_page USING btree (slug);


--
-- TOC entry 4043 (class 1259 OID 26444)
-- Name: wagtailcore_page_slug_e7c11b8f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_slug_e7c11b8f_like ON public.wagtailcore_page USING btree (slug varchar_pattern_ops);


--
-- TOC entry 4142 (class 1259 OID 26783)
-- Name: wagtailcore_pagelogentry_action_c2408198; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_action_c2408198 ON public.wagtailcore_pagelogentry USING btree (action);


--
-- TOC entry 4143 (class 1259 OID 26784)
-- Name: wagtailcore_pagelogentry_action_c2408198_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_action_c2408198_like ON public.wagtailcore_pagelogentry USING btree (action varchar_pattern_ops);


--
-- TOC entry 4144 (class 1259 OID 26785)
-- Name: wagtailcore_pagelogentry_content_changed_99f27ade; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_content_changed_99f27ade ON public.wagtailcore_pagelogentry USING btree (content_changed);


--
-- TOC entry 4145 (class 1259 OID 26786)
-- Name: wagtailcore_pagelogentry_content_type_id_74e7708a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_content_type_id_74e7708a ON public.wagtailcore_pagelogentry USING btree (content_type_id);


--
-- TOC entry 4146 (class 1259 OID 26787)
-- Name: wagtailcore_pagelogentry_page_id_8464e327; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_page_id_8464e327 ON public.wagtailcore_pagelogentry USING btree (page_id);


--
-- TOC entry 4149 (class 1259 OID 26788)
-- Name: wagtailcore_pagelogentry_revision_id_8043d103; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_revision_id_8043d103 ON public.wagtailcore_pagelogentry USING btree (revision_id);


--
-- TOC entry 4150 (class 1259 OID 26913)
-- Name: wagtailcore_pagelogentry_timestamp_deb774c4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_timestamp_deb774c4 ON public.wagtailcore_pagelogentry USING btree ("timestamp");


--
-- TOC entry 4151 (class 1259 OID 26789)
-- Name: wagtailcore_pagelogentry_user_id_604ccfd8; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_user_id_604ccfd8 ON public.wagtailcore_pagelogentry USING btree (user_id);


--
-- TOC entry 4055 (class 1259 OID 26606)
-- Name: wagtailcore_pagerevision_approved_go_live_at_e56afc67; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagerevision_approved_go_live_at_e56afc67 ON public.wagtailcore_revision USING btree (approved_go_live_at);


--
-- TOC entry 4056 (class 1259 OID 26545)
-- Name: wagtailcore_pagerevision_created_at_66954e3b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagerevision_created_at_66954e3b ON public.wagtailcore_revision USING btree (created_at);


--
-- TOC entry 4059 (class 1259 OID 26470)
-- Name: wagtailcore_pagerevision_user_id_2409d2f4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagerevision_user_id_2409d2f4 ON public.wagtailcore_revision USING btree (user_id);


--
-- TOC entry 4167 (class 1259 OID 26890)
-- Name: wagtailcore_pagesubscription_page_id_a085e7a6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagesubscription_page_id_a085e7a6 ON public.wagtailcore_pagesubscription USING btree (page_id);


--
-- TOC entry 4172 (class 1259 OID 26891)
-- Name: wagtailcore_pagesubscription_user_id_89d7def9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagesubscription_user_id_89d7def9 ON public.wagtailcore_pagesubscription USING btree (user_id);


--
-- TOC entry 4089 (class 1259 OID 26565)
-- Name: wagtailcore_pageviewrestri_pageviewrestriction_id_f147a99a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pageviewrestri_pageviewrestriction_id_f147a99a ON public.wagtailcore_pageviewrestriction_groups USING btree (pageviewrestriction_id);


--
-- TOC entry 4090 (class 1259 OID 26566)
-- Name: wagtailcore_pageviewrestriction_groups_group_id_6460f223; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pageviewrestriction_groups_group_id_6460f223 ON public.wagtailcore_pageviewrestriction_groups USING btree (group_id);


--
-- TOC entry 4062 (class 1259 OID 26476)
-- Name: wagtailcore_pageviewrestriction_page_id_15a8bea6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pageviewrestriction_page_id_15a8bea6 ON public.wagtailcore_pageviewrestriction USING btree (page_id);


--
-- TOC entry 4186 (class 1259 OID 27030)
-- Name: wagtailcore_referenceindex_base_content_type_id_313cf40f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_referenceindex_base_content_type_id_313cf40f ON public.wagtailcore_referenceindex USING btree (base_content_type_id);


--
-- TOC entry 4187 (class 1259 OID 27031)
-- Name: wagtailcore_referenceindex_content_type_id_766e0336; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_referenceindex_content_type_id_766e0336 ON public.wagtailcore_referenceindex USING btree (content_type_id);


--
-- TOC entry 4190 (class 1259 OID 27032)
-- Name: wagtailcore_referenceindex_to_content_type_id_93690bbd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_referenceindex_to_content_type_id_93690bbd ON public.wagtailcore_referenceindex USING btree (to_content_type_id);


--
-- TOC entry 4060 (class 1259 OID 26986)
-- Name: wagtailcore_revision_base_content_type_id_5b4ef7bd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_revision_base_content_type_id_5b4ef7bd ON public.wagtailcore_revision USING btree (base_content_type_id);


--
-- TOC entry 4061 (class 1259 OID 26985)
-- Name: wagtailcore_revision_content_type_id_c8cb69c0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_revision_content_type_id_c8cb69c0 ON public.wagtailcore_revision USING btree (content_type_id);


--
-- TOC entry 4065 (class 1259 OID 26482)
-- Name: wagtailcore_site_hostname_96b20b46; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_site_hostname_96b20b46 ON public.wagtailcore_site USING btree (hostname);


--
-- TOC entry 4066 (class 1259 OID 26483)
-- Name: wagtailcore_site_hostname_96b20b46_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_site_hostname_96b20b46_like ON public.wagtailcore_site USING btree (hostname varchar_pattern_ops);


--
-- TOC entry 4071 (class 1259 OID 26484)
-- Name: wagtailcore_site_root_page_id_e02fb95c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_site_root_page_id_e02fb95c ON public.wagtailcore_site USING btree (root_page_id);


--
-- TOC entry 4102 (class 1259 OID 26673)
-- Name: wagtailcore_task_content_type_id_249ab8ba; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_task_content_type_id_249ab8ba ON public.wagtailcore_task USING btree (content_type_id);


--
-- TOC entry 4105 (class 1259 OID 26689)
-- Name: wagtailcore_taskstate_content_type_id_0a758fdc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_taskstate_content_type_id_0a758fdc ON public.wagtailcore_taskstate USING btree (content_type_id);


--
-- TOC entry 4106 (class 1259 OID 26765)
-- Name: wagtailcore_taskstate_finished_by_id_13f98229; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_taskstate_finished_by_id_13f98229 ON public.wagtailcore_taskstate USING btree (finished_by_id);


--
-- TOC entry 4107 (class 1259 OID 26690)
-- Name: wagtailcore_taskstate_page_revision_id_9f52c88e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_taskstate_page_revision_id_9f52c88e ON public.wagtailcore_taskstate USING btree (revision_id);


--
-- TOC entry 4110 (class 1259 OID 26691)
-- Name: wagtailcore_taskstate_task_id_c3677c34; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_taskstate_task_id_c3677c34 ON public.wagtailcore_taskstate USING btree (task_id);


--
-- TOC entry 4111 (class 1259 OID 26731)
-- Name: wagtailcore_taskstate_workflow_state_id_9239a775; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_taskstate_workflow_state_id_9239a775 ON public.wagtailcore_taskstate USING btree (workflow_state_id);


--
-- TOC entry 4194 (class 1259 OID 27118)
-- Name: wagtailcore_uploadedfile_for_content_type_id_b0fc87b2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_uploadedfile_for_content_type_id_b0fc87b2 ON public.wagtailcore_uploadedfile USING btree (for_content_type_id);


--
-- TOC entry 4197 (class 1259 OID 27119)
-- Name: wagtailcore_uploadedfile_uploaded_by_user_id_c7580fe8; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_uploadedfile_uploaded_by_user_id_c7580fe8 ON public.wagtailcore_uploadedfile USING btree (uploaded_by_user_id);


--
-- TOC entry 4193 (class 1259 OID 27085)
-- Name: wagtailcore_workflowcontenttype_workflow_id_9aad7cd2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowcontenttype_workflow_id_9aad7cd2 ON public.wagtailcore_workflowcontenttype USING btree (workflow_id);


--
-- TOC entry 4129 (class 1259 OID 26730)
-- Name: wagtailcore_workflowpage_workflow_id_56f56ff6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowpage_workflow_id_56f56ff6 ON public.wagtailcore_workflowpage USING btree (workflow_id);


--
-- TOC entry 4117 (class 1259 OID 27059)
-- Name: wagtailcore_workflowstate_base_content_type_id_a30dc576; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowstate_base_content_type_id_a30dc576 ON public.wagtailcore_workflowstate USING btree (base_content_type_id);


--
-- TOC entry 4118 (class 1259 OID 27058)
-- Name: wagtailcore_workflowstate_content_type_id_2bb78ce1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowstate_content_type_id_2bb78ce1 ON public.wagtailcore_workflowstate USING btree (content_type_id);


--
-- TOC entry 4123 (class 1259 OID 26718)
-- Name: wagtailcore_workflowstate_requested_by_id_4090bca3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowstate_requested_by_id_4090bca3 ON public.wagtailcore_workflowstate USING btree (requested_by_id);


--
-- TOC entry 4124 (class 1259 OID 26719)
-- Name: wagtailcore_workflowstate_workflow_id_1f18378f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowstate_workflow_id_1f18378f ON public.wagtailcore_workflowstate USING btree (workflow_id);


--
-- TOC entry 4132 (class 1259 OID 26744)
-- Name: wagtailcore_workflowtask_task_id_ce7716fe; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowtask_task_id_ce7716fe ON public.wagtailcore_workflowtask USING btree (task_id);


--
-- TOC entry 4133 (class 1259 OID 26745)
-- Name: wagtailcore_workflowtask_workflow_id_b9717175; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowtask_workflow_id_b9717175 ON public.wagtailcore_workflowtask USING btree (workflow_id);


--
-- TOC entry 4285 (class 1259 OID 27491)
-- Name: wagtaildocs_document_collection_id_23881625; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtaildocs_document_collection_id_23881625 ON public.wagtaildocs_document USING btree (collection_id);


--
-- TOC entry 4288 (class 1259 OID 27484)
-- Name: wagtaildocs_document_uploaded_by_user_id_17258b41; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtaildocs_document_uploaded_by_user_id_17258b41 ON public.wagtaildocs_document USING btree (uploaded_by_user_id);


--
-- TOC entry 4289 (class 1259 OID 27528)
-- Name: wagtailembeds_embed_cache_until_26c94bb0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailembeds_embed_cache_until_26c94bb0 ON public.wagtailembeds_embed USING btree (cache_until);


--
-- TOC entry 4290 (class 1259 OID 27526)
-- Name: wagtailembeds_embed_hash_c9bd8c9a_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailembeds_embed_hash_c9bd8c9a_like ON public.wagtailembeds_embed USING btree (hash varchar_pattern_ops);


--
-- TOC entry 4295 (class 1259 OID 27542)
-- Name: wagtailforms_formsubmission_page_id_e48e93e7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailforms_formsubmission_page_id_e48e93e7 ON public.wagtailforms_formsubmission USING btree (page_id);


--
-- TOC entry 4221 (class 1259 OID 27208)
-- Name: wagtailimages_image_collection_id_c2f8af7e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_image_collection_id_c2f8af7e ON public.wagtailimages_image USING btree (collection_id);


--
-- TOC entry 4222 (class 1259 OID 27206)
-- Name: wagtailimages_image_created_at_86fa6cd4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_image_created_at_86fa6cd4 ON public.wagtailimages_image USING btree (created_at);


--
-- TOC entry 4223 (class 1259 OID 27229)
-- Name: wagtailimages_image_file_hash_fb5bbb23; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_image_file_hash_fb5bbb23 ON public.wagtailimages_image USING btree (file_hash);


--
-- TOC entry 4224 (class 1259 OID 27230)
-- Name: wagtailimages_image_file_hash_fb5bbb23_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_image_file_hash_fb5bbb23_like ON public.wagtailimages_image USING btree (file_hash varchar_pattern_ops);


--
-- TOC entry 4227 (class 1259 OID 27207)
-- Name: wagtailimages_image_uploaded_by_user_id_5d73dc75; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_image_uploaded_by_user_id_5d73dc75 ON public.wagtailimages_image USING btree (uploaded_by_user_id);


--
-- TOC entry 4228 (class 1259 OID 27214)
-- Name: wagtailimages_rendition_filter_spec_1cba3201; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_rendition_filter_spec_1cba3201 ON public.wagtailimages_rendition USING btree (filter_spec);


--
-- TOC entry 4229 (class 1259 OID 27215)
-- Name: wagtailimages_rendition_filter_spec_1cba3201_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_rendition_filter_spec_1cba3201_like ON public.wagtailimages_rendition USING btree (filter_spec varchar_pattern_ops);


--
-- TOC entry 4230 (class 1259 OID 27216)
-- Name: wagtailimages_rendition_image_id_3e1fd774; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_rendition_image_id_3e1fd774 ON public.wagtailimages_rendition USING btree (image_id);


--
-- TOC entry 4298 (class 1259 OID 27571)
-- Name: wagtailredirects_redirect_old_path_bb35247b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailredirects_redirect_old_path_bb35247b ON public.wagtailredirects_redirect USING btree (old_path);


--
-- TOC entry 4299 (class 1259 OID 27568)
-- Name: wagtailredirects_redirect_old_path_bb35247b_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailredirects_redirect_old_path_bb35247b_like ON public.wagtailredirects_redirect USING btree (old_path varchar_pattern_ops);


--
-- TOC entry 4304 (class 1259 OID 27569)
-- Name: wagtailredirects_redirect_redirect_page_id_b5728a8f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailredirects_redirect_redirect_page_id_b5728a8f ON public.wagtailredirects_redirect USING btree (redirect_page_id);


--
-- TOC entry 4305 (class 1259 OID 27570)
-- Name: wagtailredirects_redirect_site_id_780a0e1e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailredirects_redirect_site_id_780a0e1e ON public.wagtailredirects_redirect USING btree (site_id);


--
-- TOC entry 4306 (class 1259 OID 27638)
-- Name: wagtailsear_autocom_476c89_gin; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsear_autocom_476c89_gin ON public.wagtailsearch_indexentry USING gin (autocomplete);


--
-- TOC entry 4307 (class 1259 OID 27640)
-- Name: wagtailsear_body_90c85d_gin; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsear_body_90c85d_gin ON public.wagtailsearch_indexentry USING gin (body);


--
-- TOC entry 4308 (class 1259 OID 27639)
-- Name: wagtailsear_title_9caae0_gin; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsear_title_9caae0_gin ON public.wagtailsearch_indexentry USING gin (title);


--
-- TOC entry 4309 (class 1259 OID 27635)
-- Name: wagtailsearch_indexentry_content_type_id_62ed694f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsearch_indexentry_content_type_id_62ed694f ON public.wagtailsearch_indexentry USING btree (content_type_id);


--
-- TOC entry 4334 (class 1259 OID 27752)
-- Name: wagtailsearchpromotions_query_query_string_0e19aecc_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsearchpromotions_query_query_string_0e19aecc_like ON public.wagtailsearchpromotions_query USING btree (query_string varchar_pattern_ops);


--
-- TOC entry 4341 (class 1259 OID 27760)
-- Name: wagtailsearchpromotions_querydailyhits_query_id_3a591f4d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsearchpromotions_querydailyhits_query_id_3a591f4d ON public.wagtailsearchpromotions_querydailyhits USING btree (query_id);


--
-- TOC entry 4328 (class 1259 OID 27736)
-- Name: wagtailsearchpromotions_searchpromotion_page_id_71920f17; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsearchpromotions_searchpromotion_page_id_71920f17 ON public.wagtailsearchpromotions_searchpromotion USING btree (page_id);


--
-- TOC entry 4331 (class 1259 OID 27737)
-- Name: wagtailsearchpromotions_searchpromotion_query_id_fbce4eaa; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsearchpromotions_searchpromotion_query_id_fbce4eaa ON public.wagtailsearchpromotions_searchpromotion USING btree (query_id);


--
-- TOC entry 4125 (class 1259 OID 27056)
-- Name: workflowstate_base_ct_id_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX workflowstate_base_ct_id_idx ON public.wagtailcore_workflowstate USING btree (base_content_type_id, object_id);


--
-- TOC entry 4126 (class 1259 OID 27055)
-- Name: workflowstate_ct_id_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX workflowstate_ct_id_idx ON public.wagtailcore_workflowstate USING btree (content_type_id, object_id);


--
-- TOC entry 4343 (class 2606 OID 26323)
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4344 (class 2606 OID 26318)
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4342 (class 2606 OID 26309)
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4345 (class 2606 OID 26338)
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4346 (class 2606 OID 26333)
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4347 (class 2606 OID 26352)
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4348 (class 2606 OID 26347)
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4366 (class 2606 OID 26493)
-- Name: contacts_contactsubmission contacts_contactsubm_site_id_66673466_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contacts_contactsubmission
    ADD CONSTRAINT contacts_contactsubm_site_id_66673466_fk_wagtailco FOREIGN KEY (site_id) REFERENCES public.wagtailcore_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4349 (class 2606 OID 26368)
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4350 (class 2606 OID 26373)
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4419 (class 2606 OID 27260)
-- Name: pages_contactpage pages_contactpage_page_ptr_id_604d75e6_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_contactpage
    ADD CONSTRAINT pages_contactpage_page_ptr_id_604d75e6_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4420 (class 2606 OID 27265)
-- Name: pages_gallerypage pages_gallerypage_page_ptr_id_c6ee2214_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_gallerypage
    ADD CONSTRAINT pages_gallerypage_page_ptr_id_c6ee2214_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4418 (class 2606 OID 27241)
-- Name: pages_homepage pages_homepage_page_ptr_id_5b805d74_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_homepage
    ADD CONSTRAINT pages_homepage_page_ptr_id_5b805d74_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4422 (class 2606 OID 27312)
-- Name: pages_logo pages_logo_image_id_375482c6_fk_wagtailimages_image_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_logo
    ADD CONSTRAINT pages_logo_image_id_375482c6_fk_wagtailimages_image_id FOREIGN KEY (image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4421 (class 2606 OID 27307)
-- Name: pages_modularpage pages_modularpage_page_ptr_id_802d7c31_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_modularpage
    ADD CONSTRAINT pages_modularpage_page_ptr_id_802d7c31_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4423 (class 2606 OID 27333)
-- Name: pages_sitesettings pages_sitesettings_logo_id_ef4fb98b_fk_wagtailimages_image_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_sitesettings
    ADD CONSTRAINT pages_sitesettings_logo_id_ef4fb98b_fk_wagtailimages_image_id FOREIGN KEY (logo_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4424 (class 2606 OID 27348)
-- Name: pages_sitesettings pages_sitesettings_navigation_cta_page__99fb3790_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_sitesettings
    ADD CONSTRAINT pages_sitesettings_navigation_cta_page__99fb3790_fk_wagtailco FOREIGN KEY (navigation_cta_page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4425 (class 2606 OID 27338)
-- Name: pages_sitesettings pages_sitesettings_site_id_cbd7f7da_fk_wagtailcore_site_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_sitesettings
    ADD CONSTRAINT pages_sitesettings_site_id_cbd7f7da_fk_wagtailcore_site_id FOREIGN KEY (site_id) REFERENCES public.wagtailcore_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4428 (class 2606 OID 27417)
-- Name: projects_projectimage projects_projectimag_image_id_f5a991e8_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectimage
    ADD CONSTRAINT projects_projectimag_image_id_f5a991e8_fk_wagtailim FOREIGN KEY (image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4429 (class 2606 OID 27422)
-- Name: projects_projectimage projects_projectimag_project_id_618ded0e_fk_projects_; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectimage
    ADD CONSTRAINT projects_projectimag_project_id_618ded0e_fk_projects_ FOREIGN KEY (project_id) REFERENCES public.projects_project(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4442 (class 2606 OID 27706)
-- Name: projects_projectpagetag projects_projectpage_content_object_id_b258f16e_fk_projects_; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpagetag
    ADD CONSTRAINT projects_projectpage_content_object_id_b258f16e_fk_projects_ FOREIGN KEY (content_object_id) REFERENCES public.projects_projectpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4440 (class 2606 OID 27694)
-- Name: projects_projectpageimage projects_projectpage_image_id_1e7b6756_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpageimage
    ADD CONSTRAINT projects_projectpage_image_id_1e7b6756_fk_wagtailim FOREIGN KEY (image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4439 (class 2606 OID 27689)
-- Name: projects_projectpage projects_projectpage_page_ptr_id_2eccd927_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpage
    ADD CONSTRAINT projects_projectpage_page_ptr_id_2eccd927_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4441 (class 2606 OID 27699)
-- Name: projects_projectpageimage projects_projectpage_project_page_id_1f3f194b_fk_projects_; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpageimage
    ADD CONSTRAINT projects_projectpage_project_page_id_1f3f194b_fk_projects_ FOREIGN KEY (project_page_id) REFERENCES public.projects_projectpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4443 (class 2606 OID 27711)
-- Name: projects_projectpagetag projects_projectpagetag_tag_id_d11386be_fk_taggit_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpagetag
    ADD CONSTRAINT projects_projectpagetag_tag_id_d11386be_fk_taggit_tag_id FOREIGN KEY (tag_id) REFERENCES public.taggit_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4426 (class 2606 OID 27393)
-- Name: projects_projecttag projects_projecttag_content_object_id_ac067992_fk_projects_; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projecttag
    ADD CONSTRAINT projects_projecttag_content_object_id_ac067992_fk_projects_ FOREIGN KEY (content_object_id) REFERENCES public.projects_project(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4427 (class 2606 OID 27398)
-- Name: projects_projecttag projects_projecttag_tag_id_d49ab282_fk_taggit_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projecttag
    ADD CONSTRAINT projects_projecttag_tag_id_d49ab282_fk_taggit_tag_id FOREIGN KEY (tag_id) REFERENCES public.taggit_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4413 (class 2606 OID 27164)
-- Name: taggit_taggeditem taggit_taggeditem_content_type_id_9957a03c_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_content_type_id_9957a03c_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4414 (class 2606 OID 27169)
-- Name: taggit_taggeditem taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id FOREIGN KEY (tag_id) REFERENCES public.taggit_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4430 (class 2606 OID 27459)
-- Name: wagtailadmin_editingsession wagtailadmin_editing_content_type_id_4df7730e_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailadmin_editingsession
    ADD CONSTRAINT wagtailadmin_editing_content_type_id_4df7730e_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4431 (class 2606 OID 27464)
-- Name: wagtailadmin_editingsession wagtailadmin_editingsession_user_id_6e1a9b70_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailadmin_editingsession
    ADD CONSTRAINT wagtailadmin_editingsession_user_id_6e1a9b70_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4372 (class 2606 OID 26585)
-- Name: wagtailcore_collectionviewrestriction wagtailcore_collecti_collection_id_761908ec_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction
    ADD CONSTRAINT wagtailcore_collecti_collection_id_761908ec_fk_wagtailco FOREIGN KEY (collection_id) REFERENCES public.wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4373 (class 2606 OID 26593)
-- Name: wagtailcore_collectionviewrestriction_groups wagtailcore_collecti_collectionviewrestri_47320efd_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction_groups
    ADD CONSTRAINT wagtailcore_collecti_collectionviewrestri_47320efd_fk_wagtailco FOREIGN KEY (collectionviewrestriction_id) REFERENCES public.wagtailcore_collectionviewrestriction(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4374 (class 2606 OID 26598)
-- Name: wagtailcore_collectionviewrestriction_groups wagtailcore_collecti_group_id_1823f2a3_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction_groups
    ADD CONSTRAINT wagtailcore_collecti_group_id_1823f2a3_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4394 (class 2606 OID 26842)
-- Name: wagtailcore_comment wagtailcore_comment_page_id_108444b5_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_comment
    ADD CONSTRAINT wagtailcore_comment_page_id_108444b5_fk_wagtailcore_page_id FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4395 (class 2606 OID 26847)
-- Name: wagtailcore_comment wagtailcore_comment_resolved_by_id_a282aa0e_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_comment
    ADD CONSTRAINT wagtailcore_comment_resolved_by_id_a282aa0e_fk_auth_user_id FOREIGN KEY (resolved_by_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4396 (class 2606 OID 26958)
-- Name: wagtailcore_comment wagtailcore_comment_revision_created_id_1d058279_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_comment
    ADD CONSTRAINT wagtailcore_comment_revision_created_id_1d058279_fk_wagtailco FOREIGN KEY (revision_created_id) REFERENCES public.wagtailcore_revision(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4397 (class 2606 OID 26857)
-- Name: wagtailcore_comment wagtailcore_comment_user_id_0c577ca6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_comment
    ADD CONSTRAINT wagtailcore_comment_user_id_0c577ca6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4398 (class 2606 OID 26866)
-- Name: wagtailcore_commentreply wagtailcore_commentr_comment_id_afc7e027_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_commentreply
    ADD CONSTRAINT wagtailcore_commentr_comment_id_afc7e027_fk_wagtailco FOREIGN KEY (comment_id) REFERENCES public.wagtailcore_comment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4399 (class 2606 OID 26871)
-- Name: wagtailcore_commentreply wagtailcore_commentreply_user_id_d0b3b9c3_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_commentreply
    ADD CONSTRAINT wagtailcore_commentreply_user_id_d0b3b9c3_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4391 (class 2606 OID 26753)
-- Name: wagtailcore_groupapprovaltask_groups wagtailcore_groupapp_group_id_2e64b61f_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupapprovaltask_groups
    ADD CONSTRAINT wagtailcore_groupapp_group_id_2e64b61f_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4392 (class 2606 OID 26748)
-- Name: wagtailcore_groupapprovaltask_groups wagtailcore_groupapp_groupapprovaltask_id_9a9255ea_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupapprovaltask_groups
    ADD CONSTRAINT wagtailcore_groupapp_groupapprovaltask_id_9a9255ea_fk_wagtailco FOREIGN KEY (groupapprovaltask_id) REFERENCES public.wagtailcore_groupapprovaltask(task_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4381 (class 2606 OID 26692)
-- Name: wagtailcore_groupapprovaltask wagtailcore_groupapp_task_ptr_id_cfe58781_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupapprovaltask
    ADD CONSTRAINT wagtailcore_groupapp_task_ptr_id_cfe58781_fk_wagtailco FOREIGN KEY (task_ptr_id) REFERENCES public.wagtailcore_task(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4367 (class 2606 OID 26524)
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcol_collection_id_5423575a_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcol_collection_id_5423575a_fk_wagtailco FOREIGN KEY (collection_id) REFERENCES public.wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4368 (class 2606 OID 26529)
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcol_group_id_05d61460_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcol_group_id_05d61460_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4369 (class 2606 OID 26534)
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcol_permission_id_1b626275_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcol_permission_id_1b626275_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4358 (class 2606 OID 26447)
-- Name: wagtailcore_grouppagepermission wagtailcore_grouppag_group_id_fc07e671_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppag_group_id_fc07e671_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4359 (class 2606 OID 26452)
-- Name: wagtailcore_grouppagepermission wagtailcore_grouppag_page_id_710b114a_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppag_page_id_710b114a_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4360 (class 2606 OID 27097)
-- Name: wagtailcore_grouppagepermission wagtailcore_grouppag_permission_id_05acb22e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppag_permission_id_05acb22e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4410 (class 2606 OID 27128)
-- Name: wagtailcore_groupsitepermission wagtailcore_groupsit_group_id_e5cdbee4_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupsitepermission
    ADD CONSTRAINT wagtailcore_groupsit_group_id_e5cdbee4_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4411 (class 2606 OID 27133)
-- Name: wagtailcore_groupsitepermission wagtailcore_groupsit_permission_id_459b1f38_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupsitepermission
    ADD CONSTRAINT wagtailcore_groupsit_permission_id_459b1f38_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4412 (class 2606 OID 27138)
-- Name: wagtailcore_groupsitepermission wagtailcore_groupsit_site_id_245de488_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupsitepermission
    ADD CONSTRAINT wagtailcore_groupsit_site_id_245de488_fk_wagtailco FOREIGN KEY (site_id) REFERENCES public.wagtailcore_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4402 (class 2606 OID 26900)
-- Name: wagtailcore_modellogentry wagtailcore_modellog_content_type_id_68849e77_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_modellogentry
    ADD CONSTRAINT wagtailcore_modellog_content_type_id_68849e77_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4351 (class 2606 OID 26813)
-- Name: wagtailcore_page wagtailcore_page_alias_of_id_12945502_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_alias_of_id_12945502_fk_wagtailcore_page_id FOREIGN KEY (alias_of_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4352 (class 2606 OID 26432)
-- Name: wagtailcore_page wagtailcore_page_content_type_id_c28424df_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_content_type_id_c28424df_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4353 (class 2606 OID 26997)
-- Name: wagtailcore_page wagtailcore_page_latest_revision_id_e60fef51_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_latest_revision_id_e60fef51_fk_wagtailco FOREIGN KEY (latest_revision_id) REFERENCES public.wagtailcore_revision(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4354 (class 2606 OID 26567)
-- Name: wagtailcore_page wagtailcore_page_live_revision_id_930bd822_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_live_revision_id_930bd822_fk_wagtailco FOREIGN KEY (live_revision_id) REFERENCES public.wagtailcore_revision(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4355 (class 2606 OID 26807)
-- Name: wagtailcore_page wagtailcore_page_locale_id_3c7e30a6_fk_wagtailcore_locale_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_locale_id_3c7e30a6_fk_wagtailcore_locale_id FOREIGN KEY (locale_id) REFERENCES public.wagtailcore_locale(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4356 (class 2606 OID 26607)
-- Name: wagtailcore_page wagtailcore_page_locked_by_id_bcb86245_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_locked_by_id_bcb86245_fk_auth_user_id FOREIGN KEY (locked_by_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4357 (class 2606 OID 26437)
-- Name: wagtailcore_page wagtailcore_page_owner_id_fbf7c332_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_owner_id_fbf7c332_fk_auth_user_id FOREIGN KEY (owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4393 (class 2606 OID 26778)
-- Name: wagtailcore_pagelogentry wagtailcore_pageloge_content_type_id_74e7708a_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagelogentry
    ADD CONSTRAINT wagtailcore_pageloge_content_type_id_74e7708a_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4361 (class 2606 OID 26464)
-- Name: wagtailcore_revision wagtailcore_pagerevision_user_id_2409d2f4_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_revision
    ADD CONSTRAINT wagtailcore_pagerevision_user_id_2409d2f4_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4400 (class 2606 OID 26880)
-- Name: wagtailcore_pagesubscription wagtailcore_pagesubs_page_id_a085e7a6_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagesubscription
    ADD CONSTRAINT wagtailcore_pagesubs_page_id_a085e7a6_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4401 (class 2606 OID 26885)
-- Name: wagtailcore_pagesubscription wagtailcore_pagesubscription_user_id_89d7def9_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagesubscription
    ADD CONSTRAINT wagtailcore_pagesubscription_user_id_89d7def9_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4370 (class 2606 OID 26560)
-- Name: wagtailcore_pageviewrestriction_groups wagtailcore_pageview_group_id_6460f223_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction_groups
    ADD CONSTRAINT wagtailcore_pageview_group_id_6460f223_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4364 (class 2606 OID 26471)
-- Name: wagtailcore_pageviewrestriction wagtailcore_pageview_page_id_15a8bea6_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction
    ADD CONSTRAINT wagtailcore_pageview_page_id_15a8bea6_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4371 (class 2606 OID 26555)
-- Name: wagtailcore_pageviewrestriction_groups wagtailcore_pageview_pageviewrestriction__f147a99a_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction_groups
    ADD CONSTRAINT wagtailcore_pageview_pageviewrestriction__f147a99a_fk_wagtailco FOREIGN KEY (pageviewrestriction_id) REFERENCES public.wagtailcore_pageviewrestriction(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4403 (class 2606 OID 27015)
-- Name: wagtailcore_referenceindex wagtailcore_referenc_base_content_type_id_313cf40f_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_referenceindex
    ADD CONSTRAINT wagtailcore_referenc_base_content_type_id_313cf40f_fk_django_co FOREIGN KEY (base_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4404 (class 2606 OID 27020)
-- Name: wagtailcore_referenceindex wagtailcore_referenc_content_type_id_766e0336_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_referenceindex
    ADD CONSTRAINT wagtailcore_referenc_content_type_id_766e0336_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4405 (class 2606 OID 27025)
-- Name: wagtailcore_referenceindex wagtailcore_referenc_to_content_type_id_93690bbd_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_referenceindex
    ADD CONSTRAINT wagtailcore_referenc_to_content_type_id_93690bbd_fk_django_co FOREIGN KEY (to_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4362 (class 2606 OID 26992)
-- Name: wagtailcore_revision wagtailcore_revision_base_content_type_id_5b4ef7bd_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_revision
    ADD CONSTRAINT wagtailcore_revision_base_content_type_id_5b4ef7bd_fk_django_co FOREIGN KEY (base_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4363 (class 2606 OID 26987)
-- Name: wagtailcore_revision wagtailcore_revision_content_type_id_c8cb69c0_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_revision
    ADD CONSTRAINT wagtailcore_revision_content_type_id_c8cb69c0_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4365 (class 2606 OID 26477)
-- Name: wagtailcore_site wagtailcore_site_root_page_id_e02fb95c_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_site
    ADD CONSTRAINT wagtailcore_site_root_page_id_e02fb95c_fk_wagtailcore_page_id FOREIGN KEY (root_page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4375 (class 2606 OID 26668)
-- Name: wagtailcore_task wagtailcore_task_content_type_id_249ab8ba_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_task
    ADD CONSTRAINT wagtailcore_task_content_type_id_249ab8ba_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4376 (class 2606 OID 26674)
-- Name: wagtailcore_taskstate wagtailcore_taskstat_content_type_id_0a758fdc_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_taskstate
    ADD CONSTRAINT wagtailcore_taskstat_content_type_id_0a758fdc_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4377 (class 2606 OID 27033)
-- Name: wagtailcore_taskstate wagtailcore_taskstat_revision_id_df25a499_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_taskstate
    ADD CONSTRAINT wagtailcore_taskstat_revision_id_df25a499_fk_wagtailco FOREIGN KEY (revision_id) REFERENCES public.wagtailcore_revision(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4378 (class 2606 OID 26650)
-- Name: wagtailcore_taskstate wagtailcore_taskstat_workflow_state_id_9239a775_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_taskstate
    ADD CONSTRAINT wagtailcore_taskstat_workflow_state_id_9239a775_fk_wagtailco FOREIGN KEY (workflow_state_id) REFERENCES public.wagtailcore_workflowstate(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4379 (class 2606 OID 26760)
-- Name: wagtailcore_taskstate wagtailcore_taskstate_finished_by_id_13f98229_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_taskstate
    ADD CONSTRAINT wagtailcore_taskstate_finished_by_id_13f98229_fk_auth_user_id FOREIGN KEY (finished_by_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4380 (class 2606 OID 26684)
-- Name: wagtailcore_taskstate wagtailcore_taskstate_task_id_c3677c34_fk_wagtailcore_task_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_taskstate
    ADD CONSTRAINT wagtailcore_taskstate_task_id_c3677c34_fk_wagtailcore_task_id FOREIGN KEY (task_id) REFERENCES public.wagtailcore_task(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4408 (class 2606 OID 27108)
-- Name: wagtailcore_uploadedfile wagtailcore_uploaded_for_content_type_id_b0fc87b2_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_uploadedfile
    ADD CONSTRAINT wagtailcore_uploaded_for_content_type_id_b0fc87b2_fk_django_co FOREIGN KEY (for_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4409 (class 2606 OID 27113)
-- Name: wagtailcore_uploadedfile wagtailcore_uploaded_uploaded_by_user_id_c7580fe8_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_uploadedfile
    ADD CONSTRAINT wagtailcore_uploaded_uploaded_by_user_id_c7580fe8_fk_auth_user FOREIGN KEY (uploaded_by_user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4382 (class 2606 OID 27060)
-- Name: wagtailcore_workflowstate wagtailcore_workflow_base_content_type_id_a30dc576_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowstate
    ADD CONSTRAINT wagtailcore_workflow_base_content_type_id_a30dc576_fk_django_co FOREIGN KEY (base_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4383 (class 2606 OID 27065)
-- Name: wagtailcore_workflowstate wagtailcore_workflow_content_type_id_2bb78ce1_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowstate
    ADD CONSTRAINT wagtailcore_workflow_content_type_id_2bb78ce1_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4406 (class 2606 OID 27075)
-- Name: wagtailcore_workflowcontenttype wagtailcore_workflow_content_type_id_b261bb37_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowcontenttype
    ADD CONSTRAINT wagtailcore_workflow_content_type_id_b261bb37_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4384 (class 2606 OID 26697)
-- Name: wagtailcore_workflowstate wagtailcore_workflow_current_task_state_i_3a1a0632_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowstate
    ADD CONSTRAINT wagtailcore_workflow_current_task_state_i_3a1a0632_fk_wagtailco FOREIGN KEY (current_task_state_id) REFERENCES public.wagtailcore_taskstate(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4387 (class 2606 OID 26720)
-- Name: wagtailcore_workflowpage wagtailcore_workflow_page_id_81e7bab6_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowpage
    ADD CONSTRAINT wagtailcore_workflow_page_id_81e7bab6_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4385 (class 2606 OID 26707)
-- Name: wagtailcore_workflowstate wagtailcore_workflow_requested_by_id_4090bca3_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowstate
    ADD CONSTRAINT wagtailcore_workflow_requested_by_id_4090bca3_fk_auth_user FOREIGN KEY (requested_by_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4389 (class 2606 OID 26734)
-- Name: wagtailcore_workflowtask wagtailcore_workflow_task_id_ce7716fe_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowtask
    ADD CONSTRAINT wagtailcore_workflow_task_id_ce7716fe_fk_wagtailco FOREIGN KEY (task_id) REFERENCES public.wagtailcore_task(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4386 (class 2606 OID 26712)
-- Name: wagtailcore_workflowstate wagtailcore_workflow_workflow_id_1f18378f_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowstate
    ADD CONSTRAINT wagtailcore_workflow_workflow_id_1f18378f_fk_wagtailco FOREIGN KEY (workflow_id) REFERENCES public.wagtailcore_workflow(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4388 (class 2606 OID 26725)
-- Name: wagtailcore_workflowpage wagtailcore_workflow_workflow_id_56f56ff6_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowpage
    ADD CONSTRAINT wagtailcore_workflow_workflow_id_56f56ff6_fk_wagtailco FOREIGN KEY (workflow_id) REFERENCES public.wagtailcore_workflow(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4407 (class 2606 OID 27080)
-- Name: wagtailcore_workflowcontenttype wagtailcore_workflow_workflow_id_9aad7cd2_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowcontenttype
    ADD CONSTRAINT wagtailcore_workflow_workflow_id_9aad7cd2_fk_wagtailco FOREIGN KEY (workflow_id) REFERENCES public.wagtailcore_workflow(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4390 (class 2606 OID 26739)
-- Name: wagtailcore_workflowtask wagtailcore_workflow_workflow_id_b9717175_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowtask
    ADD CONSTRAINT wagtailcore_workflow_workflow_id_b9717175_fk_wagtailco FOREIGN KEY (workflow_id) REFERENCES public.wagtailcore_workflow(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4432 (class 2606 OID 27486)
-- Name: wagtaildocs_document wagtaildocs_document_collection_id_23881625_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtaildocs_document
    ADD CONSTRAINT wagtaildocs_document_collection_id_23881625_fk_wagtailco FOREIGN KEY (collection_id) REFERENCES public.wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4433 (class 2606 OID 27479)
-- Name: wagtaildocs_document wagtaildocs_document_uploaded_by_user_id_17258b41_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtaildocs_document
    ADD CONSTRAINT wagtaildocs_document_uploaded_by_user_id_17258b41_fk_auth_user FOREIGN KEY (uploaded_by_user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4434 (class 2606 OID 27537)
-- Name: wagtailforms_formsubmission wagtailforms_formsub_page_id_e48e93e7_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailforms_formsubmission
    ADD CONSTRAINT wagtailforms_formsub_page_id_e48e93e7_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4415 (class 2606 OID 27201)
-- Name: wagtailimages_image wagtailimages_image_collection_id_c2f8af7e_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_image
    ADD CONSTRAINT wagtailimages_image_collection_id_c2f8af7e_fk_wagtailco FOREIGN KEY (collection_id) REFERENCES public.wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4416 (class 2606 OID 27196)
-- Name: wagtailimages_image wagtailimages_image_uploaded_by_user_id_5d73dc75_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_image
    ADD CONSTRAINT wagtailimages_image_uploaded_by_user_id_5d73dc75_fk_auth_user FOREIGN KEY (uploaded_by_user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4417 (class 2606 OID 27209)
-- Name: wagtailimages_rendition wagtailimages_rendit_image_id_3e1fd774_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_rendition
    ADD CONSTRAINT wagtailimages_rendit_image_id_3e1fd774_fk_wagtailim FOREIGN KEY (image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4435 (class 2606 OID 27558)
-- Name: wagtailredirects_redirect wagtailredirects_red_redirect_page_id_b5728a8f_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailredirects_redirect
    ADD CONSTRAINT wagtailredirects_red_redirect_page_id_b5728a8f_fk_wagtailco FOREIGN KEY (redirect_page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4436 (class 2606 OID 27563)
-- Name: wagtailredirects_redirect wagtailredirects_red_site_id_780a0e1e_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailredirects_redirect
    ADD CONSTRAINT wagtailredirects_red_site_id_780a0e1e_fk_wagtailco FOREIGN KEY (site_id) REFERENCES public.wagtailcore_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4437 (class 2606 OID 27630)
-- Name: wagtailsearch_indexentry wagtailsearch_indexe_content_type_id_62ed694f_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_indexentry
    ADD CONSTRAINT wagtailsearch_indexe_content_type_id_62ed694f_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4444 (class 2606 OID 27767)
-- Name: wagtailsearchpromotions_searchpromotion wagtailsearchpromoti_page_id_71920f17_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_searchpromotion
    ADD CONSTRAINT wagtailsearchpromoti_page_id_71920f17_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4446 (class 2606 OID 27755)
-- Name: wagtailsearchpromotions_querydailyhits wagtailsearchpromoti_query_id_3a591f4d_fk_wagtailse; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_querydailyhits
    ADD CONSTRAINT wagtailsearchpromoti_query_id_3a591f4d_fk_wagtailse FOREIGN KEY (query_id) REFERENCES public.wagtailsearchpromotions_query(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4445 (class 2606 OID 27761)
-- Name: wagtailsearchpromotions_searchpromotion wagtailsearchpromoti_query_id_fbce4eaa_fk_wagtailse; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_searchpromotion
    ADD CONSTRAINT wagtailsearchpromoti_query_id_fbce4eaa_fk_wagtailse FOREIGN KEY (query_id) REFERENCES public.wagtailsearchpromotions_query(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4438 (class 2606 OID 27649)
-- Name: wagtailusers_userprofile wagtailusers_userprofile_user_id_59c92331_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailusers_userprofile
    ADD CONSTRAINT wagtailusers_userprofile_user_id_59c92331_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


-- Completed on 2025-09-12 10:21:55 CEST

--
-- PostgreSQL database dump complete
--

\unrestrict boDfvfP6OeEitN1JEeoRH9X4VwTI0OovdWEq3Hcp3JLISFXZg1gLpmKdgEuTeOR

