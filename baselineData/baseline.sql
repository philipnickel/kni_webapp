--
-- PostgreSQL database dump
--

\restrict kiclYaoZxVD8sySYU5EhGjhf9RYbTqKftzvtvXmFBUs8feWGAwx0TH1sqOVvfol

-- Dumped from database version 15.14
-- Dumped by pg_dump version 17.6 (Debian 17.6-0+deb13u1)

-- Started on 2025-09-12 14:47:57 CEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- TOC entry 214 (class 1259 OID 16385)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


--
-- TOC entry 215 (class 1259 OID 16388)
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
-- TOC entry 216 (class 1259 OID 16389)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- TOC entry 217 (class 1259 OID 16392)
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
-- TOC entry 218 (class 1259 OID 16393)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


--
-- TOC entry 219 (class 1259 OID 16396)
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
-- TOC entry 220 (class 1259 OID 16397)
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
-- TOC entry 221 (class 1259 OID 16402)
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- TOC entry 222 (class 1259 OID 16405)
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
-- TOC entry 223 (class 1259 OID 16406)
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
-- TOC entry 224 (class 1259 OID 16407)
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- TOC entry 225 (class 1259 OID 16410)
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
-- TOC entry 226 (class 1259 OID 16411)
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
-- TOC entry 227 (class 1259 OID 16416)
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
-- TOC entry 228 (class 1259 OID 16417)
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
-- TOC entry 229 (class 1259 OID 16423)
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
-- TOC entry 230 (class 1259 OID 16424)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- TOC entry 231 (class 1259 OID 16427)
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
-- TOC entry 232 (class 1259 OID 16428)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- TOC entry 233 (class 1259 OID 16433)
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
-- TOC entry 234 (class 1259 OID 16434)
-- Name: django_session; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- TOC entry 235 (class 1259 OID 16439)
-- Name: django_site; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


--
-- TOC entry 236 (class 1259 OID 16442)
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
-- TOC entry 237 (class 1259 OID 16443)
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
-- TOC entry 238 (class 1259 OID 16448)
-- Name: pages_gallerypage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_gallerypage (
    page_ptr_id integer NOT NULL,
    intro text NOT NULL
);


--
-- TOC entry 239 (class 1259 OID 16453)
-- Name: pages_homepage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_homepage (
    page_ptr_id integer NOT NULL,
    intro text NOT NULL,
    body jsonb NOT NULL
);


--
-- TOC entry 240 (class 1259 OID 16458)
-- Name: pages_logo; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_logo (
    id bigint NOT NULL,
    title character varying(120) NOT NULL,
    url character varying(200) NOT NULL,
    image_id integer
);


--
-- TOC entry 241 (class 1259 OID 16461)
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
-- TOC entry 242 (class 1259 OID 16462)
-- Name: pages_modularpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_modularpage (
    page_ptr_id integer NOT NULL,
    intro text NOT NULL,
    body jsonb NOT NULL
);


--
-- TOC entry 243 (class 1259 OID 16467)
-- Name: pages_service; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_service (
    id bigint NOT NULL,
    title character varying(120) NOT NULL,
    description text NOT NULL
);


--
-- TOC entry 244 (class 1259 OID 16472)
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
-- TOC entry 245 (class 1259 OID 16473)
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
-- TOC entry 246 (class 1259 OID 16478)
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
-- TOC entry 247 (class 1259 OID 16479)
-- Name: pages_testimonial; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_testimonial (
    id bigint NOT NULL,
    name character varying(120) NOT NULL,
    quote text NOT NULL,
    role character varying(120) NOT NULL
);


--
-- TOC entry 248 (class 1259 OID 16484)
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
-- TOC entry 249 (class 1259 OID 16485)
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
-- TOC entry 250 (class 1259 OID 16490)
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
-- TOC entry 251 (class 1259 OID 16491)
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
-- TOC entry 252 (class 1259 OID 16496)
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
-- TOC entry 253 (class 1259 OID 16497)
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
-- TOC entry 254 (class 1259 OID 16502)
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
-- TOC entry 255 (class 1259 OID 16507)
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
-- TOC entry 256 (class 1259 OID 16508)
-- Name: projects_projectpagetag; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.projects_projectpagetag (
    id bigint NOT NULL,
    content_object_id integer NOT NULL,
    tag_id integer NOT NULL
);


--
-- TOC entry 257 (class 1259 OID 16511)
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
-- TOC entry 258 (class 1259 OID 16512)
-- Name: projects_projecttag; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.projects_projecttag (
    id bigint NOT NULL,
    content_object_id bigint NOT NULL,
    tag_id integer NOT NULL
);


--
-- TOC entry 259 (class 1259 OID 16515)
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
-- TOC entry 260 (class 1259 OID 16516)
-- Name: taggit_tag; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.taggit_tag (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    slug character varying(100) NOT NULL
);


--
-- TOC entry 261 (class 1259 OID 16519)
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
-- TOC entry 262 (class 1259 OID 16520)
-- Name: taggit_taggeditem; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.taggit_taggeditem (
    id integer NOT NULL,
    object_id integer NOT NULL,
    content_type_id integer NOT NULL,
    tag_id integer NOT NULL
);


--
-- TOC entry 263 (class 1259 OID 16523)
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
-- TOC entry 264 (class 1259 OID 16524)
-- Name: wagtailadmin_admin; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailadmin_admin (
    id integer NOT NULL
);


--
-- TOC entry 265 (class 1259 OID 16527)
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
-- TOC entry 266 (class 1259 OID 16528)
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
-- TOC entry 267 (class 1259 OID 16531)
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
-- TOC entry 268 (class 1259 OID 16532)
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
-- TOC entry 269 (class 1259 OID 16539)
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
-- TOC entry 270 (class 1259 OID 16540)
-- Name: wagtailcore_collectionviewrestriction; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_collectionviewrestriction (
    id integer NOT NULL,
    restriction_type character varying(20) NOT NULL,
    password character varying(255) NOT NULL,
    collection_id integer NOT NULL
);


--
-- TOC entry 271 (class 1259 OID 16543)
-- Name: wagtailcore_collectionviewrestriction_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_collectionviewrestriction_groups (
    id bigint NOT NULL,
    collectionviewrestriction_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- TOC entry 272 (class 1259 OID 16546)
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
-- TOC entry 273 (class 1259 OID 16547)
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
-- TOC entry 274 (class 1259 OID 16548)
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
-- TOC entry 275 (class 1259 OID 16553)
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
-- TOC entry 276 (class 1259 OID 16554)
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
-- TOC entry 277 (class 1259 OID 16559)
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
-- TOC entry 278 (class 1259 OID 16560)
-- Name: wagtailcore_groupapprovaltask; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_groupapprovaltask (
    task_ptr_id integer NOT NULL
);


--
-- TOC entry 279 (class 1259 OID 16563)
-- Name: wagtailcore_groupapprovaltask_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_groupapprovaltask_groups (
    id bigint NOT NULL,
    groupapprovaltask_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- TOC entry 280 (class 1259 OID 16566)
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
-- TOC entry 281 (class 1259 OID 16567)
-- Name: wagtailcore_groupcollectionpermission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_groupcollectionpermission (
    id integer NOT NULL,
    collection_id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- TOC entry 282 (class 1259 OID 16570)
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
-- TOC entry 283 (class 1259 OID 16571)
-- Name: wagtailcore_grouppagepermission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_grouppagepermission (
    id integer NOT NULL,
    group_id integer NOT NULL,
    page_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- TOC entry 284 (class 1259 OID 16574)
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
-- TOC entry 285 (class 1259 OID 16575)
-- Name: wagtailcore_groupsitepermission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_groupsitepermission (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL,
    site_id integer NOT NULL
);


--
-- TOC entry 286 (class 1259 OID 16578)
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
-- TOC entry 287 (class 1259 OID 16579)
-- Name: wagtailcore_locale; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_locale (
    id integer NOT NULL,
    language_code character varying(100) NOT NULL
);


--
-- TOC entry 288 (class 1259 OID 16582)
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
-- TOC entry 289 (class 1259 OID 16583)
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
-- TOC entry 290 (class 1259 OID 16588)
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
-- TOC entry 291 (class 1259 OID 16589)
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
-- TOC entry 292 (class 1259 OID 16596)
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
-- TOC entry 293 (class 1259 OID 16597)
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
-- TOC entry 294 (class 1259 OID 16602)
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
-- TOC entry 295 (class 1259 OID 16603)
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
-- TOC entry 296 (class 1259 OID 16608)
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
-- TOC entry 297 (class 1259 OID 16609)
-- Name: wagtailcore_pagesubscription; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_pagesubscription (
    id integer NOT NULL,
    comment_notifications boolean NOT NULL,
    page_id integer NOT NULL,
    user_id integer NOT NULL
);


--
-- TOC entry 298 (class 1259 OID 16612)
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
-- TOC entry 299 (class 1259 OID 16613)
-- Name: wagtailcore_pageviewrestriction; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_pageviewrestriction (
    id integer NOT NULL,
    password character varying(255) NOT NULL,
    page_id integer NOT NULL,
    restriction_type character varying(20) NOT NULL
);


--
-- TOC entry 300 (class 1259 OID 16616)
-- Name: wagtailcore_pageviewrestriction_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_pageviewrestriction_groups (
    id bigint NOT NULL,
    pageviewrestriction_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- TOC entry 301 (class 1259 OID 16619)
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
-- TOC entry 302 (class 1259 OID 16620)
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
-- TOC entry 303 (class 1259 OID 16621)
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
-- TOC entry 304 (class 1259 OID 16626)
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
-- TOC entry 305 (class 1259 OID 16627)
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
-- TOC entry 306 (class 1259 OID 16632)
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
-- TOC entry 307 (class 1259 OID 16633)
-- Name: wagtailcore_task; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_task (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    active boolean NOT NULL,
    content_type_id integer NOT NULL
);


--
-- TOC entry 308 (class 1259 OID 16636)
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
-- TOC entry 309 (class 1259 OID 16637)
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
-- TOC entry 310 (class 1259 OID 16642)
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
-- TOC entry 311 (class 1259 OID 16643)
-- Name: wagtailcore_uploadedfile; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_uploadedfile (
    id integer NOT NULL,
    file character varying(200) NOT NULL,
    for_content_type_id integer,
    uploaded_by_user_id integer
);


--
-- TOC entry 312 (class 1259 OID 16646)
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
-- TOC entry 313 (class 1259 OID 16647)
-- Name: wagtailcore_workflow; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_workflow (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    active boolean NOT NULL
);


--
-- TOC entry 314 (class 1259 OID 16650)
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
-- TOC entry 315 (class 1259 OID 16651)
-- Name: wagtailcore_workflowcontenttype; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_workflowcontenttype (
    content_type_id integer NOT NULL,
    workflow_id integer NOT NULL
);


--
-- TOC entry 316 (class 1259 OID 16654)
-- Name: wagtailcore_workflowpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_workflowpage (
    page_id integer NOT NULL,
    workflow_id integer NOT NULL
);


--
-- TOC entry 317 (class 1259 OID 16657)
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
-- TOC entry 318 (class 1259 OID 16660)
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
-- TOC entry 319 (class 1259 OID 16661)
-- Name: wagtailcore_workflowtask; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_workflowtask (
    id integer NOT NULL,
    sort_order integer,
    task_id integer NOT NULL,
    workflow_id integer NOT NULL
);


--
-- TOC entry 320 (class 1259 OID 16664)
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
-- TOC entry 321 (class 1259 OID 16665)
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
-- TOC entry 322 (class 1259 OID 16669)
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
-- TOC entry 323 (class 1259 OID 16670)
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
-- TOC entry 324 (class 1259 OID 16675)
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
-- TOC entry 325 (class 1259 OID 16676)
-- Name: wagtailforms_formsubmission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailforms_formsubmission (
    id integer NOT NULL,
    form_data jsonb NOT NULL,
    submit_time timestamp with time zone NOT NULL,
    page_id integer NOT NULL
);


--
-- TOC entry 326 (class 1259 OID 16681)
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
-- TOC entry 327 (class 1259 OID 16682)
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
-- TOC entry 328 (class 1259 OID 16692)
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
-- TOC entry 329 (class 1259 OID 16693)
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
-- TOC entry 330 (class 1259 OID 16696)
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
-- TOC entry 331 (class 1259 OID 16697)
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
-- TOC entry 332 (class 1259 OID 16702)
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
-- TOC entry 333 (class 1259 OID 16703)
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
-- TOC entry 334 (class 1259 OID 16708)
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
-- TOC entry 335 (class 1259 OID 16709)
-- Name: wagtailsearchpromotions_query; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailsearchpromotions_query (
    id integer NOT NULL,
    query_string character varying(255) NOT NULL
);


--
-- TOC entry 336 (class 1259 OID 16712)
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
-- TOC entry 337 (class 1259 OID 16713)
-- Name: wagtailsearchpromotions_querydailyhits; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailsearchpromotions_querydailyhits (
    id integer NOT NULL,
    date date NOT NULL,
    hits integer NOT NULL,
    query_id integer NOT NULL
);


--
-- TOC entry 338 (class 1259 OID 16716)
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
-- TOC entry 339 (class 1259 OID 16717)
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
-- TOC entry 340 (class 1259 OID 16722)
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
-- TOC entry 341 (class 1259 OID 16723)
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
-- TOC entry 342 (class 1259 OID 16728)
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
-- TOC entry 4205 (class 0 OID 16385)
-- Dependencies: 214
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group (id, name) FROM stdin;
1	Moderators
2	Editors
\.


--
-- TOC entry 4207 (class 0 OID 16389)
-- Dependencies: 216
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
-- TOC entry 4209 (class 0 OID 16393)
-- Dependencies: 218
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
-- TOC entry 4211 (class 0 OID 16397)
-- Dependencies: 220
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$720000$TS2mlhQFc74VbVv5K9sAhm$wFI5eAhB1efQHUGj1/CQzaL/amNaOC4zBjDkIQsm9Xw=	2025-09-12 12:24:02.84541+00	t	admin			admin@example.com	t	t	2025-09-11 13:45:08.011701+00
\.


--
-- TOC entry 4212 (class 0 OID 16402)
-- Dependencies: 221
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- TOC entry 4215 (class 0 OID 16407)
-- Dependencies: 224
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- TOC entry 4217 (class 0 OID 16411)
-- Dependencies: 226
-- Data for Name: contacts_contactsubmission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.contacts_contactsubmission (id, created_at, name, email, phone, message, consent, status, site_id) FROM stdin;
\.


--
-- TOC entry 4219 (class 0 OID 16417)
-- Dependencies: 228
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- TOC entry 4221 (class 0 OID 16424)
-- Dependencies: 230
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
-- TOC entry 4223 (class 0 OID 16428)
-- Dependencies: 232
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2025-09-11 13:44:58.405725+00
2	auth	0001_initial	2025-09-11 13:44:58.451132+00
3	admin	0001_initial	2025-09-11 13:44:58.460529+00
4	admin	0002_logentry_remove_auto_add	2025-09-11 13:44:58.462957+00
5	admin	0003_logentry_add_action_flag_choices	2025-09-11 13:44:58.465725+00
6	contenttypes	0002_remove_content_type_name	2025-09-11 13:44:58.47129+00
7	auth	0002_alter_permission_name_max_length	2025-09-11 13:44:58.474102+00
8	auth	0003_alter_user_email_max_length	2025-09-11 13:44:58.477023+00
9	auth	0004_alter_user_username_opts	2025-09-11 13:44:58.479335+00
10	auth	0005_alter_user_last_login_null	2025-09-11 13:44:58.48417+00
11	auth	0006_require_contenttypes_0002	2025-09-11 13:44:58.484692+00
12	auth	0007_alter_validators_add_error_messages	2025-09-11 13:44:58.48698+00
13	auth	0008_alter_user_username_max_length	2025-09-11 13:44:58.492971+00
14	auth	0009_alter_user_last_name_max_length	2025-09-11 13:44:58.496223+00
15	auth	0010_alter_group_name_max_length	2025-09-11 13:44:58.500037+00
16	auth	0011_update_proxy_permissions	2025-09-11 13:44:58.502459+00
17	auth	0012_alter_user_first_name_max_length	2025-09-11 13:44:58.505408+00
18	wagtailcore	0001_initial	2025-09-11 13:44:58.612511+00
19	wagtailcore	0002_initial_data	2025-09-11 13:44:58.614201+00
20	wagtailcore	0003_add_uniqueness_constraint_on_group_page_permission	2025-09-11 13:44:58.614632+00
21	wagtailcore	0004_page_locked	2025-09-11 13:44:58.615053+00
22	wagtailcore	0005_add_page_lock_permission_to_moderators	2025-09-11 13:44:58.615564+00
23	wagtailcore	0006_add_lock_page_permission	2025-09-11 13:44:58.615994+00
24	wagtailcore	0007_page_latest_revision_created_at	2025-09-11 13:44:58.616776+00
25	wagtailcore	0008_populate_latest_revision_created_at	2025-09-11 13:44:58.617228+00
26	wagtailcore	0009_remove_auto_now_add_from_pagerevision_created_at	2025-09-11 13:44:58.617688+00
27	wagtailcore	0010_change_page_owner_to_null_on_delete	2025-09-11 13:44:58.618105+00
28	wagtailcore	0011_page_first_published_at	2025-09-11 13:44:58.618527+00
29	wagtailcore	0012_extend_page_slug_field	2025-09-11 13:44:58.618955+00
30	wagtailcore	0013_update_golive_expire_help_text	2025-09-11 13:44:58.619395+00
31	wagtailcore	0014_add_verbose_name	2025-09-11 13:44:58.619817+00
32	wagtailcore	0015_add_more_verbose_names	2025-09-11 13:44:58.620217+00
33	wagtailcore	0016_change_page_url_path_to_text_field	2025-09-11 13:44:58.620627+00
34	contacts	0001_initial	2025-09-11 13:44:58.636782+00
35	wagtailcore	0017_change_edit_page_permission_description	2025-09-11 13:44:58.669986+00
36	wagtailcore	0018_pagerevision_submitted_for_moderation_index	2025-09-11 13:44:58.677134+00
37	wagtailcore	0019_verbose_names_cleanup	2025-09-11 13:44:58.690061+00
38	wagtailcore	0020_add_index_on_page_first_published_at	2025-09-11 13:44:58.696308+00
39	wagtailcore	0021_capitalizeverbose	2025-09-11 13:44:58.77915+00
40	wagtailcore	0022_add_site_name	2025-09-11 13:44:58.785887+00
41	wagtailcore	0023_alter_page_revision_on_delete_behaviour	2025-09-11 13:44:58.789845+00
42	wagtailcore	0024_collection	2025-09-11 13:44:58.799095+00
43	wagtailcore	0025_collection_initial_data	2025-09-11 13:44:58.804207+00
44	wagtailcore	0026_group_collection_permission	2025-09-11 13:44:58.825503+00
45	wagtailcore	0027_fix_collection_path_collation	2025-09-11 13:44:58.834591+00
46	wagtailcore	0024_alter_page_content_type_on_delete_behaviour	2025-09-11 13:44:58.840121+00
47	wagtailcore	0028_merge	2025-09-11 13:44:58.841236+00
48	wagtailcore	0029_unicode_slugfield_dj19	2025-09-11 13:44:58.845221+00
49	wagtailcore	0030_index_on_pagerevision_created_at	2025-09-11 13:44:58.85096+00
50	wagtailcore	0031_add_page_view_restriction_types	2025-09-11 13:44:58.877461+00
51	wagtailcore	0032_add_bulk_delete_page_permission	2025-09-11 13:44:58.881686+00
52	wagtailcore	0033_remove_golive_expiry_help_text	2025-09-11 13:44:58.888596+00
53	wagtailcore	0034_page_live_revision	2025-09-11 13:44:58.897562+00
54	wagtailcore	0035_page_last_published_at	2025-09-11 13:44:58.901952+00
55	wagtailcore	0036_populate_page_last_published_at	2025-09-11 13:44:58.909179+00
56	wagtailcore	0037_set_page_owner_editable	2025-09-11 13:44:58.914012+00
57	wagtailcore	0038_make_first_published_at_editable	2025-09-11 13:44:58.918126+00
58	wagtailcore	0039_collectionviewrestriction	2025-09-11 13:44:58.945012+00
59	wagtailcore	0040_page_draft_title	2025-09-11 13:44:58.957409+00
60	wagtailcore	0041_group_collection_permissions_verbose_name_plural	2025-09-11 13:44:58.961003+00
61	wagtailcore	0042_index_on_pagerevision_approved_go_live_at	2025-09-11 13:44:58.967252+00
62	wagtailcore	0043_lock_fields	2025-09-11 13:44:58.979874+00
63	wagtailcore	0044_add_unlock_grouppagepermission	2025-09-11 13:44:58.98387+00
64	wagtailcore	0045_assign_unlock_grouppagepermission	2025-09-11 13:44:58.992801+00
65	wagtailcore	0046_site_name_remove_null	2025-09-11 13:44:58.998938+00
66	wagtailcore	0047_add_workflow_models	2025-09-11 13:44:59.115125+00
67	wagtailcore	0048_add_default_workflows	2025-09-11 13:44:59.144564+00
68	wagtailcore	0049_taskstate_finished_by	2025-09-11 13:44:59.157764+00
69	wagtailcore	0050_workflow_rejected_to_needs_changes	2025-09-11 13:44:59.179623+00
70	wagtailcore	0051_taskstate_comment	2025-09-11 13:44:59.189079+00
71	wagtailcore	0052_pagelogentry	2025-09-11 13:44:59.214768+00
72	wagtailcore	0053_locale_model	2025-09-11 13:44:59.222132+00
73	wagtailcore	0054_initial_locale	2025-09-11 13:44:59.231488+00
74	wagtailcore	0055_page_locale_fields	2025-09-11 13:44:59.255571+00
75	wagtailcore	0056_page_locale_fields_populate	2025-09-11 13:44:59.269475+00
76	wagtailcore	0057_page_locale_fields_notnull	2025-09-11 13:44:59.295297+00
77	wagtailcore	0058_page_alias_of	2025-09-11 13:44:59.306556+00
78	wagtailcore	0059_apply_collection_ordering	2025-09-11 13:44:59.316548+00
79	wagtailcore	0060_fix_workflow_unique_constraint	2025-09-11 13:44:59.329989+00
80	wagtailcore	0061_change_promote_tab_helpt_text_and_verbose_names	2025-09-11 13:44:59.342636+00
81	wagtailcore	0062_comment_models_and_pagesubscription	2025-09-11 13:44:59.398844+00
82	wagtailcore	0063_modellogentry	2025-09-11 13:44:59.417157+00
83	wagtailcore	0064_log_timestamp_indexes	2025-09-11 13:44:59.432703+00
84	wagtailcore	0065_log_entry_uuid	2025-09-11 13:44:59.444106+00
85	wagtailcore	0066_collection_management_permissions	2025-09-11 13:44:59.456599+00
86	wagtailcore	0067_alter_pagerevision_content_json	2025-09-11 13:44:59.479461+00
87	wagtailcore	0068_log_entry_empty_object	2025-09-11 13:44:59.493396+00
88	wagtailcore	0069_log_entry_jsonfield	2025-09-11 13:44:59.541053+00
89	wagtailcore	0070_rename_pagerevision_revision	2025-09-11 13:44:59.69455+00
90	wagtailcore	0071_populate_revision_content_type	2025-09-11 13:44:59.705265+00
91	wagtailcore	0072_alter_revision_content_type_notnull	2025-09-11 13:44:59.736782+00
92	wagtailcore	0073_page_latest_revision	2025-09-11 13:44:59.750374+00
93	wagtailcore	0074_revision_object_str	2025-09-11 13:44:59.7568+00
94	wagtailcore	0075_populate_latest_revision_and_revision_object_str	2025-09-11 13:44:59.774019+00
95	wagtailcore	0076_modellogentry_revision	2025-09-11 13:44:59.787563+00
96	wagtailcore	0077_alter_revision_user	2025-09-11 13:44:59.79535+00
97	wagtailcore	0078_referenceindex	2025-09-11 13:44:59.821019+00
98	wagtailcore	0079_rename_taskstate_page_revision	2025-09-11 13:44:59.836179+00
99	wagtailcore	0080_generic_workflowstate	2025-09-11 13:44:59.916952+00
100	wagtailcore	0081_populate_workflowstate_content_type	2025-09-11 13:44:59.927567+00
101	wagtailcore	0082_alter_workflowstate_content_type_notnull	2025-09-11 13:44:59.960964+00
102	wagtailcore	0083_workflowcontenttype	2025-09-11 13:44:59.978488+00
103	wagtailcore	0084_add_default_page_permissions	2025-09-11 13:44:59.985409+00
104	wagtailcore	0085_add_grouppagepermission_permission	2025-09-11 13:45:00.003255+00
105	wagtailcore	0086_populate_grouppagepermission_permission	2025-09-11 13:45:00.043137+00
106	wagtailcore	0087_alter_grouppagepermission_unique_together_and_more	2025-09-11 13:45:00.077407+00
107	wagtailcore	0088_fix_log_entry_json_timestamps	2025-09-11 13:45:00.105868+00
108	wagtailcore	0089_log_entry_data_json_null_to_object	2025-09-11 13:45:00.115162+00
109	wagtailcore	0090_remove_grouppagepermission_permission_type	2025-09-11 13:45:00.149025+00
110	wagtailcore	0091_remove_revision_submitted_for_moderation	2025-09-11 13:45:00.159316+00
111	wagtailcore	0092_alter_collectionviewrestriction_password_and_more	2025-09-11 13:45:00.177247+00
112	wagtailcore	0093_uploadedfile	2025-09-11 13:45:00.197167+00
113	wagtailcore	0094_alter_page_locale	2025-09-11 13:45:00.206707+00
114	wagtailcore	0095_groupsitepermission	2025-09-11 13:45:00.231797+00
115	taggit	0001_initial	2025-09-11 13:45:00.256527+00
116	wagtailimages	0001_initial	2025-09-11 13:45:00.335205+00
117	wagtailimages	0002_initial_data	2025-09-11 13:45:00.335982+00
118	wagtailimages	0003_fix_focal_point_fields	2025-09-11 13:45:00.336281+00
119	wagtailimages	0004_make_focal_point_key_not_nullable	2025-09-11 13:45:00.336599+00
120	wagtailimages	0005_make_filter_spec_unique	2025-09-11 13:45:00.336897+00
121	wagtailimages	0006_add_verbose_names	2025-09-11 13:45:00.337185+00
122	wagtailimages	0007_image_file_size	2025-09-11 13:45:00.337482+00
123	wagtailimages	0008_image_created_at_index	2025-09-11 13:45:00.337772+00
124	wagtailimages	0009_capitalizeverbose	2025-09-11 13:45:00.33824+00
125	wagtailimages	0010_change_on_delete_behaviour	2025-09-11 13:45:00.338527+00
126	wagtailimages	0011_image_collection	2025-09-11 13:45:00.338814+00
127	wagtailimages	0012_copy_image_permissions_to_collections	2025-09-11 13:45:00.339097+00
128	wagtailimages	0013_make_rendition_upload_callable	2025-09-11 13:45:00.33938+00
129	wagtailimages	0014_add_filter_spec_field	2025-09-11 13:45:00.339663+00
130	wagtailimages	0015_fill_filter_spec_field	2025-09-11 13:45:00.339942+00
131	wagtailimages	0016_deprecate_rendition_filter_relation	2025-09-11 13:45:00.340236+00
132	wagtailimages	0017_reduce_focal_point_key_max_length	2025-09-11 13:45:00.34052+00
133	wagtailimages	0018_remove_rendition_filter	2025-09-11 13:45:00.3408+00
134	wagtailimages	0019_delete_filter	2025-09-11 13:45:00.341079+00
135	wagtailimages	0020_add-verbose-name	2025-09-11 13:45:00.341401+00
136	wagtailimages	0021_image_file_hash	2025-09-11 13:45:00.341721+00
137	wagtailimages	0022_uploadedimage	2025-09-11 13:45:00.355471+00
138	wagtailadmin	0001_create_admin_access_permissions	2025-09-11 13:45:00.368256+00
139	wagtailimages	0023_add_choose_permissions	2025-09-11 13:45:00.403326+00
140	wagtailimages	0024_index_image_file_hash	2025-09-11 13:45:00.415563+00
141	wagtailimages	0025_alter_image_file_alter_rendition_file	2025-09-11 13:45:00.424849+00
142	wagtailimages	0026_delete_uploadedimage	2025-09-11 13:45:00.42808+00
143	wagtailimages	0027_image_description	2025-09-11 13:45:00.439918+00
144	pages	0001_initial	2025-09-11 13:45:00.457316+00
145	pages	0002_contactpage_gallerypage_alter_homepage_options_and_more	2025-09-11 13:45:00.549683+00
146	pages	0003_modularpage_service_testimonial_and_more	2025-09-11 13:45:00.623629+00
147	pages	0004_alter_homepage_body	2025-09-11 13:45:00.6342+00
148	pages	0005_alter_homepage_body_alter_modularpage_body	2025-09-11 13:45:00.648619+00
149	pages	0006_sitesettings_delete_themesettings	2025-09-11 13:45:00.674511+00
150	pages	0007_remove_homepage_theme_override_and_more	2025-09-11 13:45:00.692639+00
151	pages	0008_sitesettings_copyright_text_and_more	2025-09-11 13:45:00.7603+00
152	pages	0009_alter_contactpage_contact_form_intro_and_more	2025-09-11 13:45:00.77694+00
153	pages	0010_remove_sitesettings_footer_services_title_and_more	2025-09-11 13:45:00.843638+00
154	pages	0011_auto_20250910_2113	2025-09-11 13:45:00.86587+00
155	pages	0012_sitesettings_footer_services_title	2025-09-11 13:45:00.875426+00
156	pages	0013_alter_sitesettings_facebook_url_and_more	2025-09-11 13:45:00.898272+00
157	pages	0014_alter_sitesettings_footer_cta_button_text_and_more	2025-09-11 13:45:00.928152+00
158	pages	0015_add_font_and_preview_settings	2025-09-11 13:45:00.953591+00
159	taggit	0002_auto_20150616_2121	2025-09-11 13:45:00.96359+00
160	taggit	0003_taggeditem_add_unique_index	2025-09-11 13:45:00.970831+00
161	taggit	0004_alter_taggeditem_content_type_alter_taggeditem_tag	2025-09-11 13:45:00.994178+00
162	taggit	0005_auto_20220424_2025	2025-09-11 13:45:01.006747+00
163	taggit	0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx	2025-09-11 13:45:01.023753+00
164	projects	0001_initial	2025-09-11 13:45:01.08046+00
165	projects	0002_alter_project_options_project_client_name_and_more	2025-09-11 13:45:01.159027+00
166	projects	0003_remove_project_project_type	2025-09-11 13:45:01.165277+00
167	projects	0004_remove_site_field	2025-09-11 13:45:01.229758+00
168	sessions	0001_initial	2025-09-11 13:45:01.237767+00
169	sites	0001_initial	2025-09-11 13:45:01.240623+00
170	sites	0002_alter_domain_unique	2025-09-11 13:45:01.244463+00
171	wagtailadmin	0002_admin	2025-09-11 13:45:01.245578+00
172	wagtailadmin	0003_admin_managed	2025-09-11 13:45:01.24878+00
173	wagtailadmin	0004_editingsession	2025-09-11 13:45:01.271087+00
174	wagtailadmin	0005_editingsession_is_editing	2025-09-11 13:45:01.279444+00
175	wagtaildocs	0001_initial	2025-09-11 13:45:01.29981+00
176	wagtaildocs	0002_initial_data	2025-09-11 13:45:01.323704+00
177	wagtaildocs	0003_add_verbose_names	2025-09-11 13:45:01.349572+00
178	wagtaildocs	0004_capitalizeverbose	2025-09-11 13:45:01.402375+00
179	wagtaildocs	0005_document_collection	2025-09-11 13:45:01.423887+00
180	wagtaildocs	0006_copy_document_permissions_to_collections	2025-09-11 13:45:01.442476+00
181	wagtaildocs	0005_alter_uploaded_by_user_on_delete_action	2025-09-11 13:45:01.456546+00
182	wagtaildocs	0007_merge	2025-09-11 13:45:01.457626+00
183	wagtaildocs	0008_document_file_size	2025-09-11 13:45:01.466622+00
184	wagtaildocs	0009_document_verbose_name_plural	2025-09-11 13:45:01.476443+00
185	wagtaildocs	0010_document_file_hash	2025-09-11 13:45:01.486372+00
186	wagtaildocs	0011_add_choose_permissions	2025-09-11 13:45:01.529288+00
187	wagtaildocs	0012_uploadeddocument	2025-09-11 13:45:01.55076+00
188	wagtaildocs	0013_delete_uploadeddocument	2025-09-11 13:45:01.553767+00
189	wagtaildocs	0014_alter_document_file_size	2025-09-11 13:45:01.569067+00
190	wagtailembeds	0001_initial	2025-09-11 13:45:01.579451+00
191	wagtailembeds	0002_add_verbose_names	2025-09-11 13:45:01.581405+00
192	wagtailembeds	0003_capitalizeverbose	2025-09-11 13:45:01.583433+00
193	wagtailembeds	0004_embed_verbose_name_plural	2025-09-11 13:45:01.585089+00
194	wagtailembeds	0005_specify_thumbnail_url_max_length	2025-09-11 13:45:01.588033+00
195	wagtailembeds	0006_add_embed_hash	2025-09-11 13:45:01.590814+00
196	wagtailembeds	0007_populate_hash	2025-09-11 13:45:01.607252+00
197	wagtailembeds	0008_allow_long_urls	2025-09-11 13:45:01.623745+00
198	wagtailembeds	0009_embed_cache_until	2025-09-11 13:45:01.628162+00
199	wagtailforms	0001_initial	2025-09-11 13:45:01.653858+00
200	wagtailforms	0002_add_verbose_names	2025-09-11 13:45:01.666608+00
201	wagtailforms	0003_capitalizeverbose	2025-09-11 13:45:01.678685+00
202	wagtailforms	0004_add_verbose_name_plural	2025-09-11 13:45:01.685729+00
203	wagtailforms	0005_alter_formsubmission_form_data	2025-09-11 13:45:01.697766+00
204	wagtailredirects	0001_initial	2025-09-11 13:45:01.727582+00
205	wagtailredirects	0002_add_verbose_names	2025-09-11 13:45:01.747952+00
206	wagtailredirects	0003_make_site_field_editable	2025-09-11 13:45:01.761997+00
207	wagtailredirects	0004_set_unique_on_path_and_site	2025-09-11 13:45:01.785979+00
208	wagtailredirects	0005_capitalizeverbose	2025-09-11 13:45:01.840426+00
209	wagtailredirects	0006_redirect_increase_max_length	2025-09-11 13:45:01.851498+00
210	wagtailredirects	0007_add_autocreate_fields	2025-09-11 13:45:01.874008+00
211	wagtailredirects	0008_add_verbose_name_plural	2025-09-11 13:45:01.882898+00
212	wagtailsearch	0001_initial	2025-09-11 13:45:01.939683+00
213	wagtailsearch	0002_add_verbose_names	2025-09-11 13:45:02.018985+00
214	wagtailsearch	0003_remove_editors_pick	2025-09-11 13:45:02.02066+00
215	wagtailsearch	0004_querydailyhits_verbose_name_plural	2025-09-11 13:45:02.022703+00
216	wagtailsearch	0005_create_indexentry	2025-09-11 13:45:02.051331+00
217	wagtailsearch	0006_customise_indexentry	2025-09-11 13:45:02.088261+00
218	wagtailsearch	0007_delete_editorspick	2025-09-11 13:45:02.096197+00
219	wagtailsearch	0008_remove_query_and_querydailyhits_models	2025-09-11 13:45:02.114499+00
220	wagtailsearch	0009_remove_ngram_autocomplete	2025-09-11 13:45:02.118334+00
221	wagtailusers	0001_initial	2025-09-11 13:45:02.140525+00
222	wagtailusers	0002_add_verbose_name_on_userprofile	2025-09-11 13:45:02.159752+00
223	wagtailusers	0003_add_verbose_names	2025-09-11 13:45:02.168135+00
224	wagtailusers	0004_capitalizeverbose	2025-09-11 13:45:02.192611+00
225	wagtailusers	0005_make_related_name_wagtail_specific	2025-09-11 13:45:02.207321+00
226	wagtailusers	0006_userprofile_prefered_language	2025-09-11 13:45:02.217771+00
227	wagtailusers	0007_userprofile_current_time_zone	2025-09-11 13:45:02.226354+00
228	wagtailusers	0008_userprofile_avatar	2025-09-11 13:45:02.234992+00
229	wagtailusers	0009_userprofile_verbose_name_plural	2025-09-11 13:45:02.24174+00
230	wagtailusers	0010_userprofile_updated_comments_notifications	2025-09-11 13:45:02.25046+00
231	wagtailusers	0011_userprofile_dismissibles	2025-09-11 13:45:02.261358+00
232	wagtailusers	0012_userprofile_theme	2025-09-11 13:45:02.269291+00
233	wagtailusers	0013_userprofile_density	2025-09-11 13:45:02.277145+00
234	wagtailusers	0014_userprofile_contrast	2025-09-11 13:45:02.287381+00
235	wagtailusers	0015_userprofile_keyboard_shortcuts	2025-09-11 13:45:02.295983+00
236	wagtailimages	0001_squashed_0021	2025-09-11 13:45:02.298483+00
237	wagtailcore	0001_squashed_0016_change_page_url_path_to_text_field	2025-09-11 13:45:02.298954+00
238	projects	0005_add_project_page_models	2025-09-11 14:22:40.038554+00
239	projects	0006_convert_projects_to_pages	2025-09-11 14:22:40.047142+00
240	projects	0007_convert_projects_to_pages_fixed	2025-09-11 14:23:49.90461+00
241	pages	0016_alter_contactpage_contact_form_intro_and_more	2025-09-11 14:34:35.499857+00
242	wagtailsearchpromotions	0001_initial	2025-09-11 14:34:35.540835+00
243	wagtailsearchpromotions	0002_capitalizeverbose	2025-09-11 14:34:35.591265+00
244	wagtailsearchpromotions	0003_query_querydailyhits	2025-09-11 14:34:35.608838+00
245	wagtailsearchpromotions	0004_copy_queries	2025-09-11 14:34:35.609431+00
246	wagtailsearchpromotions	0005_switch_query_model	2025-09-11 14:34:35.639943+00
247	wagtailsearchpromotions	0006_reset_query_sequence	2025-09-11 14:34:35.661703+00
248	wagtailsearchpromotions	0007_searchpromotion_external_link_text_and_more	2025-09-11 14:34:35.714993+00
249	projects	0008_alter_projectpage_options_projectpage_collection_and_more	2025-09-11 14:54:13.74418+00
250	projects	0009_remove_collection_field	2025-09-11 16:24:00.467668+00
\.


--
-- TOC entry 4225 (class 0 OID 16434)
-- Dependencies: 234
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
v1p3lz8mc0mnby7nhzernz29omlgyk3v	.eJxVjMEOwiAQRP-FsyFLsS3t0bvfQJZlFdSAgTbRGP9dSXrQZE4zb95LWFyXYNfKxUYvZqHE7rdzSFdObfAXTOcsKaelRCcbIre1ymP2fDts7J8gYA3tbfa6H432E6GHjjwjK02Dgo4RiBScaPpGITjmEdl0AIA9agOoBmrSyrXGnCw_7rE8xQzvD7RSP9A:1uwhd9:Y8ADH3psdneg1xwcbI4DfJQtIkFW-AN-zJgc6xCjga8	2025-09-25 13:46:31.162255+00
magqj7t49ktawuwf8xzowdluxhtb009i	.eJxVjEEOwiAQRe_C2pCxlGnr0r1nIMDMWNSAKW2iMd5dm3Sh2__efy_l_DKPbqk8uUTqoPZq97sFH6-cV0AXn89Fx5LnKQW9KnqjVZ8K8e24uX-B0dfx-27Ytj6SRBFGgM4gWGsitNCJNDiQDEgmoAm9geCFySBGS8G2A_Zg12jlWlPJjh_3ND3VAd4fn9s_Rg:1uwhzQ:gMYueolaleIJBVQ2vlu01wZHHF9MYJ2EH4TTnHoaTG0	2025-09-25 14:09:32.965561+00
uy37tcsk1e3a3fgbtax6wcoy2cccn3gu	.eJxVjEEOwiAQRe_C2pCxlGnr0r1nIMDMWNSAKW2iMd5dm3Sh2__efy_l_DKPbqk8uUTqoPZq97sFH6-cV0AXn89Fx5LnKQW9KnqjVZ8K8e24uX-B0dfx-27Ytj6SRBFGgM4gWGsitNCJNDiQDEgmoAm9geCFySBGS8G2A_Zg12jlWlPJjh_3ND3VAd4fn9s_Rg:1uwwqp:z9DPz4zlj1Ey86dFvuA27qOl8n3N_TrLu6erjaqNpEo	2025-09-26 06:01:39.252397+00
8on61kl0a0ctwm2o6yu5af7gjihlowmt	.eJxVjMsOwiAQRf-FtSFteRS6dO83kIEZLGrAlDbRGP9dSbrQ7T3nnhdzsK2z2yotLiGbWM8Ov5uHcKXcAF4gnwsPJa9L8rwpfKeVnwrS7bi7f4EZ6vx9y1Fo9AZJe0s6iGBsb0JUMBgQBAMhWW0BYpR6VOQ7hT2A7yQYGgTFFq1UayrZ0eOeliebuvcHypRAag:1uwzc0:4BbGAFrT7uOXa5_y-cs2lvoLfw5nMcleT-OvjflcfcM	2025-09-26 08:58:32.163766+00
sxakq9pdk2tfjwag6asubhanlw72jdj0	.eJxVjMsOwiAQRf-FtSFteRS6dO83kIEZLGrAlDbRGP9dSbrQ7T3nnhdzsK2z2yotLiGbWM8Ov5uHcKXcAF4gnwsPJa9L8rwpfKeVnwrS7bi7f4EZ6vx9y1Fo9AZJe0s6iGBsb0JUMBgQBAMhWW0BYpR6VOQ7hT2A7yQYGgTFFq1UayrZ0eOeliebuvcHypRAag:1ux1rM:5AiCht2G7R3f9X0QcN88brZY0rHTBxkt2nvJ7v7YDYU	2025-09-26 11:22:32.784462+00
6kuaphzavyo9n5dm206rms26w38d0j0x	.eJxVjMsOwiAQRf-FtSFteRS6dO83kIEZLGrAlDbRGP9dSbrQ7T3nnhdzsK2z2yotLiGbWM8Ov5uHcKXcAF4gnwsPJa9L8rwpfKeVnwrS7bi7f4EZ6vx9y1Fo9AZJe0s6iGBsb0JUMBgQBAMhWW0BYpR6VOQ7hT2A7yQYGgTFFq1UayrZ0eOeliebuvcHypRAag:1ux2RM:xUz_tvv7MJ_cBx0EXfAhbV5lkIMbogFCDWQIRxysp4c	2025-09-26 11:59:44.498995+00
zph70833ez9b8658cct4p7qic51gagps	.eJxVjMsOwiAQRf-FtSFteRS6dO83kIEZLGrAlDbRGP9dSbrQ7T3nnhdzsK2z2yotLiGbWM8Ov5uHcKXcAF4gnwsPJa9L8rwpfKeVnwrS7bi7f4EZ6vx9y1Fo9AZJe0s6iGBsb0JUMBgQBAMhWW0BYpR6VOQ7hT2A7yQYGgTFFq1UayrZ0eOeliebuvcHypRAag:1ux2os:Vc1RhIElNJwy4GSb5WJ_NFvg6gIjNRacV8v8JefFYfE	2025-09-26 12:24:02.846377+00
\.


--
-- TOC entry 4226 (class 0 OID 16439)
-- Dependencies: 235
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- TOC entry 4228 (class 0 OID 16443)
-- Dependencies: 237
-- Data for Name: pages_contactpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_contactpage (page_ptr_id, intro, show_contact_form, contact_form_title, contact_form_intro) FROM stdin;
5	<p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>	t	Send os en besked	<p>Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
\.


--
-- TOC entry 4229 (class 0 OID 16448)
-- Dependencies: 238
-- Data for Name: pages_gallerypage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_gallerypage (page_ptr_id, intro) FROM stdin;
4	<p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
\.


--
-- TOC entry 4230 (class 0 OID 16453)
-- Dependencies: 239
-- Data for Name: pages_homepage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_homepage (page_ptr_id, intro, body) FROM stdin;
3	<p data-block-key="fichi">TEMPLATE: Professionelle bygge- og renoveringsløsninger med fokus på kvalitet og håndværk</p>	[{"id": "3475c607-30ae-48b8-bbd5-93b14c9218cb", "type": "hero_v2", "value": {"image": null, "style": {"divider": false, "spacing": "md", "container": "normal", "background": "hero"}, "heading": "TEMP Professionelle byggeløsninger i København og omegn", "subheading": "Fra køkkenrenovering til komplette nybyggerier - vi leverer håndværk af højeste kvalitet med fokus på kundetilfredshed og termintro fastholding.", "primary_page": 5, "primary_text": "Få et uforpligtende tilbud", "secondary_page": 4, "secondary_text": "Se vores projekter"}}, {"id": "fb18f1d7-0f6c-4b13-8d42-38eef9aa72d9", "type": "trust_badges", "value": {"items": [{"id": "01c444da-75ef-4754-9251-081ae07a8dcd", "type": "item", "value": {"icon": "star", "title": "Kvalitet i hver detalje", "description": "Vi går aldrig på kompromis med kvaliteten. Alle materialer og håndværk lever op til de højeste standarder."}}, {"id": "95a47f2f-fad0-4b0e-a08e-7ad574fee53d", "type": "item", "value": {"icon": "clock", "title": "Altid til tiden", "description": "Vi overholder altid vores deadlines og leverer projekter til tiden. Planlægning og pålidelighed er i højsædet."}}], "style": {"divider": false, "spacing": "md", "container": "normal", "background": "surface"}, "columns": "4", "heading": "Derfor vælger kunder JCleemannByg"}}, {"id": "90037c54-259e-4132-8d90-128931be7ceb", "type": "featured_projects", "value": {"style": {"divider": false, "spacing": "md", "container": "normal", "background": "surface"}, "columns": "3", "heading": "Udvalgte projekter", "subheading": "Se eksempler på vores seneste arbejde og få inspiration til dit næste projekt", "show_all_link": true, "all_projects_page": 4}}, {"id": "3d581778-17de-45f9-b911-fa5da29ca790", "type": "services_grid_inline", "value": {"items": [{"id": "338dfc7d-5ee7-433d-927d-42d4d25005f1", "type": "item", "value": {"icon": "check", "title": "Køkkenrenovering", "description": "Totalrenovering af køkkener med skræddersyede løsninger, kvalitetsmaterialer og moderne design"}}], "style": {"divider": false, "spacing": "md", "container": "normal", "background": "surface"}, "columns": "3", "heading": "Vores servicesaa"}}]
\.


--
-- TOC entry 4231 (class 0 OID 16458)
-- Dependencies: 240
-- Data for Name: pages_logo; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_logo (id, title, url, image_id) FROM stdin;
\.


--
-- TOC entry 4233 (class 0 OID 16462)
-- Dependencies: 242
-- Data for Name: pages_modularpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_modularpage (page_ptr_id, intro, body) FROM stdin;
\.


--
-- TOC entry 4234 (class 0 OID 16467)
-- Dependencies: 243
-- Data for Name: pages_service; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_service (id, title, description) FROM stdin;
\.


--
-- TOC entry 4236 (class 0 OID 16473)
-- Dependencies: 245
-- Data for Name: pages_sitesettings; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_sitesettings (id, company_name, phone, email, cvr, address, default_theme, logo_id, site_id, copyright_text, footer_contact_title, footer_description, navigation_cta_page_id, navigation_cta_text, show_navigation, facebook_url, footer_cta_button_text, footer_cta_text, footer_cta_title, instagram_url, linkedin_url, opening_hours, footer_services_title, font_choice, enable_preview, preview_url_override) FROM stdin;
1	JCleemannByg	+45 12 34 56 78	info@jcleemannbyg.dk	12345678	Eksempel Vej 123, 1234 København	forest	97	1	© 2025 JCleemannByg. Alle rettigheder forbeholdes.	Kontakt		\N		t	\N	Få et tilbud	Kontakt JCleemannByg i dag for et uforpligtende tilbud på dit næste projekt.	Klar til at starte?	\N	\N	Mandag - Fredag: 08:00 - 16:00\r\nLørdag: 08:00 - 12:00\r\nSøndag: Lukket	Services	inter-playfair	t	
\.


--
-- TOC entry 4238 (class 0 OID 16479)
-- Dependencies: 247
-- Data for Name: pages_testimonial; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_testimonial (id, name, quote, role) FROM stdin;
\.


--
-- TOC entry 4240 (class 0 OID 16485)
-- Dependencies: 249
-- Data for Name: projects_project; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects_project (id, title, slug, description, featured, published, date, client_name, location, materials) FROM stdin;
10	Træ terrasse og udendørs køkken	tr-terrasse-og-udendrs-kkken	<h3>Smukt udendørs køkken og terrasse</h3>\n                <p>Vi har bygget en fantastisk træterrasse med integreret udendørs køkken. Projektet omfatter:</p>\n                <ul>\n                    <li>Lærketræ terrasse på 45m²</li>\n                    <li>Indbygget grill og kogezone</li>\n                    <li>Opbevaringsløsninger i vejrbestandigt træ</li>\n                    <li>LED-belysning til aftentimer</li>\n                </ul>\n                <p>Materialer brugt: Lærketræ, rustfrit stål, natursten. Projektet blev færdiggjort til tiden og within budget.</p>	t	t	2024-08-15	Familie Hansen	Privat villa, Nordsjælland	Lærketræ, rustfrit stål, natursten
11	Villa renovering i København	villa-renovering-i-kbenhavn	<h3>Totalrenovering af historisk villa</h3>\n                <p>Komplet renovering af villa fra 1920'erne med respekt for den oprindelige arkitektur:</p>\n                <ul>\n                    <li>Restaurering af originale trægulve</li>\n                    <li>Modernisering af køkken og badeværelser</li>\n                    <li>Energioptimering med nye vinduer</li>\n                    <li>Tilbygning af moderne familierum</li>\n                </ul>\n                <p>Et smukt eksempel på hvordan historie og moderne komfort kan forenes harmonisk.</p>	t	t	2024-06-20	Privat kunde	Indre København	Eg, marmor, glas, tegl
12	Skræddersyet køkken installation	skrddersyet-kkken-installation	<h3>Håndlavet køkken efter mål</h3>\n                <p>Designet og bygget et unikt køkken der passer perfekt til kundens behov:</p>\n                <ul>\n                    <li>Massiv eg køkkenø med Corian bordplade</li>\n                    <li>Skræddersyede skabe i alle højder</li>\n                    <li>Integrerede hvidevarer af højeste kvalitet</li>\n                    <li>Skjult LED-belysning under skabe</li>\n                </ul>\n                <p>Køkkenet er både funktionelt og æstetisk smukt.</p>	f	t	2024-03-10		Frederiksberg	Massiv eg, Corian, rustfrit stål
13	Badeværelse renovering	badevrelse-renovering	<h3>Luksuriøst badeværelse</h3>\n                <p>Fuldstændig renovering af master badeværelse:</p>\n                <ul>\n                    <li>Italienske marmor fliser</li>\n                    <li>Fritstående badekar</li>\n                    <li>Regnbruser med termostat</li>\n                    <li>Skræddersyet vask møbel</li>\n                </ul>\n                <p>Et spa-lignende badeværelse der oser af luksus og komfort.</p>	f	t	2023-11-05		Gentofte	Marmor, messing, glas
14	Moderne kontorbygning	moderne-kontorbygning	<h3>Erhvervsprojekt med fokus på bæredygtighed</h3>\n                <p>Opførelse af moderne kontorbygning for mindre virksomhed:</p>\n                <ul>\n                    <li>Bæredygtige materialer i hele byggeriet</li>\n                    <li>Store glaspartier for naturligt lys</li>\n                    <li>Energieffektiv varme- og ventilationsystem</li>\n                    <li>Fleksible kontorrum der kan tilpasses</li>\n                </ul>\n                <p>Et moderne og miljøvenligt arbejdsmiljø.</p>	f	t	2023-09-15	TechStart ApS	Erhvervsområde, Glostrup	Træ, glas, beton, stål
15	Alternativehand1	alternativehand1		f	t	2025-09-12			
16	Carpenter1	carpenter1		f	t	2025-09-12			
17	Carpenter2	carpenter2		f	t	2025-09-12			
18	Carpenter3	carpenter3		f	t	2025-09-12			
19	Handwork1	handwork1		f	t	2025-09-12			
20	Roof1	roof1		f	t	2025-09-12			
21	Woodworking1	woodworking1		f	t	2025-09-12			
22	Alternativehand Project	alternativehand-project		f	t	2025-09-12			
23	Carpenter Project	carpenter-project		f	t	2025-09-12			
24	Handwork Project	handwork-project		f	t	2025-09-12			
25	Roof Project	roof-project		f	t	2025-09-12			
26	Woodworking Project	woodworking-project		f	t	2025-09-12			
\.


--
-- TOC entry 4242 (class 0 OID 16491)
-- Dependencies: 251
-- Data for Name: projects_projectimage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects_projectimage (id, sort_order, caption, alt_text, image_id, project_id) FROM stdin;
28	\N	Woodworking Project - woodworking1.jpg	Woodworking Project billede	\N	26
15	\N	Alternativehand1	Alternativehand1 billede	\N	15
16	\N	Carpenter1	Carpenter1 billede	\N	16
17	\N	Carpenter2	Carpenter2 billede	\N	17
18	\N	Carpenter3	Carpenter3 billede	\N	18
19	\N	Handwork1	Handwork1 billede	\N	19
20	\N	Roof1	Roof1 billede	\N	20
21	\N	Woodworking1	Woodworking1 billede	\N	21
22	\N	Alternativehand Project - alternativeHand1.jpg	Alternativehand Project billede	\N	22
23	\N	Carpenter Project - carpenter1.jpg	Carpenter Project billede	\N	23
24	\N	Carpenter Project - carpenter2.jpg	Carpenter Project billede	\N	23
25	\N	Carpenter Project - carpenter3.png	Carpenter Project billede	\N	23
26	\N	Handwork Project - handwork1.jpg	Handwork Project billede	\N	24
27	\N	Roof Project - roof1.jpg	Roof Project billede	\N	25
10	\N	Billede af Træ terrasse og udendørs køkken	Professionelt håndværk: Træ terrasse og udendørs køkken	\N	10
11	\N	Billede af Villa renovering i København	Professionelt håndværk: Villa renovering i København	\N	11
12	\N	Billede af Skræddersyet køkken installation	Professionelt håndværk: Skræddersyet køkken installation	\N	12
13	\N	Billede af Badeværelse renovering	Professionelt håndværk: Badeværelse renovering	\N	13
14	\N	Billede af Moderne kontorbygning	Professionelt håndværk: Moderne kontorbygning	\N	14
\.


--
-- TOC entry 4244 (class 0 OID 16497)
-- Dependencies: 253
-- Data for Name: projects_projectpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects_projectpage (page_ptr_id, description, materials, client_name, location, featured, project_date, estimated_budget, priority, project_status) FROM stdin;
\.


--
-- TOC entry 4245 (class 0 OID 16502)
-- Dependencies: 254
-- Data for Name: projects_projectpageimage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects_projectpageimage (id, sort_order, caption, alt_text, image_id, project_page_id) FROM stdin;
\.


--
-- TOC entry 4247 (class 0 OID 16508)
-- Dependencies: 256
-- Data for Name: projects_projectpagetag; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects_projectpagetag (id, content_object_id, tag_id) FROM stdin;
\.


--
-- TOC entry 4249 (class 0 OID 16512)
-- Dependencies: 258
-- Data for Name: projects_projecttag; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects_projecttag (id, content_object_id, tag_id) FROM stdin;
\.


--
-- TOC entry 4251 (class 0 OID 16516)
-- Dependencies: 260
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
-- TOC entry 4253 (class 0 OID 16520)
-- Dependencies: 262
-- Data for Name: taggit_taggeditem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.taggit_taggeditem (id, object_id, content_type_id, tag_id) FROM stdin;
\.


--
-- TOC entry 4255 (class 0 OID 16524)
-- Dependencies: 264
-- Data for Name: wagtailadmin_admin; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailadmin_admin (id) FROM stdin;
\.


--
-- TOC entry 4257 (class 0 OID 16528)
-- Dependencies: 266
-- Data for Name: wagtailadmin_editingsession; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailadmin_editingsession (id, object_id, last_seen_at, content_type_id, user_id, is_editing) FROM stdin;
\.


--
-- TOC entry 4259 (class 0 OID 16532)
-- Dependencies: 268
-- Data for Name: wagtailcore_collection; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_collection (id, path, depth, numchild, name) FROM stdin;
1	0001	1	0	Root
\.


--
-- TOC entry 4261 (class 0 OID 16540)
-- Dependencies: 270
-- Data for Name: wagtailcore_collectionviewrestriction; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_collectionviewrestriction (id, restriction_type, password, collection_id) FROM stdin;
\.


--
-- TOC entry 4262 (class 0 OID 16543)
-- Dependencies: 271
-- Data for Name: wagtailcore_collectionviewrestriction_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_collectionviewrestriction_groups (id, collectionviewrestriction_id, group_id) FROM stdin;
\.


--
-- TOC entry 4265 (class 0 OID 16548)
-- Dependencies: 274
-- Data for Name: wagtailcore_comment; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_comment (id, text, contentpath, "position", created_at, updated_at, resolved_at, page_id, resolved_by_id, revision_created_id, user_id) FROM stdin;
\.


--
-- TOC entry 4267 (class 0 OID 16554)
-- Dependencies: 276
-- Data for Name: wagtailcore_commentreply; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_commentreply (id, text, created_at, updated_at, comment_id, user_id) FROM stdin;
\.


--
-- TOC entry 4269 (class 0 OID 16560)
-- Dependencies: 278
-- Data for Name: wagtailcore_groupapprovaltask; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_groupapprovaltask (task_ptr_id) FROM stdin;
1
\.


--
-- TOC entry 4270 (class 0 OID 16563)
-- Dependencies: 279
-- Data for Name: wagtailcore_groupapprovaltask_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_groupapprovaltask_groups (id, groupapprovaltask_id, group_id) FROM stdin;
1	1	1
\.


--
-- TOC entry 4272 (class 0 OID 16567)
-- Dependencies: 281
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
-- TOC entry 4274 (class 0 OID 16571)
-- Dependencies: 283
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
-- TOC entry 4276 (class 0 OID 16575)
-- Dependencies: 285
-- Data for Name: wagtailcore_groupsitepermission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_groupsitepermission (id, group_id, permission_id, site_id) FROM stdin;
\.


--
-- TOC entry 4278 (class 0 OID 16579)
-- Dependencies: 287
-- Data for Name: wagtailcore_locale; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_locale (id, language_code) FROM stdin;
1	da
\.


--
-- TOC entry 4280 (class 0 OID 16583)
-- Dependencies: 289
-- Data for Name: wagtailcore_modellogentry; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_modellogentry (id, label, action, data, "timestamp", content_changed, deleted, object_id, content_type_id, user_id, uuid, revision_id) FROM stdin;
1	Generelle indstillinger for localhost [standardindstilling]	wagtail.edit	{}	2025-09-11 14:12:41.599939+00	t	f	1	53	1	d3c46905-e624-4d9a-8ad4-ad8dcf2e9308	\N
2	Generelle indstillinger for localhost [standardindstilling]	wagtail.edit	{}	2025-09-12 11:54:29.563886+00	t	f	1	53	1	11b6ccb1-4f2a-4bad-aef0-060efc88914b	\N
\.


--
-- TOC entry 4282 (class 0 OID 16589)
-- Dependencies: 291
-- Data for Name: wagtailcore_page; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_page (id, path, depth, numchild, title, slug, live, has_unpublished_changes, url_path, seo_title, show_in_menus, search_description, go_live_at, expire_at, expired, content_type_id, owner_id, locked, latest_revision_created_at, first_published_at, live_revision_id, last_published_at, draft_title, locked_at, locked_by_id, translation_key, locale_id, alias_of_id, latest_revision_id) FROM stdin;
5	000100020001	3	0	Kontakt Os	kontakt	t	f	/home-1/kontakt/		f		\N	\N	f	50	\N	f	2025-09-11 13:45:14.640185+00	2025-09-11 13:45:14.654193+00	3	2025-09-11 13:45:14.654193+00	Kontakt Os	\N	\N	1c559f5d-212e-44d6-893a-0163fe51b483	1	\N	3
4	000100020002	3	0	Projekt Galleri	galleri	t	f	/home-1/galleri/		f		\N	\N	f	51	\N	f	2025-09-11 13:45:14.577423+00	2025-09-11 13:45:14.591057+00	2	2025-09-11 13:45:14.591057+00	Projekt Galleri	\N	\N	f18d5f96-a655-4c41-bc93-ba827d7e972d	1	\N	2
1	0001	1	1	Root	root	t	f	/		f		\N	\N	f	1	\N	f	\N	\N	\N	\N	Root	\N	\N	06315736-99b7-4c3d-8d9f-7376af6c1faf	1	\N	\N
3	00010002	2	2	Velkommen til JCleemannByg	home-1	t	f	/home-1/		f		\N	\N	f	49	\N	f	2025-09-12 11:22:47.17581+00	2025-09-11 13:45:14.529+00	33	2025-09-12 11:22:47.201738+00	Velkommen til JCleemannByg	\N	\N	3fc166df-3682-476a-ba86-e93c617785c0	1	\N	33
\.


--
-- TOC entry 4284 (class 0 OID 16597)
-- Dependencies: 293
-- Data for Name: wagtailcore_pagelogentry; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pagelogentry (id, label, action, data, "timestamp", content_changed, deleted, content_type_id, page_id, revision_id, user_id, uuid) FROM stdin;
1	Velkommen til JCleemannByg	wagtail.create	{}	2025-09-11 13:45:14.488913+00	t	f	49	3	\N	\N	\N
2	Velkommen til JCleemannByg	wagtail.publish	{}	2025-09-11 13:45:14.549317+00	t	f	49	3	1	\N	\N
3	Projekt Galleri	wagtail.create	{}	2025-09-11 13:45:14.563705+00	t	f	51	4	\N	\N	\N
4	Projekt Galleri	wagtail.publish	{}	2025-09-11 13:45:14.61091+00	t	f	51	4	2	\N	\N
5	Kontakt Os	wagtail.create	{}	2025-09-11 13:45:14.625077+00	t	f	50	5	\N	\N	\N
6	Kontakt Os	wagtail.publish	{}	2025-09-11 13:45:14.674705+00	t	f	50	5	3	\N	\N
7	Velkommen til JCleemannByg	wagtail.publish	{}	2025-09-11 13:45:56.78316+00	t	f	49	3	4	\N	\N
8	Kontakt Os	wagtail.move	{"source": {"id": 1, "title": "Root"}, "destination": {"id": 3, "title": "Velkommen til JCleemannByg"}}	2025-09-11 13:50:51.283539+00	f	f	50	5	\N	\N	\N
9	Velkommen til JCleemannByg	wagtail.edit	{}	2025-09-11 13:59:35.656122+00	t	f	49	3	5	1	01f85d8e-4421-4543-8687-93b56c93b4ed
10	Velkommen til JCleemannByg	wagtail.edit	{}	2025-09-11 14:01:51.200614+00	t	f	49	3	6	1	5fe7e187-99b1-4cc1-9995-d77dc9f98bf4
11	Velkommen til JCleemannByg	wagtail.publish	{}	2025-09-11 14:01:51.236516+00	f	f	49	3	6	1	5fe7e187-99b1-4cc1-9995-d77dc9f98bf4
12	Træ terrasse og udendørs køkken	wagtail.create	{}	2025-09-11 14:24:01.469144+00	t	f	58	6	\N	\N	\N
13	Villa renovering i København	wagtail.create	{}	2025-09-11 14:24:01.52418+00	t	f	58	7	\N	\N	\N
14	Skræddersyet køkken installation	wagtail.create	{}	2025-09-11 14:24:01.55674+00	t	f	58	8	\N	\N	\N
15	Badeværelse renovering	wagtail.create	{}	2025-09-11 14:24:01.587236+00	t	f	58	9	\N	\N	\N
16	Moderne kontorbygning	wagtail.create	{}	2025-09-11 14:24:01.615489+00	t	f	58	10	\N	\N	\N
17	Projekt Galleri	wagtail.move	{"source": {"id": 1, "title": "Root"}, "destination": {"id": 3, "title": "Velkommen til JCleemannByg"}}	2025-09-11 14:24:44.518321+00	f	f	51	4	\N	\N	\N
18	Galleri	wagtail.create	{}	2025-09-11 16:11:15.389645+00	t	f	51	11	\N	\N	\N
19	Galleri	wagtail.publish	{}	2025-09-11 16:11:15.418835+00	t	f	51	11	7	\N	\N
20	Lille trin udført i jatoba	wagtail.create	{}	2025-09-11 16:11:15.429749+00	t	f	58	12	\N	\N	\N
21	Lille trin udført i jatoba	wagtail.publish	{}	2025-09-11 16:11:15.454528+00	t	f	58	12	8	\N	\N
22	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗	wagtail.create	{}	2025-09-11 16:11:15.723535+00	t	f	58	13	\N	\N	\N
23	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗	wagtail.publish	{}	2025-09-11 16:11:15.745638+00	t	f	58	13	9	\N	\N
24	Fugen skulle skiftes på disse døre. 	wagtail.create	{}	2025-09-11 16:11:15.788714+00	t	f	58	14	\N	\N	\N
25	Fugen skulle skiftes på disse døre. 	wagtail.publish	{}	2025-09-11 16:11:15.808952+00	t	f	58	14	10	\N	\N
26	Lærepladsen bliver også passet🦦	wagtail.create	{}	2025-09-11 16:11:15.875881+00	t	f	58	15	\N	\N	\N
27	Lærepladsen bliver også passet🦦	wagtail.publish	{}	2025-09-11 16:11:15.89611+00	t	f	58	15	11	\N	\N
28	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 	wagtail.create	{}	2025-09-11 16:11:15.952445+00	t	f	58	16	\N	\N	\N
29	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 	wagtail.publish	{}	2025-09-11 16:11:15.97211+00	t	f	58	16	12	\N	\N
30	Møbelsnedkeren i mig er virkelig glad! 🥳 	wagtail.create	{}	2025-09-11 16:11:16.002688+00	t	f	58	17	\N	\N	\N
31	Møbelsnedkeren i mig er virkelig glad! 🥳 	wagtail.publish	{}	2025-09-11 16:11:16.022371+00	t	f	58	17	13	\N	\N
32	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵	wagtail.create	{}	2025-09-11 16:11:16.057082+00	t	f	58	18	\N	\N	\N
33	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵	wagtail.publish	{}	2025-09-11 16:11:16.076152+00	t	f	58	18	14	\N	\N
34	Fundament/beton/whatever skjuler. 	wagtail.create	{}	2025-09-11 16:11:16.118493+00	t	f	58	19	\N	\N	\N
35	Fundament/beton/whatever skjuler. 	wagtail.publish	{}	2025-09-11 16:11:16.138301+00	t	f	58	19	15	\N	\N
36	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!	wagtail.create	{}	2025-09-11 16:11:16.175138+00	t	f	58	20	\N	\N	\N
37	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!	wagtail.publish	{}	2025-09-11 16:11:16.194433+00	t	f	58	20	16	\N	\N
38	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔	wagtail.create	{}	2025-09-11 16:11:16.292007+00	t	f	58	21	\N	\N	\N
39	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔	wagtail.publish	{}	2025-09-11 16:11:16.311723+00	t	f	58	21	17	\N	\N
40	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸	wagtail.create	{}	2025-09-11 16:11:16.346856+00	t	f	58	22	\N	\N	\N
41	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸	wagtail.publish	{}	2025-09-11 16:11:16.365919+00	t	f	58	22	18	\N	\N
42	En opgradering af TV alteret hos min kammerat🦔	wagtail.create	{}	2025-09-11 16:11:16.412265+00	t	f	58	23	\N	\N	\N
43	En opgradering af TV alteret hos min kammerat🦔	wagtail.publish	{}	2025-09-11 16:11:16.429477+00	t	f	58	23	19	\N	\N
44	Lille trin udført i jatoba	wagtail.create	{}	2025-09-11 16:13:58.252134+00	t	f	58	24	\N	\N	\N
45	Lille trin udført i jatoba	wagtail.publish	{}	2025-09-11 16:13:58.270749+00	t	f	58	24	20	\N	\N
46	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗	wagtail.create	{}	2025-09-11 16:13:58.307824+00	t	f	58	25	\N	\N	\N
47	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗	wagtail.publish	{}	2025-09-11 16:13:58.326582+00	t	f	58	25	21	\N	\N
48	Fugen skulle skiftes på disse døre. 	wagtail.create	{}	2025-09-11 16:13:58.363855+00	t	f	58	26	\N	\N	\N
49	Fugen skulle skiftes på disse døre. 	wagtail.publish	{}	2025-09-11 16:13:58.378167+00	t	f	58	26	22	\N	\N
50	Lærepladsen bliver også passet🦦	wagtail.create	{}	2025-09-11 16:13:58.44788+00	t	f	58	27	\N	\N	\N
51	Lærepladsen bliver også passet🦦	wagtail.publish	{}	2025-09-11 16:13:58.468282+00	t	f	58	27	23	\N	\N
52	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 	wagtail.create	{}	2025-09-11 16:13:58.525612+00	t	f	58	28	\N	\N	\N
53	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 	wagtail.publish	{}	2025-09-11 16:13:58.53957+00	t	f	58	28	24	\N	\N
54	Møbelsnedkeren i mig er virkelig glad! 🥳 	wagtail.create	{}	2025-09-11 16:13:58.567355+00	t	f	58	29	\N	\N	\N
55	Møbelsnedkeren i mig er virkelig glad! 🥳 	wagtail.publish	{}	2025-09-11 16:13:58.584838+00	t	f	58	29	25	\N	\N
56	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵	wagtail.create	{}	2025-09-11 16:13:58.615952+00	t	f	58	30	\N	\N	\N
57	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵	wagtail.publish	{}	2025-09-11 16:13:58.62838+00	t	f	58	30	26	\N	\N
58	Fundament/beton/whatever skjuler. 	wagtail.publish	{}	2025-09-11 16:13:58.683541+00	t	f	58	19	27	\N	\N
59	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!	wagtail.create	{}	2025-09-11 16:13:58.716997+00	t	f	58	31	\N	\N	\N
60	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!	wagtail.publish	{}	2025-09-11 16:13:58.732369+00	t	f	58	31	28	\N	\N
61	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔	wagtail.create	{}	2025-09-11 16:13:58.813295+00	t	f	58	32	\N	\N	\N
62	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔	wagtail.publish	{}	2025-09-11 16:13:58.834504+00	t	f	58	32	29	\N	\N
63	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸	wagtail.create	{}	2025-09-11 16:13:58.894887+00	t	f	58	33	\N	\N	\N
64	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸	wagtail.publish	{}	2025-09-11 16:13:58.921758+00	t	f	58	33	30	\N	\N
65	En opgradering af TV alteret hos min kammerat🦔	wagtail.publish	{}	2025-09-11 16:13:58.995106+00	t	f	58	23	31	\N	\N
66	Velkommen til JCleemannByg	wagtail.edit	{}	2025-09-12 08:58:56.010874+00	t	f	49	3	32	1	339a023e-e266-4834-bca7-e533c2e8f6f4
67	Velkommen til JCleemannByg	wagtail.publish	{}	2025-09-12 08:58:56.038596+00	t	f	49	3	32	1	339a023e-e266-4834-bca7-e533c2e8f6f4
68	Velkommen til JCleemannByg	wagtail.edit	{}	2025-09-12 11:22:47.196637+00	t	f	49	3	33	1	345973f6-2f87-4f8b-bdbf-8e49de595d7a
69	Velkommen til JCleemannByg	wagtail.publish	{}	2025-09-12 11:22:47.215812+00	t	f	49	3	33	1	345973f6-2f87-4f8b-bdbf-8e49de595d7a
70	Alternativehand Project	wagtail.create	{}	2025-09-12 11:36:07.146817+00	t	f	58	34	\N	\N	\N
71	Alternativehand Project	wagtail.publish	{}	2025-09-12 11:36:07.179367+00	t	f	58	34	34	\N	\N
72	Carpenter Project	wagtail.create	{}	2025-09-12 11:36:07.205301+00	t	f	58	35	\N	\N	\N
73	Carpenter Project	wagtail.publish	{}	2025-09-12 11:36:07.230983+00	t	f	58	35	35	\N	\N
74	Handwork Project	wagtail.create	{}	2025-09-12 11:36:07.342553+00	t	f	58	36	\N	\N	\N
75	Handwork Project	wagtail.publish	{}	2025-09-12 11:36:07.368723+00	t	f	58	36	36	\N	\N
76	Roof Project	wagtail.create	{}	2025-09-12 11:36:07.390065+00	t	f	58	37	\N	\N	\N
77	Roof Project	wagtail.publish	{}	2025-09-12 11:36:07.415203+00	t	f	58	37	37	\N	\N
78	Woodworking Project	wagtail.create	{}	2025-09-12 11:36:07.436674+00	t	f	58	38	\N	\N	\N
79	Woodworking Project	wagtail.publish	{}	2025-09-12 11:36:07.462009+00	t	f	58	38	38	\N	\N
80	Lille trin udført i jatoba	wagtail.delete	{}	2025-09-12 12:25:13.697096+00	f	t	58	12	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
81	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗	wagtail.delete	{}	2025-09-12 12:25:13.703581+00	f	t	58	13	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
82	Fugen skulle skiftes på disse døre. 	wagtail.delete	{}	2025-09-12 12:25:13.706117+00	f	t	58	14	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
83	Lærepladsen bliver også passet🦦	wagtail.delete	{}	2025-09-12 12:25:13.707662+00	f	t	58	15	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
84	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 	wagtail.delete	{}	2025-09-12 12:25:13.709258+00	f	t	58	16	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
85	Møbelsnedkeren i mig er virkelig glad! 🥳 	wagtail.delete	{}	2025-09-12 12:25:13.710517+00	f	t	58	17	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
86	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵	wagtail.delete	{}	2025-09-12 12:25:13.712383+00	f	t	58	18	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
87	Fundament/beton/whatever skjuler. 	wagtail.delete	{}	2025-09-12 12:25:13.714037+00	f	t	58	19	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
88	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!	wagtail.delete	{}	2025-09-12 12:25:13.715343+00	f	t	58	20	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
89	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔	wagtail.delete	{}	2025-09-12 12:25:13.716693+00	f	t	58	21	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
90	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸	wagtail.delete	{}	2025-09-12 12:25:13.718068+00	f	t	58	22	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
91	En opgradering af TV alteret hos min kammerat🦔	wagtail.delete	{}	2025-09-12 12:25:13.719316+00	f	t	58	23	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
92	Lille trin udført i jatoba	wagtail.delete	{}	2025-09-12 12:25:13.720838+00	f	t	58	24	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
93	Nogen gange kan man spare stilladset. Det kræver bare man kan lokke nogen til at sikre den anden ende af det reb der holder dig 🧗	wagtail.delete	{}	2025-09-12 12:25:13.722041+00	f	t	58	25	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
94	Fugen skulle skiftes på disse døre. 	wagtail.delete	{}	2025-09-12 12:25:13.723187+00	f	t	58	26	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
95	Lærepladsen bliver også passet🦦	wagtail.delete	{}	2025-09-12 12:25:13.724315+00	f	t	58	27	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
96	Har jeg glemt at tage et før billede? Det har jeg vist nok lige. 	wagtail.delete	{}	2025-09-12 12:25:13.72614+00	f	t	58	28	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
97	Møbelsnedkeren i mig er virkelig glad! 🥳 	wagtail.delete	{}	2025-09-12 12:25:13.727634+00	f	t	58	29	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
98	Bevaringsværdige vinduer. 4 sæt færdige. 4 sæt tilbage. 🪵	wagtail.delete	{}	2025-09-12 12:25:13.729252+00	f	t	58	30	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
99	Havde søde @tihizebra med ude for, at fikse vinduer. Samt udvide min viden om linolie og linoliemaling. Det var super hyggeligt!	wagtail.delete	{}	2025-09-12 12:25:13.730274+00	f	t	58	31	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
100	En uheldig undertags gennemføring (eller mangel på gennemføring). Så er det heldigt at det kan laves korrekt indefra 🦔	wagtail.delete	{}	2025-09-12 12:25:13.731185+00	f	t	58	32	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
101	Udskiftning af punkteret rude. Dejligt at finde et lille hul i det ellers meget grå vejr 🥸	wagtail.delete	{}	2025-09-12 12:25:13.732037+00	f	t	58	33	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
102	Galleri	wagtail.delete	{}	2025-09-12 12:25:13.733639+00	f	t	51	11	\N	1	2ff7bc04-7ff0-4dde-b5ba-00076b9317e3
103	Træ terrasse og udendørs køkken	wagtail.delete	{}	2025-09-12 12:25:44.865389+00	f	t	58	6	\N	1	8af818ab-de89-4058-914c-25b3cdad434e
104	Villa renovering i København	wagtail.delete	{}	2025-09-12 12:25:44.899798+00	f	t	58	7	\N	1	8af818ab-de89-4058-914c-25b3cdad434e
105	Skræddersyet køkken installation	wagtail.delete	{}	2025-09-12 12:25:44.918671+00	f	t	58	8	\N	1	8af818ab-de89-4058-914c-25b3cdad434e
106	Badeværelse renovering	wagtail.delete	{}	2025-09-12 12:25:44.935704+00	f	t	58	9	\N	1	8af818ab-de89-4058-914c-25b3cdad434e
107	Moderne kontorbygning	wagtail.delete	{}	2025-09-12 12:25:44.951822+00	f	t	58	10	\N	1	8af818ab-de89-4058-914c-25b3cdad434e
108	Alternativehand Project	wagtail.delete	{}	2025-09-12 12:25:44.96783+00	f	t	58	34	\N	1	8af818ab-de89-4058-914c-25b3cdad434e
109	Carpenter Project	wagtail.delete	{}	2025-09-12 12:25:44.984593+00	f	t	58	35	\N	1	8af818ab-de89-4058-914c-25b3cdad434e
110	Handwork Project	wagtail.delete	{}	2025-09-12 12:25:45.001416+00	f	t	58	36	\N	1	8af818ab-de89-4058-914c-25b3cdad434e
111	Roof Project	wagtail.delete	{}	2025-09-12 12:25:45.017882+00	f	t	58	37	\N	1	8af818ab-de89-4058-914c-25b3cdad434e
112	Woodworking Project	wagtail.delete	{}	2025-09-12 12:25:45.034938+00	f	t	58	38	\N	1	8af818ab-de89-4058-914c-25b3cdad434e
113	Welcome to your new Wagtail site!	wagtail.delete	{}	2025-09-12 12:25:54.138446+00	f	t	1	2	\N	1	5966b081-3b24-4dce-88f3-b12b8469a25e
\.


--
-- TOC entry 4288 (class 0 OID 16609)
-- Dependencies: 297
-- Data for Name: wagtailcore_pagesubscription; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pagesubscription (id, comment_notifications, page_id, user_id) FROM stdin;
1	f	3	1
2	f	4	1
6	f	5	1
\.


--
-- TOC entry 4290 (class 0 OID 16613)
-- Dependencies: 299
-- Data for Name: wagtailcore_pageviewrestriction; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pageviewrestriction (id, password, page_id, restriction_type) FROM stdin;
\.


--
-- TOC entry 4291 (class 0 OID 16616)
-- Dependencies: 300
-- Data for Name: wagtailcore_pageviewrestriction_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pageviewrestriction_groups (id, pageviewrestriction_id, group_id) FROM stdin;
\.


--
-- TOC entry 4294 (class 0 OID 16621)
-- Dependencies: 303
-- Data for Name: wagtailcore_referenceindex; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_referenceindex (id, object_id, to_object_id, model_path, content_path, content_path_hash, base_content_type_id, content_type_id, to_content_type_id) FROM stdin;
20	10	10	images.item.image	images.10.image	d0b160c2-0045-5a6d-b01f-2274ec307420	41	41	26
22	11	11	images.item.image	images.11.image	d879c17f-a9a2-5422-ba38-60e8e1a54ecf	41	41	26
24	12	12	images.item.image	images.12.image	d1b52978-a9ef-5ef8-8e2c-404890e9cfcf	41	41	26
26	13	13	images.item.image	images.13.image	63107060-1686-56a7-aed7-3b05c67d45cb	41	41	26
28	14	14	images.item.image	images.14.image	c9a4713e-9c60-5b66-8931-33896b5c8685	41	41	26
29	3	4	body.hero_v2.secondary_page	body.3475c607-30ae-48b8-bbd5-93b14c9218cb.secondary_page	c88541a7-0fd6-59ab-95e7-d371505ebebb	1	49	1
30	3	5	body.hero_v2.primary_page	body.3475c607-30ae-48b8-bbd5-93b14c9218cb.primary_page	ee82076a-62d6-5bcc-99ce-7f20a76ae718	1	49	1
31	3	4	body.featured_projects.all_projects_page	body.90037c54-259e-4132-8d90-128931be7ceb.all_projects_page	2c1ef3ad-825a-5542-91b1-97e24f28545a	1	49	1
185	90	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
187	91	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
189	92	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
191	93	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
193	94	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
195	95	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
197	96	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
199	97	1	collection	collection	b40b1263-e929-57f2-a7f8-9dbce56b887b	26	26	9
\.


--
-- TOC entry 4286 (class 0 OID 16603)
-- Dependencies: 295
-- Data for Name: wagtailcore_revision; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_revision (id, created_at, content, approved_go_live_at, object_id, user_id, content_type_id, base_content_type_id, object_str) FROM stdin;
2	2025-09-11 13:45:14.577423+00	{"pk": 4, "live": true, "path": "00010003", "slug": "galleri", "depth": 2, "intro": "<p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>", "owner": null, "title": "Projekt Galleri", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 0, "url_path": "/galleri/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Projekt Galleri", "content_type": 51, "live_revision": null, "show_in_menus": false, "latest_revision": null, "translation_key": "f18d5f96-a655-4c41-bc93-ba827d7e972d", "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	4	\N	51	1	Projekt Galleri
3	2025-09-11 13:45:14.640185+00	{"pk": 5, "live": true, "path": "00010004", "slug": "kontakt", "depth": 2, "intro": "<p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>", "owner": null, "title": "Kontakt Os", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 0, "url_path": "/kontakt/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Kontakt Os", "content_type": 50, "live_revision": null, "show_in_menus": false, "latest_revision": null, "translation_key": "1c559f5d-212e-44d6-893a-0163fe51b483", "last_published_at": null, "show_contact_form": true, "contact_form_intro": "<p>Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>", "contact_form_title": "Send os en besked", "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	5	\N	50	1	Kontakt Os
4	2025-09-11 13:45:56.742682+00	{"pk": 3, "body": "[]", "live": true, "path": "00010002", "slug": "home-1", "depth": 2, "intro": "<p>Professionelle bygge- og renoveringsløsninger med fokus på kvalitet og håndværk</p>", "owner": null, "title": "Velkommen til JCleemannByg", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 0, "url_path": "/home-1/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Velkommen til JCleemannByg", "content_type": 49, "live_revision": 1, "show_in_menus": false, "latest_revision": 1, "translation_key": "3fc166df-3682-476a-ba86-e93c617785c0", "last_published_at": "2025-09-11T13:45:14.529Z", "first_published_at": "2025-09-11T13:45:14.529Z", "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": "2025-09-11T13:45:14.515Z"}	\N	3	\N	49	1	Velkommen til JCleemannByg
32	2025-09-12 08:58:55.98181+00	{"pk": 3, "body": "[{\\"type\\": \\"hero_v2\\", \\"value\\": {\\"heading\\": \\"TEMP Professionelle byggel\\\\u00f8sninger i K\\\\u00f8benhavn og omegn\\", \\"subheading\\": \\"Fra k\\\\u00f8kkenrenovering til komplette nybyggerier - vi leverer h\\\\u00e5ndv\\\\u00e6rk af h\\\\u00f8jeste kvalitet med fokus p\\\\u00e5 kundetilfredshed og termintro fastholding.\\", \\"primary_text\\": \\"F\\\\u00e5 et uforpligtende tilbud\\", \\"primary_page\\": 5, \\"secondary_text\\": \\"Se vores projekter\\", \\"secondary_page\\": 4, \\"image\\": null, \\"style\\": {\\"background\\": \\"hero\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"3475c607-30ae-48b8-bbd5-93b14c9218cb\\"}, {\\"type\\": \\"trust_badges\\", \\"value\\": {\\"heading\\": \\"Derfor v\\\\u00e6lger kunder JCleemannByg\\", \\"items\\": [{\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"Kvalitet i hver detalje\\", \\"description\\": \\"Vi g\\\\u00e5r aldrig p\\\\u00e5 kompromis med kvaliteten. Alle materialer og h\\\\u00e5ndv\\\\u00e6rk lever op til de h\\\\u00f8jeste standarder.\\", \\"icon\\": \\"star\\"}, \\"id\\": \\"01c444da-75ef-4754-9251-081ae07a8dcd\\"}, {\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"Altid til tiden\\", \\"description\\": \\"Vi overholder altid vores deadlines og leverer projekter til tiden. Planl\\\\u00e6gning og p\\\\u00e5lidelighed er i h\\\\u00f8js\\\\u00e6det.\\", \\"icon\\": \\"clock\\"}, \\"id\\": \\"95a47f2f-fad0-4b0e-a08e-7ad574fee53d\\"}], \\"columns\\": \\"4\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"fb18f1d7-0f6c-4b13-8d42-38eef9aa72d9\\"}, {\\"type\\": \\"featured_projects\\", \\"value\\": {\\"heading\\": \\"Udvalgte projekter\\", \\"subheading\\": \\"Se eksempler p\\\\u00e5 vores seneste arbejde og f\\\\u00e5 inspiration til dit n\\\\u00e6ste projekt\\", \\"show_all_link\\": true, \\"all_projects_page\\": 4, \\"columns\\": \\"3\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"90037c54-259e-4132-8d90-128931be7ceb\\"}, {\\"type\\": \\"services_grid_inline\\", \\"value\\": {\\"heading\\": \\"Vores services\\", \\"items\\": [{\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"K\\\\u00f8kkenrenovering\\", \\"description\\": \\"Totalrenovering af k\\\\u00f8kkener med skr\\\\u00e6ddersyede l\\\\u00f8sninger, kvalitetsmaterialer og moderne design\\", \\"icon\\": \\"check\\"}, \\"id\\": \\"338dfc7d-5ee7-433d-927d-42d4d25005f1\\"}], \\"columns\\": \\"3\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"3d581778-17de-45f9-b911-fa5da29ca790\\"}]", "live": true, "path": "00010002", "slug": "home-1", "depth": 2, "intro": "<p data-block-key=\\"fichi\\">TEMPLATE: Professionelle bygge- og renoveringsløsninger med fokus på kvalitet og håndværk</p>", "owner": null, "title": "Velkommen til JCleemannByg", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 3, "url_path": "/home-1/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Velkommen til JCleemannByg", "content_type": 49, "live_revision": 6, "show_in_menus": false, "latest_revision": 6, "translation_key": "3fc166df-3682-476a-ba86-e93c617785c0", "last_published_at": "2025-09-11T14:01:51.209Z", "first_published_at": "2025-09-11T13:45:14.529Z", "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": "2025-09-11T14:01:51.176Z"}	\N	3	1	49	1	Velkommen til JCleemannByg
1	2025-09-11 13:45:14.515774+00	{"pk": 3, "body": "[]", "live": true, "path": "00010002", "slug": "home-1", "depth": 2, "intro": "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>", "owner": null, "title": "Velkommen til JCleemannByg", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 0, "url_path": "/home-1/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Velkommen til JCleemannByg", "content_type": 49, "live_revision": null, "show_in_menus": false, "latest_revision": null, "translation_key": "3fc166df-3682-476a-ba86-e93c617785c0", "last_published_at": null, "first_published_at": null, "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": null}	\N	3	\N	49	1	Velkommen til JCleemannByg
33	2025-09-12 11:22:47.17581+00	{"pk": 3, "body": "[{\\"type\\": \\"hero_v2\\", \\"value\\": {\\"heading\\": \\"TEMP Professionelle byggel\\\\u00f8sninger i K\\\\u00f8benhavn og omegn\\", \\"subheading\\": \\"Fra k\\\\u00f8kkenrenovering til komplette nybyggerier - vi leverer h\\\\u00e5ndv\\\\u00e6rk af h\\\\u00f8jeste kvalitet med fokus p\\\\u00e5 kundetilfredshed og termintro fastholding.\\", \\"primary_text\\": \\"F\\\\u00e5 et uforpligtende tilbud\\", \\"primary_page\\": 5, \\"secondary_text\\": \\"Se vores projekter\\", \\"secondary_page\\": 4, \\"image\\": null, \\"style\\": {\\"background\\": \\"hero\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"3475c607-30ae-48b8-bbd5-93b14c9218cb\\"}, {\\"type\\": \\"trust_badges\\", \\"value\\": {\\"heading\\": \\"Derfor v\\\\u00e6lger kunder JCleemannByg\\", \\"items\\": [{\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"Kvalitet i hver detalje\\", \\"description\\": \\"Vi g\\\\u00e5r aldrig p\\\\u00e5 kompromis med kvaliteten. Alle materialer og h\\\\u00e5ndv\\\\u00e6rk lever op til de h\\\\u00f8jeste standarder.\\", \\"icon\\": \\"star\\"}, \\"id\\": \\"01c444da-75ef-4754-9251-081ae07a8dcd\\"}, {\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"Altid til tiden\\", \\"description\\": \\"Vi overholder altid vores deadlines og leverer projekter til tiden. Planl\\\\u00e6gning og p\\\\u00e5lidelighed er i h\\\\u00f8js\\\\u00e6det.\\", \\"icon\\": \\"clock\\"}, \\"id\\": \\"95a47f2f-fad0-4b0e-a08e-7ad574fee53d\\"}], \\"columns\\": \\"4\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"fb18f1d7-0f6c-4b13-8d42-38eef9aa72d9\\"}, {\\"type\\": \\"featured_projects\\", \\"value\\": {\\"heading\\": \\"Udvalgte projekter\\", \\"subheading\\": \\"Se eksempler p\\\\u00e5 vores seneste arbejde og f\\\\u00e5 inspiration til dit n\\\\u00e6ste projekt\\", \\"show_all_link\\": true, \\"all_projects_page\\": 4, \\"columns\\": \\"3\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"90037c54-259e-4132-8d90-128931be7ceb\\"}, {\\"type\\": \\"services_grid_inline\\", \\"value\\": {\\"heading\\": \\"Vores servicesaa\\", \\"items\\": [{\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"K\\\\u00f8kkenrenovering\\", \\"description\\": \\"Totalrenovering af k\\\\u00f8kkener med skr\\\\u00e6ddersyede l\\\\u00f8sninger, kvalitetsmaterialer og moderne design\\", \\"icon\\": \\"check\\"}, \\"id\\": \\"338dfc7d-5ee7-433d-927d-42d4d25005f1\\"}], \\"columns\\": \\"3\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"3d581778-17de-45f9-b911-fa5da29ca790\\"}]", "live": true, "path": "00010002", "slug": "home-1", "depth": 2, "intro": "<p data-block-key=\\"fichi\\">TEMPLATE: Professionelle bygge- og renoveringsløsninger med fokus på kvalitet og håndværk</p>", "owner": null, "title": "Velkommen til JCleemannByg", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 3, "url_path": "/home-1/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Velkommen til JCleemannByg", "content_type": 49, "live_revision": 32, "show_in_menus": false, "latest_revision": 32, "translation_key": "3fc166df-3682-476a-ba86-e93c617785c0", "last_published_at": "2025-09-12T08:58:56.018Z", "first_published_at": "2025-09-11T13:45:14.529Z", "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": "2025-09-12T08:58:55.981Z"}	\N	3	1	49	1	Velkommen til JCleemannByg
5	2025-09-11 13:59:35.636113+00	{"pk": 3, "body": "[{\\"type\\": \\"hero_v2\\", \\"value\\": {\\"heading\\": \\"Professionelle byggel\\\\u00f8sninger i K\\\\u00f8benhavn og omegn\\", \\"subheading\\": \\"Fra k\\\\u00f8kkenrenovering til komplette nybyggerier - vi leverer h\\\\u00e5ndv\\\\u00e6rk af h\\\\u00f8jeste kvalitet med fokus p\\\\u00e5 kundetilfredshed og termintro fastholding.\\", \\"primary_text\\": \\"F\\\\u00e5 et uforpligtende tilbud\\", \\"primary_page\\": 5, \\"secondary_text\\": \\"Se vores projekter\\", \\"secondary_page\\": 4, \\"image\\": null, \\"style\\": {\\"background\\": \\"hero\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"3475c607-30ae-48b8-bbd5-93b14c9218cb\\"}, {\\"type\\": \\"trust_badges\\", \\"value\\": {\\"heading\\": \\"Derfor v\\\\u00e6lger kunder JCleemannByg\\", \\"items\\": [{\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"Kvalitet i hver detalje\\", \\"description\\": \\"Vi g\\\\u00e5r aldrig p\\\\u00e5 kompromis med kvaliteten. Alle materialer og h\\\\u00e5ndv\\\\u00e6rk lever op til de h\\\\u00f8jeste standarder.\\", \\"icon\\": \\"star\\"}, \\"id\\": \\"01c444da-75ef-4754-9251-081ae07a8dcd\\"}, {\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"Altid til tiden\\", \\"description\\": \\"Vi overholder altid vores deadlines og leverer projekter til tiden. Planl\\\\u00e6gning og p\\\\u00e5lidelighed er i h\\\\u00f8js\\\\u00e6det.\\", \\"icon\\": \\"clock\\"}, \\"id\\": \\"95a47f2f-fad0-4b0e-a08e-7ad574fee53d\\"}], \\"columns\\": \\"4\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"fb18f1d7-0f6c-4b13-8d42-38eef9aa72d9\\"}, {\\"type\\": \\"featured_projects\\", \\"value\\": {\\"heading\\": \\"Udvalgte projekter\\", \\"subheading\\": \\"Se eksempler p\\\\u00e5 vores seneste arbejde og f\\\\u00e5 inspiration til dit n\\\\u00e6ste projekt\\", \\"show_all_link\\": true, \\"all_projects_page\\": 4, \\"columns\\": \\"3\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"90037c54-259e-4132-8d90-128931be7ceb\\"}, {\\"type\\": \\"services_grid_inline\\", \\"value\\": {\\"heading\\": \\"Vores services\\", \\"items\\": [{\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"K\\\\u00f8kkenrenovering\\", \\"description\\": \\"Totalrenovering af k\\\\u00f8kkener med skr\\\\u00e6ddersyede l\\\\u00f8sninger, kvalitetsmaterialer og moderne design\\", \\"icon\\": \\"check\\"}, \\"id\\": \\"338dfc7d-5ee7-433d-927d-42d4d25005f1\\"}], \\"columns\\": \\"3\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"3d581778-17de-45f9-b911-fa5da29ca790\\"}]", "live": true, "path": "00010002", "slug": "home-1", "depth": 2, "intro": "<p data-block-key=\\"fichi\\">Professionelle bygge- og renoveringsløsninger med fokus på kvalitet og håndværk</p>", "owner": null, "title": "Velkommen til JCleemannByg", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 1, "url_path": "/home-1/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Velkommen til JCleemannByg", "content_type": 49, "live_revision": 4, "show_in_menus": false, "latest_revision": 4, "translation_key": "3fc166df-3682-476a-ba86-e93c617785c0", "last_published_at": "2025-09-11T13:45:56.761Z", "first_published_at": "2025-09-11T13:45:14.529Z", "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": false, "latest_revision_created_at": "2025-09-11T13:45:56.742Z"}	\N	3	1	49	1	Velkommen til JCleemannByg
6	2025-09-11 14:01:51.176786+00	{"pk": 3, "body": "[{\\"type\\": \\"hero_v2\\", \\"value\\": {\\"heading\\": \\"Professionelle byggel\\\\u00f8sninger i K\\\\u00f8benhavn og omegn\\", \\"subheading\\": \\"Fra k\\\\u00f8kkenrenovering til komplette nybyggerier - vi leverer h\\\\u00e5ndv\\\\u00e6rk af h\\\\u00f8jeste kvalitet med fokus p\\\\u00e5 kundetilfredshed og termintro fastholding.\\", \\"primary_text\\": \\"F\\\\u00e5 et uforpligtende tilbud\\", \\"primary_page\\": 5, \\"secondary_text\\": \\"Se vores projekter\\", \\"secondary_page\\": 4, \\"image\\": null, \\"style\\": {\\"background\\": \\"hero\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"3475c607-30ae-48b8-bbd5-93b14c9218cb\\"}, {\\"type\\": \\"trust_badges\\", \\"value\\": {\\"heading\\": \\"Derfor v\\\\u00e6lger kunder JCleemannByg\\", \\"items\\": [{\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"Kvalitet i hver detalje\\", \\"description\\": \\"Vi g\\\\u00e5r aldrig p\\\\u00e5 kompromis med kvaliteten. Alle materialer og h\\\\u00e5ndv\\\\u00e6rk lever op til de h\\\\u00f8jeste standarder.\\", \\"icon\\": \\"star\\"}, \\"id\\": \\"01c444da-75ef-4754-9251-081ae07a8dcd\\"}, {\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"Altid til tiden\\", \\"description\\": \\"Vi overholder altid vores deadlines og leverer projekter til tiden. Planl\\\\u00e6gning og p\\\\u00e5lidelighed er i h\\\\u00f8js\\\\u00e6det.\\", \\"icon\\": \\"clock\\"}, \\"id\\": \\"95a47f2f-fad0-4b0e-a08e-7ad574fee53d\\"}], \\"columns\\": \\"4\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"fb18f1d7-0f6c-4b13-8d42-38eef9aa72d9\\"}, {\\"type\\": \\"featured_projects\\", \\"value\\": {\\"heading\\": \\"Udvalgte projekter\\", \\"subheading\\": \\"Se eksempler p\\\\u00e5 vores seneste arbejde og f\\\\u00e5 inspiration til dit n\\\\u00e6ste projekt\\", \\"show_all_link\\": true, \\"all_projects_page\\": 4, \\"columns\\": \\"3\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"90037c54-259e-4132-8d90-128931be7ceb\\"}, {\\"type\\": \\"services_grid_inline\\", \\"value\\": {\\"heading\\": \\"Vores services\\", \\"items\\": [{\\"type\\": \\"item\\", \\"value\\": {\\"title\\": \\"K\\\\u00f8kkenrenovering\\", \\"description\\": \\"Totalrenovering af k\\\\u00f8kkener med skr\\\\u00e6ddersyede l\\\\u00f8sninger, kvalitetsmaterialer og moderne design\\", \\"icon\\": \\"check\\"}, \\"id\\": \\"338dfc7d-5ee7-433d-927d-42d4d25005f1\\"}], \\"columns\\": \\"3\\", \\"style\\": {\\"background\\": \\"surface\\", \\"spacing\\": \\"md\\", \\"container\\": \\"normal\\", \\"divider\\": false}}, \\"id\\": \\"3d581778-17de-45f9-b911-fa5da29ca790\\"}]", "live": true, "path": "00010002", "slug": "home-1", "depth": 2, "intro": "<p data-block-key=\\"fichi\\">Professionelle bygge- og renoveringsløsninger med fokus på kvalitet og håndværk</p>", "owner": null, "title": "Velkommen til JCleemannByg", "locale": 1, "locked": false, "expired": false, "alias_of": null, "numchild": 1, "url_path": "/home-1/", "expire_at": null, "locked_at": null, "locked_by": null, "seo_title": "", "go_live_at": null, "draft_title": "Velkommen til JCleemannByg", "content_type": 49, "live_revision": 4, "show_in_menus": false, "latest_revision": 5, "translation_key": "3fc166df-3682-476a-ba86-e93c617785c0", "last_published_at": "2025-09-11T13:45:56.761Z", "first_published_at": "2025-09-11T13:45:14.529Z", "search_description": "", "wagtail_admin_comments": [], "has_unpublished_changes": true, "latest_revision_created_at": "2025-09-11T13:59:35.636Z"}	\N	3	1	49	1	Velkommen til JCleemannByg
\.


--
-- TOC entry 4296 (class 0 OID 16627)
-- Dependencies: 305
-- Data for Name: wagtailcore_site; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_site (id, hostname, port, is_default_site, root_page_id, site_name) FROM stdin;
1	localhost	80	t	3	
\.


--
-- TOC entry 4298 (class 0 OID 16633)
-- Dependencies: 307
-- Data for Name: wagtailcore_task; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_task (id, name, active, content_type_id) FROM stdin;
1	Moderators approval	t	2
\.


--
-- TOC entry 4300 (class 0 OID 16637)
-- Dependencies: 309
-- Data for Name: wagtailcore_taskstate; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_taskstate (id, status, started_at, finished_at, content_type_id, revision_id, task_id, workflow_state_id, finished_by_id, comment) FROM stdin;
\.


--
-- TOC entry 4302 (class 0 OID 16643)
-- Dependencies: 311
-- Data for Name: wagtailcore_uploadedfile; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_uploadedfile (id, file, for_content_type_id, uploaded_by_user_id) FROM stdin;
\.


--
-- TOC entry 4304 (class 0 OID 16647)
-- Dependencies: 313
-- Data for Name: wagtailcore_workflow; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflow (id, name, active) FROM stdin;
1	Moderators approval	t
\.


--
-- TOC entry 4306 (class 0 OID 16651)
-- Dependencies: 315
-- Data for Name: wagtailcore_workflowcontenttype; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflowcontenttype (content_type_id, workflow_id) FROM stdin;
\.


--
-- TOC entry 4307 (class 0 OID 16654)
-- Dependencies: 316
-- Data for Name: wagtailcore_workflowpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflowpage (page_id, workflow_id) FROM stdin;
1	1
\.


--
-- TOC entry 4308 (class 0 OID 16657)
-- Dependencies: 317
-- Data for Name: wagtailcore_workflowstate; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflowstate (id, status, created_at, current_task_state_id, object_id, requested_by_id, workflow_id, content_type_id, base_content_type_id) FROM stdin;
\.


--
-- TOC entry 4310 (class 0 OID 16661)
-- Dependencies: 319
-- Data for Name: wagtailcore_workflowtask; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflowtask (id, sort_order, task_id, workflow_id) FROM stdin;
1	0	1	1
\.


--
-- TOC entry 4312 (class 0 OID 16665)
-- Dependencies: 321
-- Data for Name: wagtaildocs_document; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtaildocs_document (id, title, file, created_at, uploaded_by_user_id, collection_id, file_size, file_hash) FROM stdin;
\.


--
-- TOC entry 4314 (class 0 OID 16670)
-- Dependencies: 323
-- Data for Name: wagtailembeds_embed; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailembeds_embed (id, url, max_width, type, html, title, author_name, provider_name, thumbnail_url, width, height, last_updated, hash, cache_until) FROM stdin;
\.


--
-- TOC entry 4316 (class 0 OID 16676)
-- Dependencies: 325
-- Data for Name: wagtailforms_formsubmission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailforms_formsubmission (id, form_data, submit_time, page_id) FROM stdin;
\.


--
-- TOC entry 4318 (class 0 OID 16682)
-- Dependencies: 327
-- Data for Name: wagtailimages_image; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailimages_image (id, title, file, width, height, created_at, focal_point_x, focal_point_y, focal_point_width, focal_point_height, uploaded_by_user_id, file_size, collection_id, file_hash, description) FROM stdin;
90	alternativeHand1.jpg	original_images/stock_mediaproject_imagesalternativeHand1_I3qFEal.jpg	1280	960	2025-09-12 11:36:07.191033+00	\N	\N	\N	\N	\N	\N	1		
91	carpenter1.jpg	original_images/stock_mediaproject_imagescarpenter1_XigJI98.jpg	1280	850	2025-09-12 11:36:07.23784+00	\N	\N	\N	\N	\N	\N	1		
92	carpenter2.jpg	original_images/stock_mediaproject_imagescarpenter2_LuyXyfP.jpg	1280	857	2025-09-12 11:36:07.253819+00	\N	\N	\N	\N	\N	\N	1		
93	carpenter3.png	original_images/stock_mediaproject_imagescarpenter3_Da0kPWu.png	1280	1280	2025-09-12 11:36:07.330164+00	\N	\N	\N	\N	\N	\N	1		
94	handwork1.jpg	original_images/stock_mediaproject_imageshandwork1_zQrVLXF.jpg	1280	853	2025-09-12 11:36:07.377591+00	\N	\N	\N	\N	\N	\N	1		
95	roof1.jpg	original_images/stock_mediaproject_imagesroof1_GAMVOzm.jpg	1280	679	2025-09-12 11:36:07.424297+00	\N	\N	\N	\N	\N	\N	1		
96	woodworking1.jpg	original_images/stock_mediaproject_imageswoodworking1_omXBZy6.jpg	1280	853	2025-09-12 11:36:07.468768+00	\N	\N	\N	\N	\N	\N	1		
97	JcleemannbygLogo_transparent	original_images/JcleemannbygLogo_transparent.png	1024	1024	2025-09-12 11:54:25.885621+00	\N	\N	\N	\N	1	1382984	1	1083305a9bc350b4e116f5a52e3142459782ec13	
\.


--
-- TOC entry 4320 (class 0 OID 16693)
-- Dependencies: 329
-- Data for Name: wagtailimages_rendition; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailimages_rendition (id, file, width, height, focal_point_key, filter_spec, image_id) FROM stdin;
43	images/stock_mediaproject_imageswoodworking1_omXBZy6.width-400.jpg	400	266		width-400	96
44	images/stock_mediaproject_imagesroof1_GAMVOzm.width-400.jpg	400	212		width-400	95
45	images/stock_mediaproject_imageshandwork1_zQrVLXF.width-400.jpg	400	266		width-400	94
46	images/stock_mediaproject_imagescarpenter1_XigJI98.width-400.jpg	400	265		width-400	91
47	images/stock_mediaproject_imagesalternativeHand1_I3qF.width-400.jpg	400	300		width-400	90
48	images/stock_mediaproject_imagescarpenter1_XigJI98.width-1200.jpg	1200	796		width-1200	91
49	images/stock_mediaproject_imagescarpenter2_LuyXyfP.width-600.jpg	600	401		width-600	92
50	images/stock_mediaproject_imagescarpenter3_Da0kPWu.width-600.png	600	600		width-600	93
51	images/stock_mediaproject_imagesalternati.2e16d0ba.fill-400x300.jpg	400	300	2e16d0ba	fill-400x300	90
52	images/stock_mediaproject_imageswoodworking1_omXBZy6.width-1200.jpg	1200	799		width-1200	96
54	images/stock_mediaproject_imageswoodworking1_omXBZy.max-165x165.jpg	165	109		max-165x165	96
55	images/stock_mediaproject_imagesroof1_GAMVOzm.max-165x165.jpg	165	87		max-165x165	95
56	images/stock_mediaproject_imageshandwork1_zQrVLXF.max-165x165.jpg	165	109		max-165x165	94
57	images/stock_mediaproject_imagescarpenter3_Da0kPWu.max-165x165.png	165	165		max-165x165	93
58	images/stock_mediaproject_imagescarpenter2_LuyXyfP.max-165x165.jpg	165	110		max-165x165	92
59	images/stock_mediaproject_imagescarpenter1_XigJI98.max-165x165.jpg	165	109		max-165x165	91
60	images/stock_mediaproject_imagesalternativeHand1_I3.max-165x165.jpg	165	123		max-165x165	90
74	images/JcleemannbygLogo_transparent.max-165x165.png	165	165		max-165x165	97
75	images/JcleemannbygLogo_transparent.width-1200.png	1024	1024		width-1200	97
76	images/JcleemannbygLogo_transparent.width-600.png	600	600		width-600	97
77	images/JcleemannbygLogo_transparent.width-40.png	40	40		width-40	97
\.


--
-- TOC entry 4322 (class 0 OID 16697)
-- Dependencies: 331
-- Data for Name: wagtailredirects_redirect; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailredirects_redirect (id, old_path, is_permanent, redirect_link, redirect_page_id, site_id, automatically_created, created_at, redirect_page_route_path) FROM stdin;
\.


--
-- TOC entry 4324 (class 0 OID 16703)
-- Dependencies: 333
-- Data for Name: wagtailsearch_indexentry; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailsearch_indexentry (id, object_id, title_norm, content_type_id, autocomplete, title, body) FROM stdin;
32	10	0.7724137931034483	41		'køkken':5 'og':3 'terrass':2 'træ':1 'udendør':4	'45m²':21 'aftentim':34 'belysn':32 'blev':42 'brugt':36 'budget':48 'bygget':8 'en':9 'fantastisk':10 'færdiggjort':43 'grill':23 'har':7 'indbygget':22 'integreret':13 'kogezon':25 'køkken':3,15 'led':31 'led-belysn':30 'lærketræ':18,37 'material':35 'med':12 'natursten':40 'og':4,24,46 'omfatt':17 'opbevaringsløsning':26 'projektet':16,41 'på':20 'rustfrit':38 'smukt':1 'stål':39 'terrass':5,19 'tiden':45 'til':33,44 'træ':29 'træterrass':11 'udendør':2,14 'vejrbestandigt':28 'vi':6 'within':47
4	4	3.0504201680672267	51	'ad':5 'aliquip':15 'commodo':18 'consequat':19 'ea':17 'enim':4 'ex':16 'exercitation':10 'galleri':2 'laboris':12 'minim':6 'nisi':13 'nostrud':9 'projekt':1 'quis':8 'ullamco':11 'ut':3,14 'veniam':7	'galleri':2B 'projekt':1B	'ad':3 'aliquip':13 'commodo':16 'consequat':17 'ea':15 'enim':2 'ex':14 'exercit':8 'labori':10 'minim':4 'nisi':11 'nostrud':7 'qui':6 'ullamco':9 'ut':1,12 'veniam':5
38	13	1.9310344827586208	41		'badeværels':1 'renov':2	'af':5,26 'badekar':12 'badeværels':2,7,23 'der':24 'et':19 'fliser':10 'fritståend':11 'fuldstændig':3 'italiensk':8 'komfort':29 'lignend':22 'luksuriøst':1 'luksus':27 'marmor':9 'master':6 'med':14 'møbel':18 'og':28 'oser':25 'regnbrus':13 'renov':4 'skræddersyet':16 'spa':21 'spa-lignend':20 'termostat':15 'vask':17
40	14	1.9310344827586208	41		'kontorbygn':2 'modern':1	'af':7 'arbejdsmiljø':36 'byggeriet':17 'bæredygtig':13 'bæredygtigh':5 'der':29 'energieffektiv':23 'erhvervsprojekt':1 'et':32 'fleksibl':27 'fokus':3 'glasparti':19 'hele':16 'kan':30 'kontorbygn':9 'kontorrum':28 'lys':22 'material':14 'med':2 'miljøvenligt':35 'mindr':11 'modern':8,33 'naturligt':21 'og':25,34 'opførels':6 'på':4 'store':18 'tilpass':31 'varm':24 'ventilationsystem':26 'virksomh':12
65	1	6.11864406779661	1	'root':1	'root':1B	
7	5	1.9310344827586208	50	'besked':6 'en':5 'kontakt':1 'os':2,4 'send':3	'kontakt':1B 'os':2B	'anim':34 'aut':2 'besk':20 'cillum':11 'culpa':29 'cupidatat':24 'deserunt':32 'dolor':4,12 'dui':1 'en':19 'ess':10 'est':36 'eu':13 'excepteur':21 'fugiat':14 'id':35 'irur':3 'laborum':37 'mollit':33 'non':25 'nulla':15 'occaecat':23 'officia':31 'os':18 'pariatur':16 'proident':26 'qui':30 'reprehenderit':6 'send':17 'sint':22 'sunt':27 'velit':9 'volupt':8
34	11	1.2873563218390804	41		'københavn':4 'renov':2 'villa':1	'1920':10 'af':2,7,19,23,32 'arkitektur':17 'badeværels':26 'den':15 'eksempel':37 'energioptim':27 'ern':11 'et':35 'familierum':34 'foren':45 'fra':9 'harmonisk':46 'histori':40 'historisk':3 'hvordan':39 'kan':44 'komfort':43 'komplet':5 'køkken':24 'med':12,28 'modern':33,42 'modernis':22 'nye':29 'og':25,41 'oprindelig':16 'original':20 'på':38 'renov':6 'respekt':13 'restaur':18 'smukt':36 'tilbygn':31 'totalrenov':1 'trægulv':21 'villa':4,8 'vinduer':30
36	12	1.2873563218390804	41		'instal':3 'køkken':2 'skræddersyet':1	'af':30 'all':26 'behov':16 'belysn':36 'bordplad':22 'bygget':7 'både':41 'corian':21 'der':11 'designet':5 'efter':3 'eg':18 'er':40 'et':8 'funktionelt':42 'hvidevar':29 'håndlavet':1 'højder':27 'højest':31 'integrered':28 'kunden':15 'kvalitet':32 'køkken':2,10 'køkkenet':39 'køkkenø':19 'led':35 'led-belysn':34 'massiv':17 'med':20 'mål':4 'og':6,43 'passer':12 'perfekt':13 'skabe':24,38 'skjult':33 'skræddersyed':23 'smukt':45 'til':14 'unikt':9 'æstetisk':44
257	25	3.5183823529411766	41		'project':2 'roof':1	
235	15	8.166666666666666	41		'alternativehand1':1	
237	16	8.043103448275863	41		'carpenter1':1	
239	17	7.923728813559322	41		'carpenter2':1	
241	18	7.808333333333334	41		'carpenter3':1	
243	19	7.69672131147541	41		'handwork1':1	
245	20	7.588709677419355	41		'roof1':1	
247	21	7.484126984126984	41		'woodworking1':1	
249	22	3.6953125	41		'alternativehand':1 'project':2	
251	23	3.65	41		'carpent':1 'project':2	
255	24	3.5597014925373136	41		'handwork':1 'project':2	
259	26	3.4782608695652173	41		'project':2 'woodwork':1	
264	90	6.836879432624113	26	'alternativehand1.jpg':1	'alternativehand1.jpg':1A	
274	94	6.612244897959184	26	'handwork1.jpg':1	'handwork1.jpg':1A	
282	96	6.47682119205298	26	'woodworking1.jpg':1	'woodworking1.jpg':1A	
268	91	6.7622377622377625	26	'carpenter1.jpg':1	'carpenter1.jpg':1A	
269	92	6.722222222222222	26	'carpenter2.jpg':1	'carpenter2.jpg':1A	
270	93	6.682758620689655	26	'carpenter3.png':1	'carpenter3.png':1A	
278	95	6.543624161073826	26	'roof1.jpg':1	'roof1.jpg':1A	
283	97	3.223684210526316	26	'jcleemannbyglogo':1 'transparent':2	'jcleemannbyglogo':1A 'transpar':2A	
1	3	1.9405684754521964	49	'bygge':6 'fokus':10 'håndværk':14 'jcleemannbyg':3 'kvalitet':12 'med':9 'og':7,13 'professionelle':5 'på':11 'renoveringsløsninger':8 'template':4 'til':2 'velkommen':1	'jcleemannbyg':3B 'til':2B 'velkommen':1B	'3':115,133 '4':96 'af':27,123 'aldrig':58 'all':63 'altid':75,80 'arbejd':107 'bygg':3 'byggeløsning':14 'check':132 'clock':94 'de':70 'deadlin':82 'derfor':48 'design':131 'detalj':55 'dit':112 'eksempl':103 'er':91 'et':38 'fasthold':36 'fokus':7,31 'fra':19 'få':37,109 'gradient':45 'går':57 'hero':44 'hver':54 'håndværk':11,26,66 'højest':28,71 'højsædet':93 'inspir':110 'jcleemannbyg':51 'komplett':22 'kompromi':60 'kunder':50 'kundetilfredsh':33 'kvalitet':9,29,52 'kvaliteten':62 'kvalitetsmaterial':128 'københavn':16 'køkkener':124 'køkkenrenov':20,121 'lever':25,67,84 'løsninger':127 'material':64 'med':6,30,61,125 'medium':46,98,117,135 'modern':130 'normal':47,99,118,136 'nybyggeri':23 'næste':113 'og':4,10,17,34,65,83,89,108,129 'omegn':18 'op':68 'overhold':79 'planlægn':88 'professionell':2,13 'projekt':43,85,101,114 'på':8,32,59,104 'pålideligh':90 'qualiti':74 'renoveringsløsning':5 'se':41,102 'senest':106 'servicesaa':120 'skræddersyed':126 'standard':72 'star':73 'surfac':97,116,134 'temp':12 'templat':1 'termintro':35 'tiden':77,87 'til':21,69,76,86,111 'tilbud':40 'time':95 'totalrenov':122 'udvalgt':100 'uforpligtend':39 'vi':24,56,78 'vore':42,81,105,119 'vælger':49
\.


--
-- TOC entry 4326 (class 0 OID 16709)
-- Dependencies: 335
-- Data for Name: wagtailsearchpromotions_query; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailsearchpromotions_query (id, query_string) FROM stdin;
1	project
2	hej
\.


--
-- TOC entry 4328 (class 0 OID 16713)
-- Dependencies: 337
-- Data for Name: wagtailsearchpromotions_querydailyhits; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailsearchpromotions_querydailyhits (id, date, hits, query_id) FROM stdin;
1	2025-09-11	6	1
2	2025-09-11	1	2
\.


--
-- TOC entry 4330 (class 0 OID 16717)
-- Dependencies: 339
-- Data for Name: wagtailsearchpromotions_searchpromotion; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailsearchpromotions_searchpromotion (id, sort_order, description, page_id, query_id, external_link_text, external_link_url) FROM stdin;
\.


--
-- TOC entry 4332 (class 0 OID 16723)
-- Dependencies: 341
-- Data for Name: wagtailusers_userprofile; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailusers_userprofile (id, submitted_notifications, approved_notifications, rejected_notifications, user_id, preferred_language, current_time_zone, avatar, updated_comments_notifications, dismissibles, theme, density, contrast, keyboard_shortcuts) FROM stdin;
\.


--
-- TOC entry 4339 (class 0 OID 0)
-- Dependencies: 215
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 2, true);


--
-- TOC entry 4340 (class 0 OID 0)
-- Dependencies: 217
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 18, true);


--
-- TOC entry 4341 (class 0 OID 0)
-- Dependencies: 219
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 254, true);


--
-- TOC entry 4342 (class 0 OID 0)
-- Dependencies: 222
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- TOC entry 4343 (class 0 OID 0)
-- Dependencies: 223
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- TOC entry 4344 (class 0 OID 0)
-- Dependencies: 225
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 4345 (class 0 OID 0)
-- Dependencies: 227
-- Name: contacts_contactsubmission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.contacts_contactsubmission_id_seq', 1, false);


--
-- TOC entry 4346 (class 0 OID 0)
-- Dependencies: 229
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- TOC entry 4347 (class 0 OID 0)
-- Dependencies: 231
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 63, true);


--
-- TOC entry 4348 (class 0 OID 0)
-- Dependencies: 233
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 250, true);


--
-- TOC entry 4349 (class 0 OID 0)
-- Dependencies: 236
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_site_id_seq', 1, true);


--
-- TOC entry 4350 (class 0 OID 0)
-- Dependencies: 241
-- Name: pages_logo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pages_logo_id_seq', 1, false);


--
-- TOC entry 4351 (class 0 OID 0)
-- Dependencies: 244
-- Name: pages_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pages_service_id_seq', 1, false);


--
-- TOC entry 4352 (class 0 OID 0)
-- Dependencies: 246
-- Name: pages_sitesettings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pages_sitesettings_id_seq', 1, true);


--
-- TOC entry 4353 (class 0 OID 0)
-- Dependencies: 248
-- Name: pages_testimonial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pages_testimonial_id_seq', 1, false);


--
-- TOC entry 4354 (class 0 OID 0)
-- Dependencies: 250
-- Name: projects_project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.projects_project_id_seq', 26, true);


--
-- TOC entry 4355 (class 0 OID 0)
-- Dependencies: 252
-- Name: projects_projectimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.projects_projectimage_id_seq', 28, true);


--
-- TOC entry 4356 (class 0 OID 0)
-- Dependencies: 255
-- Name: projects_projectpageimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.projects_projectpageimage_id_seq', 67, true);


--
-- TOC entry 4357 (class 0 OID 0)
-- Dependencies: 257
-- Name: projects_projectpagetag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.projects_projectpagetag_id_seq', 18, true);


--
-- TOC entry 4358 (class 0 OID 0)
-- Dependencies: 259
-- Name: projects_projecttag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.projects_projecttag_id_seq', 1, false);


--
-- TOC entry 4359 (class 0 OID 0)
-- Dependencies: 261
-- Name: taggit_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.taggit_tag_id_seq', 16, true);


--
-- TOC entry 4360 (class 0 OID 0)
-- Dependencies: 263
-- Name: taggit_taggeditem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.taggit_taggeditem_id_seq', 1, false);


--
-- TOC entry 4361 (class 0 OID 0)
-- Dependencies: 265
-- Name: wagtailadmin_admin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailadmin_admin_id_seq', 1, false);


--
-- TOC entry 4362 (class 0 OID 0)
-- Dependencies: 267
-- Name: wagtailadmin_editingsession_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailadmin_editingsession_id_seq', 13, true);


--
-- TOC entry 4363 (class 0 OID 0)
-- Dependencies: 269
-- Name: wagtailcore_collection_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_collection_id_seq', 1, true);


--
-- TOC entry 4364 (class 0 OID 0)
-- Dependencies: 272
-- Name: wagtailcore_collectionviewrestriction_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_collectionviewrestriction_groups_id_seq', 1, false);


--
-- TOC entry 4365 (class 0 OID 0)
-- Dependencies: 273
-- Name: wagtailcore_collectionviewrestriction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_collectionviewrestriction_id_seq', 1, false);


--
-- TOC entry 4366 (class 0 OID 0)
-- Dependencies: 275
-- Name: wagtailcore_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_comment_id_seq', 1, false);


--
-- TOC entry 4367 (class 0 OID 0)
-- Dependencies: 277
-- Name: wagtailcore_commentreply_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_commentreply_id_seq', 1, false);


--
-- TOC entry 4368 (class 0 OID 0)
-- Dependencies: 280
-- Name: wagtailcore_groupapprovaltask_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_groupapprovaltask_groups_id_seq', 1, true);


--
-- TOC entry 4369 (class 0 OID 0)
-- Dependencies: 282
-- Name: wagtailcore_groupcollectionpermission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_groupcollectionpermission_id_seq', 12, true);


--
-- TOC entry 4370 (class 0 OID 0)
-- Dependencies: 284
-- Name: wagtailcore_grouppagepermission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_grouppagepermission_id_seq', 7, true);


--
-- TOC entry 4371 (class 0 OID 0)
-- Dependencies: 286
-- Name: wagtailcore_groupsitepermission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_groupsitepermission_id_seq', 1, false);


--
-- TOC entry 4372 (class 0 OID 0)
-- Dependencies: 288
-- Name: wagtailcore_locale_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_locale_id_seq', 1, true);


--
-- TOC entry 4373 (class 0 OID 0)
-- Dependencies: 290
-- Name: wagtailcore_modellogentry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_modellogentry_id_seq', 2, true);


--
-- TOC entry 4374 (class 0 OID 0)
-- Dependencies: 292
-- Name: wagtailcore_page_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_page_id_seq', 38, true);


--
-- TOC entry 4375 (class 0 OID 0)
-- Dependencies: 294
-- Name: wagtailcore_pagelogentry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pagelogentry_id_seq', 113, true);


--
-- TOC entry 4376 (class 0 OID 0)
-- Dependencies: 296
-- Name: wagtailcore_pagerevision_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pagerevision_id_seq', 38, true);


--
-- TOC entry 4377 (class 0 OID 0)
-- Dependencies: 298
-- Name: wagtailcore_pagesubscription_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pagesubscription_id_seq', 6, true);


--
-- TOC entry 4378 (class 0 OID 0)
-- Dependencies: 301
-- Name: wagtailcore_pageviewrestriction_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pageviewrestriction_groups_id_seq', 1, false);


--
-- TOC entry 4379 (class 0 OID 0)
-- Dependencies: 302
-- Name: wagtailcore_pageviewrestriction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pageviewrestriction_id_seq', 1, false);


--
-- TOC entry 4380 (class 0 OID 0)
-- Dependencies: 304
-- Name: wagtailcore_referenceindex_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_referenceindex_id_seq', 199, true);


--
-- TOC entry 4381 (class 0 OID 0)
-- Dependencies: 306
-- Name: wagtailcore_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_site_id_seq', 1, true);


--
-- TOC entry 4382 (class 0 OID 0)
-- Dependencies: 308
-- Name: wagtailcore_task_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_task_id_seq', 1, true);


--
-- TOC entry 4383 (class 0 OID 0)
-- Dependencies: 310
-- Name: wagtailcore_taskstate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_taskstate_id_seq', 1, false);


--
-- TOC entry 4384 (class 0 OID 0)
-- Dependencies: 312
-- Name: wagtailcore_uploadedfile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_uploadedfile_id_seq', 1, false);


--
-- TOC entry 4385 (class 0 OID 0)
-- Dependencies: 314
-- Name: wagtailcore_workflow_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_workflow_id_seq', 1, true);


--
-- TOC entry 4386 (class 0 OID 0)
-- Dependencies: 318
-- Name: wagtailcore_workflowstate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_workflowstate_id_seq', 1, false);


--
-- TOC entry 4387 (class 0 OID 0)
-- Dependencies: 320
-- Name: wagtailcore_workflowtask_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_workflowtask_id_seq', 1, true);


--
-- TOC entry 4388 (class 0 OID 0)
-- Dependencies: 322
-- Name: wagtaildocs_document_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtaildocs_document_id_seq', 1, false);


--
-- TOC entry 4389 (class 0 OID 0)
-- Dependencies: 324
-- Name: wagtailembeds_embed_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailembeds_embed_id_seq', 1, false);


--
-- TOC entry 4390 (class 0 OID 0)
-- Dependencies: 326
-- Name: wagtailforms_formsubmission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailforms_formsubmission_id_seq', 1, false);


--
-- TOC entry 4391 (class 0 OID 0)
-- Dependencies: 328
-- Name: wagtailimages_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailimages_image_id_seq', 97, true);


--
-- TOC entry 4392 (class 0 OID 0)
-- Dependencies: 330
-- Name: wagtailimages_rendition_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailimages_rendition_id_seq', 90, true);


--
-- TOC entry 4393 (class 0 OID 0)
-- Dependencies: 332
-- Name: wagtailredirects_redirect_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailredirects_redirect_id_seq', 1, false);


--
-- TOC entry 4394 (class 0 OID 0)
-- Dependencies: 334
-- Name: wagtailsearch_indexentry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailsearch_indexentry_id_seq', 296, true);


--
-- TOC entry 4395 (class 0 OID 0)
-- Dependencies: 336
-- Name: wagtailsearchpromotions_query_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailsearchpromotions_query_id_seq', 2, true);


--
-- TOC entry 4396 (class 0 OID 0)
-- Dependencies: 338
-- Name: wagtailsearchpromotions_querydailyhits_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailsearchpromotions_querydailyhits_id_seq', 2, true);


--
-- TOC entry 4397 (class 0 OID 0)
-- Dependencies: 340
-- Name: wagtailsearchpromotions_searchpromotion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailsearchpromotions_searchpromotion_id_seq', 1, false);


--
-- TOC entry 4398 (class 0 OID 0)
-- Dependencies: 342
-- Name: wagtailusers_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailusers_userprofile_id_seq', 1, false);


--
-- TOC entry 3604 (class 2606 OID 16732)
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 3609 (class 2606 OID 16734)
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- TOC entry 3612 (class 2606 OID 16736)
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3606 (class 2606 OID 16738)
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 3615 (class 2606 OID 16740)
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- TOC entry 3617 (class 2606 OID 16742)
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 3625 (class 2606 OID 16744)
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 3628 (class 2606 OID 16746)
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- TOC entry 3619 (class 2606 OID 16748)
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- TOC entry 3631 (class 2606 OID 16750)
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3634 (class 2606 OID 16752)
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- TOC entry 3622 (class 2606 OID 16754)
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- TOC entry 3636 (class 2606 OID 16756)
-- Name: contacts_contactsubmission contacts_contactsubmission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contacts_contactsubmission
    ADD CONSTRAINT contacts_contactsubmission_pkey PRIMARY KEY (id);


--
-- TOC entry 3640 (class 2606 OID 16758)
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 3643 (class 2606 OID 16760)
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- TOC entry 3645 (class 2606 OID 16762)
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 3647 (class 2606 OID 16764)
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 3650 (class 2606 OID 16766)
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 3654 (class 2606 OID 16768)
-- Name: django_site django_site_domain_a2e37b91_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE (domain);


--
-- TOC entry 3656 (class 2606 OID 16770)
-- Name: django_site django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- TOC entry 3658 (class 2606 OID 16772)
-- Name: pages_contactpage pages_contactpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_contactpage
    ADD CONSTRAINT pages_contactpage_pkey PRIMARY KEY (page_ptr_id);


--
-- TOC entry 3660 (class 2606 OID 16774)
-- Name: pages_gallerypage pages_gallerypage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_gallerypage
    ADD CONSTRAINT pages_gallerypage_pkey PRIMARY KEY (page_ptr_id);


--
-- TOC entry 3662 (class 2606 OID 16776)
-- Name: pages_homepage pages_homepage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_homepage
    ADD CONSTRAINT pages_homepage_pkey PRIMARY KEY (page_ptr_id);


--
-- TOC entry 3665 (class 2606 OID 16778)
-- Name: pages_logo pages_logo_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_logo
    ADD CONSTRAINT pages_logo_pkey PRIMARY KEY (id);


--
-- TOC entry 3667 (class 2606 OID 16780)
-- Name: pages_modularpage pages_modularpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_modularpage
    ADD CONSTRAINT pages_modularpage_pkey PRIMARY KEY (page_ptr_id);


--
-- TOC entry 3669 (class 2606 OID 16782)
-- Name: pages_service pages_service_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_service
    ADD CONSTRAINT pages_service_pkey PRIMARY KEY (id);


--
-- TOC entry 3673 (class 2606 OID 16784)
-- Name: pages_sitesettings pages_sitesettings_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_sitesettings
    ADD CONSTRAINT pages_sitesettings_pkey PRIMARY KEY (id);


--
-- TOC entry 3675 (class 2606 OID 16786)
-- Name: pages_sitesettings pages_sitesettings_site_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_sitesettings
    ADD CONSTRAINT pages_sitesettings_site_id_key UNIQUE (site_id);


--
-- TOC entry 3677 (class 2606 OID 16788)
-- Name: pages_testimonial pages_testimonial_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_testimonial
    ADD CONSTRAINT pages_testimonial_pkey PRIMARY KEY (id);


--
-- TOC entry 3679 (class 2606 OID 16790)
-- Name: projects_project projects_project_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_project
    ADD CONSTRAINT projects_project_pkey PRIMARY KEY (id);


--
-- TOC entry 3682 (class 2606 OID 16792)
-- Name: projects_project projects_project_slug_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_project
    ADD CONSTRAINT projects_project_slug_key UNIQUE (slug);


--
-- TOC entry 3685 (class 2606 OID 16794)
-- Name: projects_projectimage projects_projectimage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectimage
    ADD CONSTRAINT projects_projectimage_pkey PRIMARY KEY (id);


--
-- TOC entry 3688 (class 2606 OID 16796)
-- Name: projects_projectpage projects_projectpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpage
    ADD CONSTRAINT projects_projectpage_pkey PRIMARY KEY (page_ptr_id);


--
-- TOC entry 3691 (class 2606 OID 16798)
-- Name: projects_projectpageimage projects_projectpageimage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpageimage
    ADD CONSTRAINT projects_projectpageimage_pkey PRIMARY KEY (id);


--
-- TOC entry 3695 (class 2606 OID 16800)
-- Name: projects_projectpagetag projects_projectpagetag_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpagetag
    ADD CONSTRAINT projects_projectpagetag_pkey PRIMARY KEY (id);


--
-- TOC entry 3699 (class 2606 OID 16802)
-- Name: projects_projecttag projects_projecttag_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projecttag
    ADD CONSTRAINT projects_projecttag_pkey PRIMARY KEY (id);


--
-- TOC entry 3703 (class 2606 OID 16804)
-- Name: taggit_tag taggit_tag_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_tag
    ADD CONSTRAINT taggit_tag_name_key UNIQUE (name);


--
-- TOC entry 3705 (class 2606 OID 16806)
-- Name: taggit_tag taggit_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_tag
    ADD CONSTRAINT taggit_tag_pkey PRIMARY KEY (id);


--
-- TOC entry 3708 (class 2606 OID 16808)
-- Name: taggit_tag taggit_tag_slug_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_tag
    ADD CONSTRAINT taggit_tag_slug_key UNIQUE (slug);


--
-- TOC entry 3712 (class 2606 OID 16810)
-- Name: taggit_taggeditem taggit_taggeditem_content_type_id_object_id_tag_id_4bb97a8e_uni; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_content_type_id_object_id_tag_id_4bb97a8e_uni UNIQUE (content_type_id, object_id, tag_id);


--
-- TOC entry 3715 (class 2606 OID 16812)
-- Name: taggit_taggeditem taggit_taggeditem_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_pkey PRIMARY KEY (id);


--
-- TOC entry 3764 (class 2606 OID 16814)
-- Name: wagtailcore_grouppagepermission unique_permission; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission
    ADD CONSTRAINT unique_permission UNIQUE (group_id, page_id, permission_id);


--
-- TOC entry 3718 (class 2606 OID 16816)
-- Name: wagtailadmin_admin wagtailadmin_admin_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailadmin_admin
    ADD CONSTRAINT wagtailadmin_admin_pkey PRIMARY KEY (id);


--
-- TOC entry 3722 (class 2606 OID 16818)
-- Name: wagtailadmin_editingsession wagtailadmin_editingsession_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailadmin_editingsession
    ADD CONSTRAINT wagtailadmin_editingsession_pkey PRIMARY KEY (id);


--
-- TOC entry 3726 (class 2606 OID 16820)
-- Name: wagtailcore_collection wagtailcore_collection_path_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collection
    ADD CONSTRAINT wagtailcore_collection_path_key UNIQUE (path);


--
-- TOC entry 3728 (class 2606 OID 16822)
-- Name: wagtailcore_collection wagtailcore_collection_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collection
    ADD CONSTRAINT wagtailcore_collection_pkey PRIMARY KEY (id);


--
-- TOC entry 3733 (class 2606 OID 16824)
-- Name: wagtailcore_collectionviewrestriction_groups wagtailcore_collectionvi_collectionviewrestrictio_988995ae_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction_groups
    ADD CONSTRAINT wagtailcore_collectionvi_collectionviewrestrictio_988995ae_uniq UNIQUE (collectionviewrestriction_id, group_id);


--
-- TOC entry 3737 (class 2606 OID 16826)
-- Name: wagtailcore_collectionviewrestriction_groups wagtailcore_collectionviewrestriction_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction_groups
    ADD CONSTRAINT wagtailcore_collectionviewrestriction_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 3731 (class 2606 OID 16828)
-- Name: wagtailcore_collectionviewrestriction wagtailcore_collectionviewrestriction_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction
    ADD CONSTRAINT wagtailcore_collectionviewrestriction_pkey PRIMARY KEY (id);


--
-- TOC entry 3740 (class 2606 OID 16830)
-- Name: wagtailcore_comment wagtailcore_comment_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_comment
    ADD CONSTRAINT wagtailcore_comment_pkey PRIMARY KEY (id);


--
-- TOC entry 3746 (class 2606 OID 16832)
-- Name: wagtailcore_commentreply wagtailcore_commentreply_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_commentreply
    ADD CONSTRAINT wagtailcore_commentreply_pkey PRIMARY KEY (id);


--
-- TOC entry 3751 (class 2606 OID 16834)
-- Name: wagtailcore_groupapprovaltask_groups wagtailcore_groupapprova_groupapprovaltask_id_gro_bb5ee7eb_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupapprovaltask_groups
    ADD CONSTRAINT wagtailcore_groupapprova_groupapprovaltask_id_gro_bb5ee7eb_uniq UNIQUE (groupapprovaltask_id, group_id);


--
-- TOC entry 3755 (class 2606 OID 16836)
-- Name: wagtailcore_groupapprovaltask_groups wagtailcore_groupapprovaltask_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupapprovaltask_groups
    ADD CONSTRAINT wagtailcore_groupapprovaltask_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 3749 (class 2606 OID 16838)
-- Name: wagtailcore_groupapprovaltask wagtailcore_groupapprovaltask_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupapprovaltask
    ADD CONSTRAINT wagtailcore_groupapprovaltask_pkey PRIMARY KEY (task_ptr_id);


--
-- TOC entry 3757 (class 2606 OID 16840)
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcollect_group_id_collection_id_p_a21cefe9_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcollect_group_id_collection_id_p_a21cefe9_uniq UNIQUE (group_id, collection_id, permission_id);


--
-- TOC entry 3762 (class 2606 OID 16842)
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcollectionpermission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcollectionpermission_pkey PRIMARY KEY (id);


--
-- TOC entry 3769 (class 2606 OID 16844)
-- Name: wagtailcore_grouppagepermission wagtailcore_grouppagepermission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppagepermission_pkey PRIMARY KEY (id);


--
-- TOC entry 3771 (class 2606 OID 16846)
-- Name: wagtailcore_groupsitepermission wagtailcore_groupsiteper_group_id_site_id_permiss_a58ee30d_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupsitepermission
    ADD CONSTRAINT wagtailcore_groupsiteper_group_id_site_id_permiss_a58ee30d_uniq UNIQUE (group_id, site_id, permission_id);


--
-- TOC entry 3775 (class 2606 OID 16848)
-- Name: wagtailcore_groupsitepermission wagtailcore_groupsitepermission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupsitepermission
    ADD CONSTRAINT wagtailcore_groupsitepermission_pkey PRIMARY KEY (id);


--
-- TOC entry 3779 (class 2606 OID 16850)
-- Name: wagtailcore_locale wagtailcore_locale_language_code_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_locale
    ADD CONSTRAINT wagtailcore_locale_language_code_key UNIQUE (language_code);


--
-- TOC entry 3781 (class 2606 OID 16852)
-- Name: wagtailcore_locale wagtailcore_locale_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_locale
    ADD CONSTRAINT wagtailcore_locale_pkey PRIMARY KEY (id);


--
-- TOC entry 3789 (class 2606 OID 16854)
-- Name: wagtailcore_modellogentry wagtailcore_modellogentry_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_modellogentry
    ADD CONSTRAINT wagtailcore_modellogentry_pkey PRIMARY KEY (id);


--
-- TOC entry 3803 (class 2606 OID 16856)
-- Name: wagtailcore_page wagtailcore_page_path_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_path_key UNIQUE (path);


--
-- TOC entry 3805 (class 2606 OID 16858)
-- Name: wagtailcore_page wagtailcore_page_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_pkey PRIMARY KEY (id);


--
-- TOC entry 3809 (class 2606 OID 16860)
-- Name: wagtailcore_page wagtailcore_page_translation_key_locale_id_9b041bad_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_translation_key_locale_id_9b041bad_uniq UNIQUE (translation_key, locale_id);


--
-- TOC entry 3816 (class 2606 OID 16862)
-- Name: wagtailcore_pagelogentry wagtailcore_pagelogentry_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagelogentry
    ADD CONSTRAINT wagtailcore_pagelogentry_pkey PRIMARY KEY (id);


--
-- TOC entry 3825 (class 2606 OID 16864)
-- Name: wagtailcore_revision wagtailcore_pagerevision_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_revision
    ADD CONSTRAINT wagtailcore_pagerevision_pkey PRIMARY KEY (id);


--
-- TOC entry 3831 (class 2606 OID 16866)
-- Name: wagtailcore_pagesubscription wagtailcore_pagesubscription_page_id_user_id_0cef73ed_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagesubscription
    ADD CONSTRAINT wagtailcore_pagesubscription_page_id_user_id_0cef73ed_uniq UNIQUE (page_id, user_id);


--
-- TOC entry 3833 (class 2606 OID 16868)
-- Name: wagtailcore_pagesubscription wagtailcore_pagesubscription_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagesubscription
    ADD CONSTRAINT wagtailcore_pagesubscription_pkey PRIMARY KEY (id);


--
-- TOC entry 3839 (class 2606 OID 16870)
-- Name: wagtailcore_pageviewrestriction_groups wagtailcore_pageviewrest_pageviewrestriction_id_g_d23f80bb_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction_groups
    ADD CONSTRAINT wagtailcore_pageviewrest_pageviewrestriction_id_g_d23f80bb_uniq UNIQUE (pageviewrestriction_id, group_id);


--
-- TOC entry 3843 (class 2606 OID 16872)
-- Name: wagtailcore_pageviewrestriction_groups wagtailcore_pageviewrestriction_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction_groups
    ADD CONSTRAINT wagtailcore_pageviewrestriction_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 3837 (class 2606 OID 16874)
-- Name: wagtailcore_pageviewrestriction wagtailcore_pageviewrestriction_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction
    ADD CONSTRAINT wagtailcore_pageviewrestriction_pkey PRIMARY KEY (id);


--
-- TOC entry 3845 (class 2606 OID 16876)
-- Name: wagtailcore_referenceindex wagtailcore_referenceind_base_content_type_id_obj_9e6ccd6a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_referenceindex
    ADD CONSTRAINT wagtailcore_referenceind_base_content_type_id_obj_9e6ccd6a_uniq UNIQUE (base_content_type_id, object_id, to_content_type_id, to_object_id, content_path_hash);


--
-- TOC entry 3849 (class 2606 OID 16878)
-- Name: wagtailcore_referenceindex wagtailcore_referenceindex_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_referenceindex
    ADD CONSTRAINT wagtailcore_referenceindex_pkey PRIMARY KEY (id);


--
-- TOC entry 3854 (class 2606 OID 16880)
-- Name: wagtailcore_site wagtailcore_site_hostname_port_2c626d70_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_site
    ADD CONSTRAINT wagtailcore_site_hostname_port_2c626d70_uniq UNIQUE (hostname, port);


--
-- TOC entry 3856 (class 2606 OID 16882)
-- Name: wagtailcore_site wagtailcore_site_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_site
    ADD CONSTRAINT wagtailcore_site_pkey PRIMARY KEY (id);


--
-- TOC entry 3860 (class 2606 OID 16884)
-- Name: wagtailcore_task wagtailcore_task_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_task
    ADD CONSTRAINT wagtailcore_task_pkey PRIMARY KEY (id);


--
-- TOC entry 3865 (class 2606 OID 16886)
-- Name: wagtailcore_taskstate wagtailcore_taskstate_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_taskstate
    ADD CONSTRAINT wagtailcore_taskstate_pkey PRIMARY KEY (id);


--
-- TOC entry 3870 (class 2606 OID 16888)
-- Name: wagtailcore_uploadedfile wagtailcore_uploadedfile_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_uploadedfile
    ADD CONSTRAINT wagtailcore_uploadedfile_pkey PRIMARY KEY (id);


--
-- TOC entry 3873 (class 2606 OID 16890)
-- Name: wagtailcore_workflow wagtailcore_workflow_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflow
    ADD CONSTRAINT wagtailcore_workflow_pkey PRIMARY KEY (id);


--
-- TOC entry 3875 (class 2606 OID 16892)
-- Name: wagtailcore_workflowcontenttype wagtailcore_workflowcontenttype_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowcontenttype
    ADD CONSTRAINT wagtailcore_workflowcontenttype_pkey PRIMARY KEY (content_type_id);


--
-- TOC entry 3878 (class 2606 OID 16894)
-- Name: wagtailcore_workflowpage wagtailcore_workflowpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowpage
    ADD CONSTRAINT wagtailcore_workflowpage_pkey PRIMARY KEY (page_id);


--
-- TOC entry 3884 (class 2606 OID 16896)
-- Name: wagtailcore_workflowstate wagtailcore_workflowstate_current_task_state_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowstate
    ADD CONSTRAINT wagtailcore_workflowstate_current_task_state_id_key UNIQUE (current_task_state_id);


--
-- TOC entry 3886 (class 2606 OID 16898)
-- Name: wagtailcore_workflowstate wagtailcore_workflowstate_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowstate
    ADD CONSTRAINT wagtailcore_workflowstate_pkey PRIMARY KEY (id);


--
-- TOC entry 3892 (class 2606 OID 16900)
-- Name: wagtailcore_workflowtask wagtailcore_workflowtask_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowtask
    ADD CONSTRAINT wagtailcore_workflowtask_pkey PRIMARY KEY (id);


--
-- TOC entry 3896 (class 2606 OID 16902)
-- Name: wagtailcore_workflowtask wagtailcore_workflowtask_workflow_id_task_id_4ec7a62b_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowtask
    ADD CONSTRAINT wagtailcore_workflowtask_workflow_id_task_id_4ec7a62b_uniq UNIQUE (workflow_id, task_id);


--
-- TOC entry 3899 (class 2606 OID 16904)
-- Name: wagtaildocs_document wagtaildocs_document_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtaildocs_document
    ADD CONSTRAINT wagtaildocs_document_pkey PRIMARY KEY (id);


--
-- TOC entry 3904 (class 2606 OID 16906)
-- Name: wagtailembeds_embed wagtailembeds_embed_hash_c9bd8c9a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailembeds_embed
    ADD CONSTRAINT wagtailembeds_embed_hash_c9bd8c9a_uniq UNIQUE (hash);


--
-- TOC entry 3906 (class 2606 OID 16908)
-- Name: wagtailembeds_embed wagtailembeds_embed_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailembeds_embed
    ADD CONSTRAINT wagtailembeds_embed_pkey PRIMARY KEY (id);


--
-- TOC entry 3909 (class 2606 OID 16910)
-- Name: wagtailforms_formsubmission wagtailforms_formsubmission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailforms_formsubmission
    ADD CONSTRAINT wagtailforms_formsubmission_pkey PRIMARY KEY (id);


--
-- TOC entry 3915 (class 2606 OID 16912)
-- Name: wagtailimages_image wagtailimages_image_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_image
    ADD CONSTRAINT wagtailimages_image_pkey PRIMARY KEY (id);


--
-- TOC entry 3921 (class 2606 OID 16914)
-- Name: wagtailimages_rendition wagtailimages_rendition_image_id_filter_spec_foc_323c8fe0_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_rendition
    ADD CONSTRAINT wagtailimages_rendition_image_id_filter_spec_foc_323c8fe0_uniq UNIQUE (image_id, filter_spec, focal_point_key);


--
-- TOC entry 3923 (class 2606 OID 16916)
-- Name: wagtailimages_rendition wagtailimages_rendition_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_rendition
    ADD CONSTRAINT wagtailimages_rendition_pkey PRIMARY KEY (id);


--
-- TOC entry 3927 (class 2606 OID 16918)
-- Name: wagtailredirects_redirect wagtailredirects_redirect_old_path_site_id_783622d7_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailredirects_redirect
    ADD CONSTRAINT wagtailredirects_redirect_old_path_site_id_783622d7_uniq UNIQUE (old_path, site_id);


--
-- TOC entry 3929 (class 2606 OID 16920)
-- Name: wagtailredirects_redirect wagtailredirects_redirect_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailredirects_redirect
    ADD CONSTRAINT wagtailredirects_redirect_pkey PRIMARY KEY (id);


--
-- TOC entry 3937 (class 2606 OID 16922)
-- Name: wagtailsearch_indexentry wagtailsearch_indexentry_content_type_id_object_i_bcd7ba73_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_indexentry
    ADD CONSTRAINT wagtailsearch_indexentry_content_type_id_object_i_bcd7ba73_uniq UNIQUE (content_type_id, object_id);


--
-- TOC entry 3939 (class 2606 OID 16924)
-- Name: wagtailsearch_indexentry wagtailsearch_indexentry_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_indexentry
    ADD CONSTRAINT wagtailsearch_indexentry_pkey PRIMARY KEY (id);


--
-- TOC entry 3946 (class 2606 OID 16926)
-- Name: wagtailsearchpromotions_querydailyhits wagtailsearchpromotions__query_id_date_b9f15515_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_querydailyhits
    ADD CONSTRAINT wagtailsearchpromotions__query_id_date_b9f15515_uniq UNIQUE (query_id, date);


--
-- TOC entry 3941 (class 2606 OID 16928)
-- Name: wagtailsearchpromotions_query wagtailsearchpromotions_query_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_query
    ADD CONSTRAINT wagtailsearchpromotions_query_pkey PRIMARY KEY (id);


--
-- TOC entry 3944 (class 2606 OID 16930)
-- Name: wagtailsearchpromotions_query wagtailsearchpromotions_query_query_string_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_query
    ADD CONSTRAINT wagtailsearchpromotions_query_query_string_key UNIQUE (query_string);


--
-- TOC entry 3948 (class 2606 OID 16932)
-- Name: wagtailsearchpromotions_querydailyhits wagtailsearchpromotions_querydailyhits_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_querydailyhits
    ADD CONSTRAINT wagtailsearchpromotions_querydailyhits_pkey PRIMARY KEY (id);


--
-- TOC entry 3952 (class 2606 OID 16934)
-- Name: wagtailsearchpromotions_searchpromotion wagtailsearchpromotions_searchpromotion_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_searchpromotion
    ADD CONSTRAINT wagtailsearchpromotions_searchpromotion_pkey PRIMARY KEY (id);


--
-- TOC entry 3955 (class 2606 OID 16936)
-- Name: wagtailusers_userprofile wagtailusers_userprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailusers_userprofile
    ADD CONSTRAINT wagtailusers_userprofile_pkey PRIMARY KEY (id);


--
-- TOC entry 3957 (class 2606 OID 16938)
-- Name: wagtailusers_userprofile wagtailusers_userprofile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailusers_userprofile
    ADD CONSTRAINT wagtailusers_userprofile_user_id_key UNIQUE (user_id);


--
-- TOC entry 3602 (class 1259 OID 16939)
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 3607 (class 1259 OID 16940)
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- TOC entry 3610 (class 1259 OID 16941)
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- TOC entry 3613 (class 1259 OID 16942)
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- TOC entry 3623 (class 1259 OID 16943)
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- TOC entry 3626 (class 1259 OID 16944)
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- TOC entry 3629 (class 1259 OID 16945)
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- TOC entry 3632 (class 1259 OID 16946)
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- TOC entry 3620 (class 1259 OID 16947)
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- TOC entry 3820 (class 1259 OID 16948)
-- Name: base_content_object_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX base_content_object_idx ON public.wagtailcore_revision USING btree (base_content_type_id, object_id);


--
-- TOC entry 3637 (class 1259 OID 16949)
-- Name: contacts_contactsubmission_site_id_66673466; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX contacts_contactsubmission_site_id_66673466 ON public.contacts_contactsubmission USING btree (site_id);


--
-- TOC entry 3821 (class 1259 OID 16950)
-- Name: content_object_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX content_object_idx ON public.wagtailcore_revision USING btree (content_type_id, object_id);


--
-- TOC entry 3638 (class 1259 OID 16951)
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- TOC entry 3641 (class 1259 OID 16952)
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- TOC entry 3648 (class 1259 OID 16953)
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- TOC entry 3651 (class 1259 OID 16954)
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 3652 (class 1259 OID 16955)
-- Name: django_site_domain_a2e37b91_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_site_domain_a2e37b91_like ON public.django_site USING btree (domain varchar_pattern_ops);


--
-- TOC entry 3663 (class 1259 OID 16956)
-- Name: pages_logo_image_id_375482c6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX pages_logo_image_id_375482c6 ON public.pages_logo USING btree (image_id);


--
-- TOC entry 3670 (class 1259 OID 16957)
-- Name: pages_sitesettings_logo_id_ef4fb98b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX pages_sitesettings_logo_id_ef4fb98b ON public.pages_sitesettings USING btree (logo_id);


--
-- TOC entry 3671 (class 1259 OID 16958)
-- Name: pages_sitesettings_navigation_cta_page_id_99fb3790; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX pages_sitesettings_navigation_cta_page_id_99fb3790 ON public.pages_sitesettings USING btree (navigation_cta_page_id);


--
-- TOC entry 3680 (class 1259 OID 16959)
-- Name: projects_project_slug_2d50067a_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_project_slug_2d50067a_like ON public.projects_project USING btree (slug varchar_pattern_ops);


--
-- TOC entry 3683 (class 1259 OID 16960)
-- Name: projects_projectimage_image_id_f5a991e8; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projectimage_image_id_f5a991e8 ON public.projects_projectimage USING btree (image_id);


--
-- TOC entry 3686 (class 1259 OID 16961)
-- Name: projects_projectimage_project_id_618ded0e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projectimage_project_id_618ded0e ON public.projects_projectimage USING btree (project_id);


--
-- TOC entry 3689 (class 1259 OID 16962)
-- Name: projects_projectpageimage_image_id_1e7b6756; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projectpageimage_image_id_1e7b6756 ON public.projects_projectpageimage USING btree (image_id);


--
-- TOC entry 3692 (class 1259 OID 16963)
-- Name: projects_projectpageimage_project_page_id_1f3f194b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projectpageimage_project_page_id_1f3f194b ON public.projects_projectpageimage USING btree (project_page_id);


--
-- TOC entry 3693 (class 1259 OID 16964)
-- Name: projects_projectpagetag_content_object_id_b258f16e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projectpagetag_content_object_id_b258f16e ON public.projects_projectpagetag USING btree (content_object_id);


--
-- TOC entry 3696 (class 1259 OID 16965)
-- Name: projects_projectpagetag_tag_id_d11386be; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projectpagetag_tag_id_d11386be ON public.projects_projectpagetag USING btree (tag_id);


--
-- TOC entry 3697 (class 1259 OID 16966)
-- Name: projects_projecttag_content_object_id_ac067992; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projecttag_content_object_id_ac067992 ON public.projects_projecttag USING btree (content_object_id);


--
-- TOC entry 3700 (class 1259 OID 16967)
-- Name: projects_projecttag_tag_id_d49ab282; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX projects_projecttag_tag_id_d49ab282 ON public.projects_projecttag USING btree (tag_id);


--
-- TOC entry 3701 (class 1259 OID 16968)
-- Name: taggit_tag_name_58eb2ed9_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_tag_name_58eb2ed9_like ON public.taggit_tag USING btree (name varchar_pattern_ops);


--
-- TOC entry 3706 (class 1259 OID 16969)
-- Name: taggit_tag_slug_6be58b2c_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_tag_slug_6be58b2c_like ON public.taggit_tag USING btree (slug varchar_pattern_ops);


--
-- TOC entry 3709 (class 1259 OID 16970)
-- Name: taggit_tagg_content_8fc721_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_tagg_content_8fc721_idx ON public.taggit_taggeditem USING btree (content_type_id, object_id);


--
-- TOC entry 3710 (class 1259 OID 16971)
-- Name: taggit_taggeditem_content_type_id_9957a03c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_taggeditem_content_type_id_9957a03c ON public.taggit_taggeditem USING btree (content_type_id);


--
-- TOC entry 3713 (class 1259 OID 16972)
-- Name: taggit_taggeditem_object_id_e2d7d1df; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_taggeditem_object_id_e2d7d1df ON public.taggit_taggeditem USING btree (object_id);


--
-- TOC entry 3716 (class 1259 OID 16973)
-- Name: taggit_taggeditem_tag_id_f4f5b767; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_taggeditem_tag_id_f4f5b767 ON public.taggit_taggeditem USING btree (tag_id);


--
-- TOC entry 3880 (class 1259 OID 16974)
-- Name: unique_in_progress_workflow; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX unique_in_progress_workflow ON public.wagtailcore_workflowstate USING btree (base_content_type_id, object_id) WHERE ((status)::text = ANY (ARRAY[('in_progress'::character varying)::text, ('needs_changes'::character varying)::text]));


--
-- TOC entry 3719 (class 1259 OID 16975)
-- Name: wagtailadmi_content_717955_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailadmi_content_717955_idx ON public.wagtailadmin_editingsession USING btree (content_type_id, object_id);


--
-- TOC entry 3720 (class 1259 OID 16976)
-- Name: wagtailadmin_editingsession_content_type_id_4df7730e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailadmin_editingsession_content_type_id_4df7730e ON public.wagtailadmin_editingsession USING btree (content_type_id);


--
-- TOC entry 3723 (class 1259 OID 16977)
-- Name: wagtailadmin_editingsession_user_id_6e1a9b70; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailadmin_editingsession_user_id_6e1a9b70 ON public.wagtailadmin_editingsession USING btree (user_id);


--
-- TOC entry 3724 (class 1259 OID 16978)
-- Name: wagtailcore_collection_path_d848dc19_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_collection_path_d848dc19_like ON public.wagtailcore_collection USING btree (path varchar_pattern_ops);


--
-- TOC entry 3734 (class 1259 OID 16979)
-- Name: wagtailcore_collectionview_collectionviewrestriction__47320efd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_collectionview_collectionviewrestriction__47320efd ON public.wagtailcore_collectionviewrestriction_groups USING btree (collectionviewrestriction_id);


--
-- TOC entry 3729 (class 1259 OID 16980)
-- Name: wagtailcore_collectionviewrestriction_collection_id_761908ec; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_collectionviewrestriction_collection_id_761908ec ON public.wagtailcore_collectionviewrestriction USING btree (collection_id);


--
-- TOC entry 3735 (class 1259 OID 16981)
-- Name: wagtailcore_collectionviewrestriction_groups_group_id_1823f2a3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_collectionviewrestriction_groups_group_id_1823f2a3 ON public.wagtailcore_collectionviewrestriction_groups USING btree (group_id);


--
-- TOC entry 3738 (class 1259 OID 16982)
-- Name: wagtailcore_comment_page_id_108444b5; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_comment_page_id_108444b5 ON public.wagtailcore_comment USING btree (page_id);


--
-- TOC entry 3741 (class 1259 OID 16983)
-- Name: wagtailcore_comment_resolved_by_id_a282aa0e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_comment_resolved_by_id_a282aa0e ON public.wagtailcore_comment USING btree (resolved_by_id);


--
-- TOC entry 3742 (class 1259 OID 16984)
-- Name: wagtailcore_comment_revision_created_id_1d058279; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_comment_revision_created_id_1d058279 ON public.wagtailcore_comment USING btree (revision_created_id);


--
-- TOC entry 3743 (class 1259 OID 16985)
-- Name: wagtailcore_comment_user_id_0c577ca6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_comment_user_id_0c577ca6 ON public.wagtailcore_comment USING btree (user_id);


--
-- TOC entry 3744 (class 1259 OID 16986)
-- Name: wagtailcore_commentreply_comment_id_afc7e027; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_commentreply_comment_id_afc7e027 ON public.wagtailcore_commentreply USING btree (comment_id);


--
-- TOC entry 3747 (class 1259 OID 16987)
-- Name: wagtailcore_commentreply_user_id_d0b3b9c3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_commentreply_user_id_d0b3b9c3 ON public.wagtailcore_commentreply USING btree (user_id);


--
-- TOC entry 3752 (class 1259 OID 16988)
-- Name: wagtailcore_groupapprovalt_groupapprovaltask_id_9a9255ea; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupapprovalt_groupapprovaltask_id_9a9255ea ON public.wagtailcore_groupapprovaltask_groups USING btree (groupapprovaltask_id);


--
-- TOC entry 3753 (class 1259 OID 16989)
-- Name: wagtailcore_groupapprovaltask_groups_group_id_2e64b61f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupapprovaltask_groups_group_id_2e64b61f ON public.wagtailcore_groupapprovaltask_groups USING btree (group_id);


--
-- TOC entry 3758 (class 1259 OID 16990)
-- Name: wagtailcore_groupcollectionpermission_collection_id_5423575a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupcollectionpermission_collection_id_5423575a ON public.wagtailcore_groupcollectionpermission USING btree (collection_id);


--
-- TOC entry 3759 (class 1259 OID 16991)
-- Name: wagtailcore_groupcollectionpermission_group_id_05d61460; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupcollectionpermission_group_id_05d61460 ON public.wagtailcore_groupcollectionpermission USING btree (group_id);


--
-- TOC entry 3760 (class 1259 OID 16992)
-- Name: wagtailcore_groupcollectionpermission_permission_id_1b626275; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupcollectionpermission_permission_id_1b626275 ON public.wagtailcore_groupcollectionpermission USING btree (permission_id);


--
-- TOC entry 3765 (class 1259 OID 16993)
-- Name: wagtailcore_grouppagepermission_group_id_fc07e671; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_grouppagepermission_group_id_fc07e671 ON public.wagtailcore_grouppagepermission USING btree (group_id);


--
-- TOC entry 3766 (class 1259 OID 16994)
-- Name: wagtailcore_grouppagepermission_page_id_710b114a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_grouppagepermission_page_id_710b114a ON public.wagtailcore_grouppagepermission USING btree (page_id);


--
-- TOC entry 3767 (class 1259 OID 16995)
-- Name: wagtailcore_grouppagepermission_permission_id_05acb22e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_grouppagepermission_permission_id_05acb22e ON public.wagtailcore_grouppagepermission USING btree (permission_id);


--
-- TOC entry 3772 (class 1259 OID 16996)
-- Name: wagtailcore_groupsitepermission_group_id_e5cdbee4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupsitepermission_group_id_e5cdbee4 ON public.wagtailcore_groupsitepermission USING btree (group_id);


--
-- TOC entry 3773 (class 1259 OID 16997)
-- Name: wagtailcore_groupsitepermission_permission_id_459b1f38; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupsitepermission_permission_id_459b1f38 ON public.wagtailcore_groupsitepermission USING btree (permission_id);


--
-- TOC entry 3776 (class 1259 OID 16998)
-- Name: wagtailcore_groupsitepermission_site_id_245de488; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupsitepermission_site_id_245de488 ON public.wagtailcore_groupsitepermission USING btree (site_id);


--
-- TOC entry 3777 (class 1259 OID 16999)
-- Name: wagtailcore_locale_language_code_03149338_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_locale_language_code_03149338_like ON public.wagtailcore_locale USING btree (language_code varchar_pattern_ops);


--
-- TOC entry 3782 (class 1259 OID 17000)
-- Name: wagtailcore_modellogentry_action_d2d856ee; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_action_d2d856ee ON public.wagtailcore_modellogentry USING btree (action);


--
-- TOC entry 3783 (class 1259 OID 17001)
-- Name: wagtailcore_modellogentry_action_d2d856ee_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_action_d2d856ee_like ON public.wagtailcore_modellogentry USING btree (action varchar_pattern_ops);


--
-- TOC entry 3784 (class 1259 OID 17002)
-- Name: wagtailcore_modellogentry_content_changed_8bc39742; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_content_changed_8bc39742 ON public.wagtailcore_modellogentry USING btree (content_changed);


--
-- TOC entry 3785 (class 1259 OID 17003)
-- Name: wagtailcore_modellogentry_content_type_id_68849e77; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_content_type_id_68849e77 ON public.wagtailcore_modellogentry USING btree (content_type_id);


--
-- TOC entry 3786 (class 1259 OID 17004)
-- Name: wagtailcore_modellogentry_object_id_e0e7d4ef; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_object_id_e0e7d4ef ON public.wagtailcore_modellogentry USING btree (object_id);


--
-- TOC entry 3787 (class 1259 OID 17005)
-- Name: wagtailcore_modellogentry_object_id_e0e7d4ef_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_object_id_e0e7d4ef_like ON public.wagtailcore_modellogentry USING btree (object_id varchar_pattern_ops);


--
-- TOC entry 3790 (class 1259 OID 17006)
-- Name: wagtailcore_modellogentry_revision_id_df6ca33a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_revision_id_df6ca33a ON public.wagtailcore_modellogentry USING btree (revision_id);


--
-- TOC entry 3791 (class 1259 OID 17007)
-- Name: wagtailcore_modellogentry_timestamp_9694521b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_timestamp_9694521b ON public.wagtailcore_modellogentry USING btree ("timestamp");


--
-- TOC entry 3792 (class 1259 OID 17008)
-- Name: wagtailcore_modellogentry_user_id_0278d1bf; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_modellogentry_user_id_0278d1bf ON public.wagtailcore_modellogentry USING btree (user_id);


--
-- TOC entry 3793 (class 1259 OID 17009)
-- Name: wagtailcore_page_alias_of_id_12945502; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_alias_of_id_12945502 ON public.wagtailcore_page USING btree (alias_of_id);


--
-- TOC entry 3794 (class 1259 OID 17010)
-- Name: wagtailcore_page_content_type_id_c28424df; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_content_type_id_c28424df ON public.wagtailcore_page USING btree (content_type_id);


--
-- TOC entry 3795 (class 1259 OID 17011)
-- Name: wagtailcore_page_first_published_at_2b5dd637; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_first_published_at_2b5dd637 ON public.wagtailcore_page USING btree (first_published_at);


--
-- TOC entry 3796 (class 1259 OID 17012)
-- Name: wagtailcore_page_latest_revision_id_e60fef51; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_latest_revision_id_e60fef51 ON public.wagtailcore_page USING btree (latest_revision_id);


--
-- TOC entry 3797 (class 1259 OID 17013)
-- Name: wagtailcore_page_live_revision_id_930bd822; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_live_revision_id_930bd822 ON public.wagtailcore_page USING btree (live_revision_id);


--
-- TOC entry 3798 (class 1259 OID 17014)
-- Name: wagtailcore_page_locale_id_3c7e30a6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_locale_id_3c7e30a6 ON public.wagtailcore_page USING btree (locale_id);


--
-- TOC entry 3799 (class 1259 OID 17015)
-- Name: wagtailcore_page_locked_by_id_bcb86245; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_locked_by_id_bcb86245 ON public.wagtailcore_page USING btree (locked_by_id);


--
-- TOC entry 3800 (class 1259 OID 17016)
-- Name: wagtailcore_page_owner_id_fbf7c332; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_owner_id_fbf7c332 ON public.wagtailcore_page USING btree (owner_id);


--
-- TOC entry 3801 (class 1259 OID 17017)
-- Name: wagtailcore_page_path_98eba2c8_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_path_98eba2c8_like ON public.wagtailcore_page USING btree (path varchar_pattern_ops);


--
-- TOC entry 3806 (class 1259 OID 17018)
-- Name: wagtailcore_page_slug_e7c11b8f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_slug_e7c11b8f ON public.wagtailcore_page USING btree (slug);


--
-- TOC entry 3807 (class 1259 OID 17019)
-- Name: wagtailcore_page_slug_e7c11b8f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_slug_e7c11b8f_like ON public.wagtailcore_page USING btree (slug varchar_pattern_ops);


--
-- TOC entry 3810 (class 1259 OID 17020)
-- Name: wagtailcore_pagelogentry_action_c2408198; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_action_c2408198 ON public.wagtailcore_pagelogentry USING btree (action);


--
-- TOC entry 3811 (class 1259 OID 17021)
-- Name: wagtailcore_pagelogentry_action_c2408198_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_action_c2408198_like ON public.wagtailcore_pagelogentry USING btree (action varchar_pattern_ops);


--
-- TOC entry 3812 (class 1259 OID 17022)
-- Name: wagtailcore_pagelogentry_content_changed_99f27ade; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_content_changed_99f27ade ON public.wagtailcore_pagelogentry USING btree (content_changed);


--
-- TOC entry 3813 (class 1259 OID 17023)
-- Name: wagtailcore_pagelogentry_content_type_id_74e7708a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_content_type_id_74e7708a ON public.wagtailcore_pagelogentry USING btree (content_type_id);


--
-- TOC entry 3814 (class 1259 OID 17024)
-- Name: wagtailcore_pagelogentry_page_id_8464e327; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_page_id_8464e327 ON public.wagtailcore_pagelogentry USING btree (page_id);


--
-- TOC entry 3817 (class 1259 OID 17025)
-- Name: wagtailcore_pagelogentry_revision_id_8043d103; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_revision_id_8043d103 ON public.wagtailcore_pagelogentry USING btree (revision_id);


--
-- TOC entry 3818 (class 1259 OID 17026)
-- Name: wagtailcore_pagelogentry_timestamp_deb774c4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_timestamp_deb774c4 ON public.wagtailcore_pagelogentry USING btree ("timestamp");


--
-- TOC entry 3819 (class 1259 OID 17027)
-- Name: wagtailcore_pagelogentry_user_id_604ccfd8; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagelogentry_user_id_604ccfd8 ON public.wagtailcore_pagelogentry USING btree (user_id);


--
-- TOC entry 3822 (class 1259 OID 17028)
-- Name: wagtailcore_pagerevision_approved_go_live_at_e56afc67; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagerevision_approved_go_live_at_e56afc67 ON public.wagtailcore_revision USING btree (approved_go_live_at);


--
-- TOC entry 3823 (class 1259 OID 17029)
-- Name: wagtailcore_pagerevision_created_at_66954e3b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagerevision_created_at_66954e3b ON public.wagtailcore_revision USING btree (created_at);


--
-- TOC entry 3826 (class 1259 OID 17030)
-- Name: wagtailcore_pagerevision_user_id_2409d2f4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagerevision_user_id_2409d2f4 ON public.wagtailcore_revision USING btree (user_id);


--
-- TOC entry 3829 (class 1259 OID 17031)
-- Name: wagtailcore_pagesubscription_page_id_a085e7a6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagesubscription_page_id_a085e7a6 ON public.wagtailcore_pagesubscription USING btree (page_id);


--
-- TOC entry 3834 (class 1259 OID 17032)
-- Name: wagtailcore_pagesubscription_user_id_89d7def9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagesubscription_user_id_89d7def9 ON public.wagtailcore_pagesubscription USING btree (user_id);


--
-- TOC entry 3840 (class 1259 OID 17033)
-- Name: wagtailcore_pageviewrestri_pageviewrestriction_id_f147a99a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pageviewrestri_pageviewrestriction_id_f147a99a ON public.wagtailcore_pageviewrestriction_groups USING btree (pageviewrestriction_id);


--
-- TOC entry 3841 (class 1259 OID 17034)
-- Name: wagtailcore_pageviewrestriction_groups_group_id_6460f223; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pageviewrestriction_groups_group_id_6460f223 ON public.wagtailcore_pageviewrestriction_groups USING btree (group_id);


--
-- TOC entry 3835 (class 1259 OID 17035)
-- Name: wagtailcore_pageviewrestriction_page_id_15a8bea6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pageviewrestriction_page_id_15a8bea6 ON public.wagtailcore_pageviewrestriction USING btree (page_id);


--
-- TOC entry 3846 (class 1259 OID 17036)
-- Name: wagtailcore_referenceindex_base_content_type_id_313cf40f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_referenceindex_base_content_type_id_313cf40f ON public.wagtailcore_referenceindex USING btree (base_content_type_id);


--
-- TOC entry 3847 (class 1259 OID 17037)
-- Name: wagtailcore_referenceindex_content_type_id_766e0336; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_referenceindex_content_type_id_766e0336 ON public.wagtailcore_referenceindex USING btree (content_type_id);


--
-- TOC entry 3850 (class 1259 OID 17038)
-- Name: wagtailcore_referenceindex_to_content_type_id_93690bbd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_referenceindex_to_content_type_id_93690bbd ON public.wagtailcore_referenceindex USING btree (to_content_type_id);


--
-- TOC entry 3827 (class 1259 OID 17039)
-- Name: wagtailcore_revision_base_content_type_id_5b4ef7bd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_revision_base_content_type_id_5b4ef7bd ON public.wagtailcore_revision USING btree (base_content_type_id);


--
-- TOC entry 3828 (class 1259 OID 17040)
-- Name: wagtailcore_revision_content_type_id_c8cb69c0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_revision_content_type_id_c8cb69c0 ON public.wagtailcore_revision USING btree (content_type_id);


--
-- TOC entry 3851 (class 1259 OID 17041)
-- Name: wagtailcore_site_hostname_96b20b46; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_site_hostname_96b20b46 ON public.wagtailcore_site USING btree (hostname);


--
-- TOC entry 3852 (class 1259 OID 17042)
-- Name: wagtailcore_site_hostname_96b20b46_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_site_hostname_96b20b46_like ON public.wagtailcore_site USING btree (hostname varchar_pattern_ops);


--
-- TOC entry 3857 (class 1259 OID 17043)
-- Name: wagtailcore_site_root_page_id_e02fb95c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_site_root_page_id_e02fb95c ON public.wagtailcore_site USING btree (root_page_id);


--
-- TOC entry 3858 (class 1259 OID 17044)
-- Name: wagtailcore_task_content_type_id_249ab8ba; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_task_content_type_id_249ab8ba ON public.wagtailcore_task USING btree (content_type_id);


--
-- TOC entry 3861 (class 1259 OID 17045)
-- Name: wagtailcore_taskstate_content_type_id_0a758fdc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_taskstate_content_type_id_0a758fdc ON public.wagtailcore_taskstate USING btree (content_type_id);


--
-- TOC entry 3862 (class 1259 OID 17046)
-- Name: wagtailcore_taskstate_finished_by_id_13f98229; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_taskstate_finished_by_id_13f98229 ON public.wagtailcore_taskstate USING btree (finished_by_id);


--
-- TOC entry 3863 (class 1259 OID 17047)
-- Name: wagtailcore_taskstate_page_revision_id_9f52c88e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_taskstate_page_revision_id_9f52c88e ON public.wagtailcore_taskstate USING btree (revision_id);


--
-- TOC entry 3866 (class 1259 OID 17048)
-- Name: wagtailcore_taskstate_task_id_c3677c34; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_taskstate_task_id_c3677c34 ON public.wagtailcore_taskstate USING btree (task_id);


--
-- TOC entry 3867 (class 1259 OID 17049)
-- Name: wagtailcore_taskstate_workflow_state_id_9239a775; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_taskstate_workflow_state_id_9239a775 ON public.wagtailcore_taskstate USING btree (workflow_state_id);


--
-- TOC entry 3868 (class 1259 OID 17050)
-- Name: wagtailcore_uploadedfile_for_content_type_id_b0fc87b2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_uploadedfile_for_content_type_id_b0fc87b2 ON public.wagtailcore_uploadedfile USING btree (for_content_type_id);


--
-- TOC entry 3871 (class 1259 OID 17051)
-- Name: wagtailcore_uploadedfile_uploaded_by_user_id_c7580fe8; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_uploadedfile_uploaded_by_user_id_c7580fe8 ON public.wagtailcore_uploadedfile USING btree (uploaded_by_user_id);


--
-- TOC entry 3876 (class 1259 OID 17052)
-- Name: wagtailcore_workflowcontenttype_workflow_id_9aad7cd2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowcontenttype_workflow_id_9aad7cd2 ON public.wagtailcore_workflowcontenttype USING btree (workflow_id);


--
-- TOC entry 3879 (class 1259 OID 17053)
-- Name: wagtailcore_workflowpage_workflow_id_56f56ff6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowpage_workflow_id_56f56ff6 ON public.wagtailcore_workflowpage USING btree (workflow_id);


--
-- TOC entry 3881 (class 1259 OID 17054)
-- Name: wagtailcore_workflowstate_base_content_type_id_a30dc576; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowstate_base_content_type_id_a30dc576 ON public.wagtailcore_workflowstate USING btree (base_content_type_id);


--
-- TOC entry 3882 (class 1259 OID 17055)
-- Name: wagtailcore_workflowstate_content_type_id_2bb78ce1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowstate_content_type_id_2bb78ce1 ON public.wagtailcore_workflowstate USING btree (content_type_id);


--
-- TOC entry 3887 (class 1259 OID 17056)
-- Name: wagtailcore_workflowstate_requested_by_id_4090bca3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowstate_requested_by_id_4090bca3 ON public.wagtailcore_workflowstate USING btree (requested_by_id);


--
-- TOC entry 3888 (class 1259 OID 17057)
-- Name: wagtailcore_workflowstate_workflow_id_1f18378f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowstate_workflow_id_1f18378f ON public.wagtailcore_workflowstate USING btree (workflow_id);


--
-- TOC entry 3893 (class 1259 OID 17058)
-- Name: wagtailcore_workflowtask_task_id_ce7716fe; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowtask_task_id_ce7716fe ON public.wagtailcore_workflowtask USING btree (task_id);


--
-- TOC entry 3894 (class 1259 OID 17059)
-- Name: wagtailcore_workflowtask_workflow_id_b9717175; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_workflowtask_workflow_id_b9717175 ON public.wagtailcore_workflowtask USING btree (workflow_id);


--
-- TOC entry 3897 (class 1259 OID 17060)
-- Name: wagtaildocs_document_collection_id_23881625; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtaildocs_document_collection_id_23881625 ON public.wagtaildocs_document USING btree (collection_id);


--
-- TOC entry 3900 (class 1259 OID 17061)
-- Name: wagtaildocs_document_uploaded_by_user_id_17258b41; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtaildocs_document_uploaded_by_user_id_17258b41 ON public.wagtaildocs_document USING btree (uploaded_by_user_id);


--
-- TOC entry 3901 (class 1259 OID 17062)
-- Name: wagtailembeds_embed_cache_until_26c94bb0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailembeds_embed_cache_until_26c94bb0 ON public.wagtailembeds_embed USING btree (cache_until);


--
-- TOC entry 3902 (class 1259 OID 17063)
-- Name: wagtailembeds_embed_hash_c9bd8c9a_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailembeds_embed_hash_c9bd8c9a_like ON public.wagtailembeds_embed USING btree (hash varchar_pattern_ops);


--
-- TOC entry 3907 (class 1259 OID 17064)
-- Name: wagtailforms_formsubmission_page_id_e48e93e7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailforms_formsubmission_page_id_e48e93e7 ON public.wagtailforms_formsubmission USING btree (page_id);


--
-- TOC entry 3910 (class 1259 OID 17065)
-- Name: wagtailimages_image_collection_id_c2f8af7e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_image_collection_id_c2f8af7e ON public.wagtailimages_image USING btree (collection_id);


--
-- TOC entry 3911 (class 1259 OID 17066)
-- Name: wagtailimages_image_created_at_86fa6cd4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_image_created_at_86fa6cd4 ON public.wagtailimages_image USING btree (created_at);


--
-- TOC entry 3912 (class 1259 OID 17067)
-- Name: wagtailimages_image_file_hash_fb5bbb23; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_image_file_hash_fb5bbb23 ON public.wagtailimages_image USING btree (file_hash);


--
-- TOC entry 3913 (class 1259 OID 17068)
-- Name: wagtailimages_image_file_hash_fb5bbb23_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_image_file_hash_fb5bbb23_like ON public.wagtailimages_image USING btree (file_hash varchar_pattern_ops);


--
-- TOC entry 3916 (class 1259 OID 17069)
-- Name: wagtailimages_image_uploaded_by_user_id_5d73dc75; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_image_uploaded_by_user_id_5d73dc75 ON public.wagtailimages_image USING btree (uploaded_by_user_id);


--
-- TOC entry 3917 (class 1259 OID 17070)
-- Name: wagtailimages_rendition_filter_spec_1cba3201; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_rendition_filter_spec_1cba3201 ON public.wagtailimages_rendition USING btree (filter_spec);


--
-- TOC entry 3918 (class 1259 OID 17071)
-- Name: wagtailimages_rendition_filter_spec_1cba3201_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_rendition_filter_spec_1cba3201_like ON public.wagtailimages_rendition USING btree (filter_spec varchar_pattern_ops);


--
-- TOC entry 3919 (class 1259 OID 17072)
-- Name: wagtailimages_rendition_image_id_3e1fd774; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_rendition_image_id_3e1fd774 ON public.wagtailimages_rendition USING btree (image_id);


--
-- TOC entry 3924 (class 1259 OID 17073)
-- Name: wagtailredirects_redirect_old_path_bb35247b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailredirects_redirect_old_path_bb35247b ON public.wagtailredirects_redirect USING btree (old_path);


--
-- TOC entry 3925 (class 1259 OID 17074)
-- Name: wagtailredirects_redirect_old_path_bb35247b_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailredirects_redirect_old_path_bb35247b_like ON public.wagtailredirects_redirect USING btree (old_path varchar_pattern_ops);


--
-- TOC entry 3930 (class 1259 OID 17075)
-- Name: wagtailredirects_redirect_redirect_page_id_b5728a8f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailredirects_redirect_redirect_page_id_b5728a8f ON public.wagtailredirects_redirect USING btree (redirect_page_id);


--
-- TOC entry 3931 (class 1259 OID 17076)
-- Name: wagtailredirects_redirect_site_id_780a0e1e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailredirects_redirect_site_id_780a0e1e ON public.wagtailredirects_redirect USING btree (site_id);


--
-- TOC entry 3932 (class 1259 OID 17077)
-- Name: wagtailsear_autocom_476c89_gin; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsear_autocom_476c89_gin ON public.wagtailsearch_indexentry USING gin (autocomplete);


--
-- TOC entry 3933 (class 1259 OID 17078)
-- Name: wagtailsear_body_90c85d_gin; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsear_body_90c85d_gin ON public.wagtailsearch_indexentry USING gin (body);


--
-- TOC entry 3934 (class 1259 OID 17079)
-- Name: wagtailsear_title_9caae0_gin; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsear_title_9caae0_gin ON public.wagtailsearch_indexentry USING gin (title);


--
-- TOC entry 3935 (class 1259 OID 17080)
-- Name: wagtailsearch_indexentry_content_type_id_62ed694f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsearch_indexentry_content_type_id_62ed694f ON public.wagtailsearch_indexentry USING btree (content_type_id);


--
-- TOC entry 3942 (class 1259 OID 17081)
-- Name: wagtailsearchpromotions_query_query_string_0e19aecc_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsearchpromotions_query_query_string_0e19aecc_like ON public.wagtailsearchpromotions_query USING btree (query_string varchar_pattern_ops);


--
-- TOC entry 3949 (class 1259 OID 17082)
-- Name: wagtailsearchpromotions_querydailyhits_query_id_3a591f4d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsearchpromotions_querydailyhits_query_id_3a591f4d ON public.wagtailsearchpromotions_querydailyhits USING btree (query_id);


--
-- TOC entry 3950 (class 1259 OID 17083)
-- Name: wagtailsearchpromotions_searchpromotion_page_id_71920f17; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsearchpromotions_searchpromotion_page_id_71920f17 ON public.wagtailsearchpromotions_searchpromotion USING btree (page_id);


--
-- TOC entry 3953 (class 1259 OID 17084)
-- Name: wagtailsearchpromotions_searchpromotion_query_id_fbce4eaa; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsearchpromotions_searchpromotion_query_id_fbce4eaa ON public.wagtailsearchpromotions_searchpromotion USING btree (query_id);


--
-- TOC entry 3889 (class 1259 OID 17085)
-- Name: workflowstate_base_ct_id_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX workflowstate_base_ct_id_idx ON public.wagtailcore_workflowstate USING btree (base_content_type_id, object_id);


--
-- TOC entry 3890 (class 1259 OID 17086)
-- Name: workflowstate_ct_id_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX workflowstate_ct_id_idx ON public.wagtailcore_workflowstate USING btree (content_type_id, object_id);


--
-- TOC entry 3958 (class 2606 OID 17087)
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3959 (class 2606 OID 17092)
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3960 (class 2606 OID 17097)
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3961 (class 2606 OID 17102)
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3962 (class 2606 OID 17107)
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3963 (class 2606 OID 17112)
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3964 (class 2606 OID 17117)
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3965 (class 2606 OID 17122)
-- Name: contacts_contactsubmission contacts_contactsubm_site_id_66673466_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contacts_contactsubmission
    ADD CONSTRAINT contacts_contactsubm_site_id_66673466_fk_wagtailco FOREIGN KEY (site_id) REFERENCES public.wagtailcore_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3966 (class 2606 OID 17127)
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3967 (class 2606 OID 17132)
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3968 (class 2606 OID 17137)
-- Name: pages_contactpage pages_contactpage_page_ptr_id_604d75e6_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_contactpage
    ADD CONSTRAINT pages_contactpage_page_ptr_id_604d75e6_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3969 (class 2606 OID 17142)
-- Name: pages_gallerypage pages_gallerypage_page_ptr_id_c6ee2214_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_gallerypage
    ADD CONSTRAINT pages_gallerypage_page_ptr_id_c6ee2214_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3970 (class 2606 OID 17147)
-- Name: pages_homepage pages_homepage_page_ptr_id_5b805d74_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_homepage
    ADD CONSTRAINT pages_homepage_page_ptr_id_5b805d74_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3971 (class 2606 OID 17152)
-- Name: pages_logo pages_logo_image_id_375482c6_fk_wagtailimages_image_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_logo
    ADD CONSTRAINT pages_logo_image_id_375482c6_fk_wagtailimages_image_id FOREIGN KEY (image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3972 (class 2606 OID 17157)
-- Name: pages_modularpage pages_modularpage_page_ptr_id_802d7c31_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_modularpage
    ADD CONSTRAINT pages_modularpage_page_ptr_id_802d7c31_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3973 (class 2606 OID 17162)
-- Name: pages_sitesettings pages_sitesettings_logo_id_ef4fb98b_fk_wagtailimages_image_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_sitesettings
    ADD CONSTRAINT pages_sitesettings_logo_id_ef4fb98b_fk_wagtailimages_image_id FOREIGN KEY (logo_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3974 (class 2606 OID 17167)
-- Name: pages_sitesettings pages_sitesettings_navigation_cta_page__99fb3790_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_sitesettings
    ADD CONSTRAINT pages_sitesettings_navigation_cta_page__99fb3790_fk_wagtailco FOREIGN KEY (navigation_cta_page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3975 (class 2606 OID 17172)
-- Name: pages_sitesettings pages_sitesettings_site_id_cbd7f7da_fk_wagtailcore_site_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_sitesettings
    ADD CONSTRAINT pages_sitesettings_site_id_cbd7f7da_fk_wagtailcore_site_id FOREIGN KEY (site_id) REFERENCES public.wagtailcore_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3976 (class 2606 OID 17177)
-- Name: projects_projectimage projects_projectimag_image_id_f5a991e8_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectimage
    ADD CONSTRAINT projects_projectimag_image_id_f5a991e8_fk_wagtailim FOREIGN KEY (image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3977 (class 2606 OID 17182)
-- Name: projects_projectimage projects_projectimag_project_id_618ded0e_fk_projects_; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectimage
    ADD CONSTRAINT projects_projectimag_project_id_618ded0e_fk_projects_ FOREIGN KEY (project_id) REFERENCES public.projects_project(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3981 (class 2606 OID 17187)
-- Name: projects_projectpagetag projects_projectpage_content_object_id_b258f16e_fk_projects_; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpagetag
    ADD CONSTRAINT projects_projectpage_content_object_id_b258f16e_fk_projects_ FOREIGN KEY (content_object_id) REFERENCES public.projects_projectpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3979 (class 2606 OID 17192)
-- Name: projects_projectpageimage projects_projectpage_image_id_1e7b6756_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpageimage
    ADD CONSTRAINT projects_projectpage_image_id_1e7b6756_fk_wagtailim FOREIGN KEY (image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3978 (class 2606 OID 17197)
-- Name: projects_projectpage projects_projectpage_page_ptr_id_2eccd927_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpage
    ADD CONSTRAINT projects_projectpage_page_ptr_id_2eccd927_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3980 (class 2606 OID 17202)
-- Name: projects_projectpageimage projects_projectpage_project_page_id_1f3f194b_fk_projects_; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpageimage
    ADD CONSTRAINT projects_projectpage_project_page_id_1f3f194b_fk_projects_ FOREIGN KEY (project_page_id) REFERENCES public.projects_projectpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3982 (class 2606 OID 17207)
-- Name: projects_projectpagetag projects_projectpagetag_tag_id_d11386be_fk_taggit_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projectpagetag
    ADD CONSTRAINT projects_projectpagetag_tag_id_d11386be_fk_taggit_tag_id FOREIGN KEY (tag_id) REFERENCES public.taggit_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3983 (class 2606 OID 17212)
-- Name: projects_projecttag projects_projecttag_content_object_id_ac067992_fk_projects_; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projecttag
    ADD CONSTRAINT projects_projecttag_content_object_id_ac067992_fk_projects_ FOREIGN KEY (content_object_id) REFERENCES public.projects_project(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3984 (class 2606 OID 17217)
-- Name: projects_projecttag projects_projecttag_tag_id_d49ab282_fk_taggit_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects_projecttag
    ADD CONSTRAINT projects_projecttag_tag_id_d49ab282_fk_taggit_tag_id FOREIGN KEY (tag_id) REFERENCES public.taggit_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3985 (class 2606 OID 17222)
-- Name: taggit_taggeditem taggit_taggeditem_content_type_id_9957a03c_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_content_type_id_9957a03c_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3986 (class 2606 OID 17227)
-- Name: taggit_taggeditem taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id FOREIGN KEY (tag_id) REFERENCES public.taggit_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3987 (class 2606 OID 17232)
-- Name: wagtailadmin_editingsession wagtailadmin_editing_content_type_id_4df7730e_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailadmin_editingsession
    ADD CONSTRAINT wagtailadmin_editing_content_type_id_4df7730e_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3988 (class 2606 OID 17237)
-- Name: wagtailadmin_editingsession wagtailadmin_editingsession_user_id_6e1a9b70_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailadmin_editingsession
    ADD CONSTRAINT wagtailadmin_editingsession_user_id_6e1a9b70_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3989 (class 2606 OID 17242)
-- Name: wagtailcore_collectionviewrestriction wagtailcore_collecti_collection_id_761908ec_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction
    ADD CONSTRAINT wagtailcore_collecti_collection_id_761908ec_fk_wagtailco FOREIGN KEY (collection_id) REFERENCES public.wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3990 (class 2606 OID 17247)
-- Name: wagtailcore_collectionviewrestriction_groups wagtailcore_collecti_collectionviewrestri_47320efd_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction_groups
    ADD CONSTRAINT wagtailcore_collecti_collectionviewrestri_47320efd_fk_wagtailco FOREIGN KEY (collectionviewrestriction_id) REFERENCES public.wagtailcore_collectionviewrestriction(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3991 (class 2606 OID 17252)
-- Name: wagtailcore_collectionviewrestriction_groups wagtailcore_collecti_group_id_1823f2a3_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction_groups
    ADD CONSTRAINT wagtailcore_collecti_group_id_1823f2a3_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3992 (class 2606 OID 17257)
-- Name: wagtailcore_comment wagtailcore_comment_page_id_108444b5_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_comment
    ADD CONSTRAINT wagtailcore_comment_page_id_108444b5_fk_wagtailcore_page_id FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3993 (class 2606 OID 17262)
-- Name: wagtailcore_comment wagtailcore_comment_resolved_by_id_a282aa0e_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_comment
    ADD CONSTRAINT wagtailcore_comment_resolved_by_id_a282aa0e_fk_auth_user_id FOREIGN KEY (resolved_by_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3994 (class 2606 OID 17267)
-- Name: wagtailcore_comment wagtailcore_comment_revision_created_id_1d058279_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_comment
    ADD CONSTRAINT wagtailcore_comment_revision_created_id_1d058279_fk_wagtailco FOREIGN KEY (revision_created_id) REFERENCES public.wagtailcore_revision(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3995 (class 2606 OID 17272)
-- Name: wagtailcore_comment wagtailcore_comment_user_id_0c577ca6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_comment
    ADD CONSTRAINT wagtailcore_comment_user_id_0c577ca6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3996 (class 2606 OID 17277)
-- Name: wagtailcore_commentreply wagtailcore_commentr_comment_id_afc7e027_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_commentreply
    ADD CONSTRAINT wagtailcore_commentr_comment_id_afc7e027_fk_wagtailco FOREIGN KEY (comment_id) REFERENCES public.wagtailcore_comment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3997 (class 2606 OID 17282)
-- Name: wagtailcore_commentreply wagtailcore_commentreply_user_id_d0b3b9c3_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_commentreply
    ADD CONSTRAINT wagtailcore_commentreply_user_id_d0b3b9c3_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3999 (class 2606 OID 17287)
-- Name: wagtailcore_groupapprovaltask_groups wagtailcore_groupapp_group_id_2e64b61f_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupapprovaltask_groups
    ADD CONSTRAINT wagtailcore_groupapp_group_id_2e64b61f_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4000 (class 2606 OID 17292)
-- Name: wagtailcore_groupapprovaltask_groups wagtailcore_groupapp_groupapprovaltask_id_9a9255ea_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupapprovaltask_groups
    ADD CONSTRAINT wagtailcore_groupapp_groupapprovaltask_id_9a9255ea_fk_wagtailco FOREIGN KEY (groupapprovaltask_id) REFERENCES public.wagtailcore_groupapprovaltask(task_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3998 (class 2606 OID 17297)
-- Name: wagtailcore_groupapprovaltask wagtailcore_groupapp_task_ptr_id_cfe58781_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupapprovaltask
    ADD CONSTRAINT wagtailcore_groupapp_task_ptr_id_cfe58781_fk_wagtailco FOREIGN KEY (task_ptr_id) REFERENCES public.wagtailcore_task(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4001 (class 2606 OID 17302)
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcol_collection_id_5423575a_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcol_collection_id_5423575a_fk_wagtailco FOREIGN KEY (collection_id) REFERENCES public.wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4002 (class 2606 OID 17307)
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcol_group_id_05d61460_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcol_group_id_05d61460_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4003 (class 2606 OID 17312)
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcol_permission_id_1b626275_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcol_permission_id_1b626275_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4004 (class 2606 OID 17317)
-- Name: wagtailcore_grouppagepermission wagtailcore_grouppag_group_id_fc07e671_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppag_group_id_fc07e671_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4005 (class 2606 OID 17322)
-- Name: wagtailcore_grouppagepermission wagtailcore_grouppag_page_id_710b114a_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppag_page_id_710b114a_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4006 (class 2606 OID 17327)
-- Name: wagtailcore_grouppagepermission wagtailcore_grouppag_permission_id_05acb22e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppag_permission_id_05acb22e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4007 (class 2606 OID 17332)
-- Name: wagtailcore_groupsitepermission wagtailcore_groupsit_group_id_e5cdbee4_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupsitepermission
    ADD CONSTRAINT wagtailcore_groupsit_group_id_e5cdbee4_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4008 (class 2606 OID 17337)
-- Name: wagtailcore_groupsitepermission wagtailcore_groupsit_permission_id_459b1f38_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupsitepermission
    ADD CONSTRAINT wagtailcore_groupsit_permission_id_459b1f38_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4009 (class 2606 OID 17342)
-- Name: wagtailcore_groupsitepermission wagtailcore_groupsit_site_id_245de488_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupsitepermission
    ADD CONSTRAINT wagtailcore_groupsit_site_id_245de488_fk_wagtailco FOREIGN KEY (site_id) REFERENCES public.wagtailcore_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4010 (class 2606 OID 17347)
-- Name: wagtailcore_modellogentry wagtailcore_modellog_content_type_id_68849e77_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_modellogentry
    ADD CONSTRAINT wagtailcore_modellog_content_type_id_68849e77_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4011 (class 2606 OID 17352)
-- Name: wagtailcore_page wagtailcore_page_alias_of_id_12945502_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_alias_of_id_12945502_fk_wagtailcore_page_id FOREIGN KEY (alias_of_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4012 (class 2606 OID 17357)
-- Name: wagtailcore_page wagtailcore_page_content_type_id_c28424df_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_content_type_id_c28424df_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4013 (class 2606 OID 17362)
-- Name: wagtailcore_page wagtailcore_page_latest_revision_id_e60fef51_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_latest_revision_id_e60fef51_fk_wagtailco FOREIGN KEY (latest_revision_id) REFERENCES public.wagtailcore_revision(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4014 (class 2606 OID 17367)
-- Name: wagtailcore_page wagtailcore_page_live_revision_id_930bd822_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_live_revision_id_930bd822_fk_wagtailco FOREIGN KEY (live_revision_id) REFERENCES public.wagtailcore_revision(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4015 (class 2606 OID 17372)
-- Name: wagtailcore_page wagtailcore_page_locale_id_3c7e30a6_fk_wagtailcore_locale_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_locale_id_3c7e30a6_fk_wagtailcore_locale_id FOREIGN KEY (locale_id) REFERENCES public.wagtailcore_locale(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4016 (class 2606 OID 17377)
-- Name: wagtailcore_page wagtailcore_page_locked_by_id_bcb86245_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_locked_by_id_bcb86245_fk_auth_user_id FOREIGN KEY (locked_by_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4017 (class 2606 OID 17382)
-- Name: wagtailcore_page wagtailcore_page_owner_id_fbf7c332_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_owner_id_fbf7c332_fk_auth_user_id FOREIGN KEY (owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4018 (class 2606 OID 17387)
-- Name: wagtailcore_pagelogentry wagtailcore_pageloge_content_type_id_74e7708a_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagelogentry
    ADD CONSTRAINT wagtailcore_pageloge_content_type_id_74e7708a_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4019 (class 2606 OID 17392)
-- Name: wagtailcore_revision wagtailcore_pagerevision_user_id_2409d2f4_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_revision
    ADD CONSTRAINT wagtailcore_pagerevision_user_id_2409d2f4_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4022 (class 2606 OID 17397)
-- Name: wagtailcore_pagesubscription wagtailcore_pagesubs_page_id_a085e7a6_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagesubscription
    ADD CONSTRAINT wagtailcore_pagesubs_page_id_a085e7a6_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4023 (class 2606 OID 17402)
-- Name: wagtailcore_pagesubscription wagtailcore_pagesubscription_user_id_89d7def9_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagesubscription
    ADD CONSTRAINT wagtailcore_pagesubscription_user_id_89d7def9_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4025 (class 2606 OID 17407)
-- Name: wagtailcore_pageviewrestriction_groups wagtailcore_pageview_group_id_6460f223_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction_groups
    ADD CONSTRAINT wagtailcore_pageview_group_id_6460f223_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4024 (class 2606 OID 17412)
-- Name: wagtailcore_pageviewrestriction wagtailcore_pageview_page_id_15a8bea6_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction
    ADD CONSTRAINT wagtailcore_pageview_page_id_15a8bea6_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4026 (class 2606 OID 17417)
-- Name: wagtailcore_pageviewrestriction_groups wagtailcore_pageview_pageviewrestriction__f147a99a_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction_groups
    ADD CONSTRAINT wagtailcore_pageview_pageviewrestriction__f147a99a_fk_wagtailco FOREIGN KEY (pageviewrestriction_id) REFERENCES public.wagtailcore_pageviewrestriction(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4027 (class 2606 OID 17422)
-- Name: wagtailcore_referenceindex wagtailcore_referenc_base_content_type_id_313cf40f_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_referenceindex
    ADD CONSTRAINT wagtailcore_referenc_base_content_type_id_313cf40f_fk_django_co FOREIGN KEY (base_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4028 (class 2606 OID 17427)
-- Name: wagtailcore_referenceindex wagtailcore_referenc_content_type_id_766e0336_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_referenceindex
    ADD CONSTRAINT wagtailcore_referenc_content_type_id_766e0336_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4029 (class 2606 OID 17432)
-- Name: wagtailcore_referenceindex wagtailcore_referenc_to_content_type_id_93690bbd_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_referenceindex
    ADD CONSTRAINT wagtailcore_referenc_to_content_type_id_93690bbd_fk_django_co FOREIGN KEY (to_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4020 (class 2606 OID 17437)
-- Name: wagtailcore_revision wagtailcore_revision_base_content_type_id_5b4ef7bd_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_revision
    ADD CONSTRAINT wagtailcore_revision_base_content_type_id_5b4ef7bd_fk_django_co FOREIGN KEY (base_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4021 (class 2606 OID 17442)
-- Name: wagtailcore_revision wagtailcore_revision_content_type_id_c8cb69c0_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_revision
    ADD CONSTRAINT wagtailcore_revision_content_type_id_c8cb69c0_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4030 (class 2606 OID 17447)
-- Name: wagtailcore_site wagtailcore_site_root_page_id_e02fb95c_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_site
    ADD CONSTRAINT wagtailcore_site_root_page_id_e02fb95c_fk_wagtailcore_page_id FOREIGN KEY (root_page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4031 (class 2606 OID 17452)
-- Name: wagtailcore_task wagtailcore_task_content_type_id_249ab8ba_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_task
    ADD CONSTRAINT wagtailcore_task_content_type_id_249ab8ba_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4032 (class 2606 OID 17457)
-- Name: wagtailcore_taskstate wagtailcore_taskstat_content_type_id_0a758fdc_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_taskstate
    ADD CONSTRAINT wagtailcore_taskstat_content_type_id_0a758fdc_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4033 (class 2606 OID 17462)
-- Name: wagtailcore_taskstate wagtailcore_taskstat_revision_id_df25a499_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_taskstate
    ADD CONSTRAINT wagtailcore_taskstat_revision_id_df25a499_fk_wagtailco FOREIGN KEY (revision_id) REFERENCES public.wagtailcore_revision(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4034 (class 2606 OID 17467)
-- Name: wagtailcore_taskstate wagtailcore_taskstat_workflow_state_id_9239a775_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_taskstate
    ADD CONSTRAINT wagtailcore_taskstat_workflow_state_id_9239a775_fk_wagtailco FOREIGN KEY (workflow_state_id) REFERENCES public.wagtailcore_workflowstate(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4035 (class 2606 OID 17472)
-- Name: wagtailcore_taskstate wagtailcore_taskstate_finished_by_id_13f98229_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_taskstate
    ADD CONSTRAINT wagtailcore_taskstate_finished_by_id_13f98229_fk_auth_user_id FOREIGN KEY (finished_by_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4036 (class 2606 OID 17477)
-- Name: wagtailcore_taskstate wagtailcore_taskstate_task_id_c3677c34_fk_wagtailcore_task_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_taskstate
    ADD CONSTRAINT wagtailcore_taskstate_task_id_c3677c34_fk_wagtailcore_task_id FOREIGN KEY (task_id) REFERENCES public.wagtailcore_task(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4037 (class 2606 OID 17482)
-- Name: wagtailcore_uploadedfile wagtailcore_uploaded_for_content_type_id_b0fc87b2_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_uploadedfile
    ADD CONSTRAINT wagtailcore_uploaded_for_content_type_id_b0fc87b2_fk_django_co FOREIGN KEY (for_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4038 (class 2606 OID 17487)
-- Name: wagtailcore_uploadedfile wagtailcore_uploaded_uploaded_by_user_id_c7580fe8_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_uploadedfile
    ADD CONSTRAINT wagtailcore_uploaded_uploaded_by_user_id_c7580fe8_fk_auth_user FOREIGN KEY (uploaded_by_user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4043 (class 2606 OID 17492)
-- Name: wagtailcore_workflowstate wagtailcore_workflow_base_content_type_id_a30dc576_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowstate
    ADD CONSTRAINT wagtailcore_workflow_base_content_type_id_a30dc576_fk_django_co FOREIGN KEY (base_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4044 (class 2606 OID 17497)
-- Name: wagtailcore_workflowstate wagtailcore_workflow_content_type_id_2bb78ce1_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowstate
    ADD CONSTRAINT wagtailcore_workflow_content_type_id_2bb78ce1_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4039 (class 2606 OID 17502)
-- Name: wagtailcore_workflowcontenttype wagtailcore_workflow_content_type_id_b261bb37_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowcontenttype
    ADD CONSTRAINT wagtailcore_workflow_content_type_id_b261bb37_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4045 (class 2606 OID 17507)
-- Name: wagtailcore_workflowstate wagtailcore_workflow_current_task_state_i_3a1a0632_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowstate
    ADD CONSTRAINT wagtailcore_workflow_current_task_state_i_3a1a0632_fk_wagtailco FOREIGN KEY (current_task_state_id) REFERENCES public.wagtailcore_taskstate(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4041 (class 2606 OID 17512)
-- Name: wagtailcore_workflowpage wagtailcore_workflow_page_id_81e7bab6_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowpage
    ADD CONSTRAINT wagtailcore_workflow_page_id_81e7bab6_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4046 (class 2606 OID 17517)
-- Name: wagtailcore_workflowstate wagtailcore_workflow_requested_by_id_4090bca3_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowstate
    ADD CONSTRAINT wagtailcore_workflow_requested_by_id_4090bca3_fk_auth_user FOREIGN KEY (requested_by_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4048 (class 2606 OID 17522)
-- Name: wagtailcore_workflowtask wagtailcore_workflow_task_id_ce7716fe_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowtask
    ADD CONSTRAINT wagtailcore_workflow_task_id_ce7716fe_fk_wagtailco FOREIGN KEY (task_id) REFERENCES public.wagtailcore_task(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4047 (class 2606 OID 17527)
-- Name: wagtailcore_workflowstate wagtailcore_workflow_workflow_id_1f18378f_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowstate
    ADD CONSTRAINT wagtailcore_workflow_workflow_id_1f18378f_fk_wagtailco FOREIGN KEY (workflow_id) REFERENCES public.wagtailcore_workflow(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4042 (class 2606 OID 17532)
-- Name: wagtailcore_workflowpage wagtailcore_workflow_workflow_id_56f56ff6_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowpage
    ADD CONSTRAINT wagtailcore_workflow_workflow_id_56f56ff6_fk_wagtailco FOREIGN KEY (workflow_id) REFERENCES public.wagtailcore_workflow(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4040 (class 2606 OID 17537)
-- Name: wagtailcore_workflowcontenttype wagtailcore_workflow_workflow_id_9aad7cd2_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowcontenttype
    ADD CONSTRAINT wagtailcore_workflow_workflow_id_9aad7cd2_fk_wagtailco FOREIGN KEY (workflow_id) REFERENCES public.wagtailcore_workflow(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4049 (class 2606 OID 17542)
-- Name: wagtailcore_workflowtask wagtailcore_workflow_workflow_id_b9717175_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_workflowtask
    ADD CONSTRAINT wagtailcore_workflow_workflow_id_b9717175_fk_wagtailco FOREIGN KEY (workflow_id) REFERENCES public.wagtailcore_workflow(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4050 (class 2606 OID 17547)
-- Name: wagtaildocs_document wagtaildocs_document_collection_id_23881625_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtaildocs_document
    ADD CONSTRAINT wagtaildocs_document_collection_id_23881625_fk_wagtailco FOREIGN KEY (collection_id) REFERENCES public.wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4051 (class 2606 OID 17552)
-- Name: wagtaildocs_document wagtaildocs_document_uploaded_by_user_id_17258b41_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtaildocs_document
    ADD CONSTRAINT wagtaildocs_document_uploaded_by_user_id_17258b41_fk_auth_user FOREIGN KEY (uploaded_by_user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4052 (class 2606 OID 17557)
-- Name: wagtailforms_formsubmission wagtailforms_formsub_page_id_e48e93e7_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailforms_formsubmission
    ADD CONSTRAINT wagtailforms_formsub_page_id_e48e93e7_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4053 (class 2606 OID 17562)
-- Name: wagtailimages_image wagtailimages_image_collection_id_c2f8af7e_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_image
    ADD CONSTRAINT wagtailimages_image_collection_id_c2f8af7e_fk_wagtailco FOREIGN KEY (collection_id) REFERENCES public.wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4054 (class 2606 OID 17567)
-- Name: wagtailimages_image wagtailimages_image_uploaded_by_user_id_5d73dc75_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_image
    ADD CONSTRAINT wagtailimages_image_uploaded_by_user_id_5d73dc75_fk_auth_user FOREIGN KEY (uploaded_by_user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4055 (class 2606 OID 17572)
-- Name: wagtailimages_rendition wagtailimages_rendit_image_id_3e1fd774_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_rendition
    ADD CONSTRAINT wagtailimages_rendit_image_id_3e1fd774_fk_wagtailim FOREIGN KEY (image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4056 (class 2606 OID 17577)
-- Name: wagtailredirects_redirect wagtailredirects_red_redirect_page_id_b5728a8f_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailredirects_redirect
    ADD CONSTRAINT wagtailredirects_red_redirect_page_id_b5728a8f_fk_wagtailco FOREIGN KEY (redirect_page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4057 (class 2606 OID 17582)
-- Name: wagtailredirects_redirect wagtailredirects_red_site_id_780a0e1e_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailredirects_redirect
    ADD CONSTRAINT wagtailredirects_red_site_id_780a0e1e_fk_wagtailco FOREIGN KEY (site_id) REFERENCES public.wagtailcore_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4058 (class 2606 OID 17587)
-- Name: wagtailsearch_indexentry wagtailsearch_indexe_content_type_id_62ed694f_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_indexentry
    ADD CONSTRAINT wagtailsearch_indexe_content_type_id_62ed694f_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4060 (class 2606 OID 17592)
-- Name: wagtailsearchpromotions_searchpromotion wagtailsearchpromoti_page_id_71920f17_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_searchpromotion
    ADD CONSTRAINT wagtailsearchpromoti_page_id_71920f17_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4059 (class 2606 OID 17597)
-- Name: wagtailsearchpromotions_querydailyhits wagtailsearchpromoti_query_id_3a591f4d_fk_wagtailse; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_querydailyhits
    ADD CONSTRAINT wagtailsearchpromoti_query_id_3a591f4d_fk_wagtailse FOREIGN KEY (query_id) REFERENCES public.wagtailsearchpromotions_query(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4061 (class 2606 OID 17602)
-- Name: wagtailsearchpromotions_searchpromotion wagtailsearchpromoti_query_id_fbce4eaa_fk_wagtailse; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearchpromotions_searchpromotion
    ADD CONSTRAINT wagtailsearchpromoti_query_id_fbce4eaa_fk_wagtailse FOREIGN KEY (query_id) REFERENCES public.wagtailsearchpromotions_query(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 4062 (class 2606 OID 17607)
-- Name: wagtailusers_userprofile wagtailusers_userprofile_user_id_59c92331_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailusers_userprofile
    ADD CONSTRAINT wagtailusers_userprofile_user_id_59c92331_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


-- Completed on 2025-09-12 14:47:58 CEST

--
-- PostgreSQL database dump complete
--

\unrestrict kiclYaoZxVD8sySYU5EhGjhf9RYbTqKftzvtvXmFBUs8feWGAwx0TH1sqOVvfol

