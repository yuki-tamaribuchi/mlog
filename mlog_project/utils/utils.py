def get_profile_image_size(size):
	PROFILE_IMAGE_SIZE={
		'XS':{
			'HEIGHT':50,
			'WIDTH':50,
		},
		'SM':{
			'HEIGHT':100,
			'WIDTH':100
		},
		'MID':{
			'HEIGHT':200,
			'WIDTH':200
		},
		'LG':{
			'HEIGHT':250,
			'WIDTH':250
		},
		'XLG':{
			'HEIGHT':300,
			'WIDTH':300
		},
	}

	return PROFILE_IMAGE_SIZE[size]