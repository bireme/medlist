{% load mptt_tags %}
{% load i18n %}
{% load app_filters %}

{% spaceless %}
<?xml version="1.0" encoding="UTF-8"?>
<list lang="{{request.LANGUAGE_CODE}}">
	<name>{{ list|translate:request.LANGUAGE_CODE }}</name>
	<abbreviation>{{ list.abbreviation }}</abbreviation>
	<year>{{ list.year }}</year>
	<edition>{{ list.edition }}</edition>
	<type>{{ list.type }}</type>
	<subtype>{{ list.subtype }}</subtype>
	<observation>{{ list.obs|safe }}</observation>
	
	<section_list>

	{% recursetree nodes %}
	    <section>
	    	<name>{{ node|translate:request.LANGUAGE_CODE }}</name>
	    
	        {% if not node.is_leaf_node %}            
	            	{% if node.observation %}
	            		<observation>
		            		{% with request.LANGUAGE_CODE|add:"|observation" as language %}
		            			{{ node|translate:language }}
		            		{% endwith %}
	            		</observation>
		            {% endif %}	
	                {{ children }}                
	            
	        {% else %}
	        	
	        		{% if node.observation %}
		        		<observation>
			        		{% with request.LANGUAGE_CODE|add:"|observation" as language %}
		            			{{ node|translate:language }}
		            		{% endwith %}
			        	</observation>
			        {% endif %}	
	        		<pharmaceutical_form_list>
	        			{% if not node.id in sections_has_complementary %}
							{% for id, section_forms in pharm_section.items %}
								{% if id == node.id %}
									{% for section_form in section_forms %}
										{% if not section_form.complementary_list %}
											{% with section_form.pharmaceutical_form as form %}
												<pharmaceutical_form>
													<medicine>
														{{ form.medicine|translate:request.LANGUAGE_CODE }}
													</medicine>
													<form_type>
														{{ form.pharmaceutical_form_type|translate:request.LANGUAGE_CODE }}
													</form_type>												
													<composition>
														{% field_lang form "composition" request.LANGUAGE_CODE %}
													</composition>
		                                            <observation_list>
		                                                {% if  section_form.restriction_age %}<restriction_age>true</restriction_age>{% endif %}
		                                                {% if section_form.specialist_care_for_children %}<specialist_care_for_children>true</specialist_care_for_children> {% endif %}
		                                                {% if section_form.only_for_children %}<only_for_children>true</only_for_children>{% endif %}
		                                                {% if section_form.best_evidence %}<best_evidence>true</best_evidence> {% endif %}
		                                            </observation_list>
		                                        </pharmaceutical_form>
											{% endwith %}
										{% endif %}
									{% endfor %}
								{% endif %}
							{% endfor %}
						{% endif %}
					</pharmaceutical_form_list>

	    			{% if node.id in sections_has_complementary %}        			
	        			<complementary_list>
							{% for id, section_forms in pharm_section.items %}
								{% if id == node.id %}
									{% for section_form in section_forms %}
										{% if section_form.complementary_list %}
											{% with section_form.pharmaceutical_form as form %}
												<pharmaceutical_form>
													<medicine>
														{{ form.medicine|translate:request.LANGUAGE_CODE }}
													<medicine>
													<form_type>
														{{ form.pharmaceutical_form_type|translate:request.LANGUAGE_CODE }}
													</form_type>
													<composition>
														{% field_lang form "composition" request.LANGUAGE_CODE %}
													</composition>
		                                            <observation_list>		                                            	
		                                                {% if  section_form.restriction_age %}<restriction_age>true</restriction_age>{% endif %}
		                                                {% if section_form.specialist_care_for_children %}<specialist_care_for_children>true</specialist_care_for_children> {% endif %}
		                                                {% if section_form.only_for_children %}<only_for_children>true</only_for_children>{% endif %}
		                                                {% if section_form.best_evidence %}<best_evidence>true</best_evidence> {% endif %}		                                                
		                                            </observation_list>
												</pharmaceutical_form>
											{% endwith %}
										{% endif %}
									{% endfor %}
								{% endif %}
							{% endfor %}
						</complementary_list>
	    			{% endif %}
	        {% endif %}
	    </section>    
	{% endrecursetree %}
	</section_list>
</list>
{% endspaceless %}