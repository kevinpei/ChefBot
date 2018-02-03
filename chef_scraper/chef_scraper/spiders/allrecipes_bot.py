# -*- coding: utf-8 -*-
import scrapy


class AllrecipesBotSpider(scrapy.Spider):
	name = 'allrecipes_bot'
	allowed_domains = ['www.allrecipes.com']
	start_urls = ['http://allrecipes.com/recipes/78/breakfast-and-brunch/']
	
	def parse(self, response):
		results_file = open('breakfast.txt', 'a')
		name = response.css('span.fixed-recipe-card__title-link::text').extract()
		ratings = response.css('span.stars.stars-4-5').xpath('@data-ratingstars').extract()
		review_number = response.css('span.fixed-recipe-card__reviews').xpath('format-large-number').xpath('@number').extract()
		for x in range(len(name)):
			results_file.write('title: ' + name[x] + ' ratings: ' + ratings[x] + ' review number: ' + review_number[x] + '\n')
		results_file.close()
