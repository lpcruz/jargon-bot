#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

print ("Hello, I am Jargon Bot. My goal is to provide you with substantial and game-changing jargon that can help you succeed. You need to move NOW. Ideation is key and the key to ideation is YOU. ")
username = raw_input("To start, what is your name? ")


def bullshit():
	'''This is bullshit'''
	intro = ['per our discussion, we will', 'pardon my sudden intrusion at this time, however, we will','for your reference, we will']
	adverbs = ['appropriately', 'collaboratively', 'compellingly', 'competently', 'completely','continually','conveniently', 'credibly', 'distinctively', 'dramatically', 'dynamically', 'efficiently','efficiently', 'energistically' ,'energistically', 'enthusiastically'  'globally', 'holisticly' , 'interactively', 'intrinsically', 'monotonectally', 'objectively', 'phosfluorescently', 'proactively', 'professionally', 'progressively', 'quickly', 'rapidiously', 'seamlessly' , 'synergistically', 'uniquely']
	verbs = ['actualize', 'administrate', 'aggregate', 'architect', 'benchmark', 'brand', 'build', 'cloudify', 'communicate', 'conceptualize', 'coordinate', 'create', 'cultivate', 'customize', 'deliver', 'deploy', 'develop', 'dinintermediate', 'disseminate', 'drive', 'embrace', 'enable', 'empower', 'enable','engage', 'engineer','enhance', 'envisioneer', 'evisculate', 'evolve', 'expedite', 'exploit', 'extend', 'fabricate', 'facilitate', 'fashion', 'formulate', 'foster', 'generate', 'grow', 'harness', 'impact', 'implement', 'incentivize', 'incubate', 'initiate', 'innovate', 'integrate', 'iterate', 'leverage existing',  'leverage skills', 'maintain', 'matrix', 'maximize', 'mesh', 'monetize', 'morph', 'myocardinate', 'negotiate', 'network', 'optimize', 'orchestrate', 'parallel', 'task', 'plagiarize',  'promote', 'pursue', 'recaptiualize','reconceptualize', 'redefine', 're-engineer', 'reintermediate', 'reinvent', 'repurpose', 'restore', 'revolutionize', 'scale', 'seize', 'simplify', 'strategize', 'streamline', 'supply', 'syndicate', 'synergize', 'synthesize', 'target', 'transform', 'transition', 'underwhelm', 'unleash', 'utilize', 'visualize', 'whiteboard']
	adjectives = ['24/7','24/365','accurate','adaptive', 'alternative', 'an expanded array of', 'B2B','B2C','backend', 'backward-compatible', 'best-of-breed','bleeding-edge','bricks-and-clicks','business','clicks-and-mortar','client-based','client-centered','client-centric','client-focused','collaborative','compelling','competitive','cooperative','corporate','cost effective','covalent','cross-functional','cross-media','cross-platform','cross-unit','customer directed', 'customized','cutting-edge','distinctive','distributed','diverse','dynamic','e-business','economically sound','effective','efficient','elastic','emerging','empowered','enabled','end-to-end','enterprise','enterprise-wide','equity invested','error-free','ethical','excellent', 'exceptional','extensible','extensive','flexible','focused','frictionless','front-end', 'fully researched','fully tested','functional','functional','future-proof','global','go forward', 'goal-oriented','granular','high standards in','high-payoff','high-quality','highly efficient', 'holistic','impactful','inexpensive','innovative','installed base','integrated','interactive', 'interdependent','intuitive','just in time','leading-edge','leveraged','long-term','low-risk high-yield','magnetic','maintainable','market positioning','market-driven','mission-critical','multidisciplinary','multifunctional','multimedia based','next-generation','on-demand', 'one-to-one','open-source','optimal','out-of-the-box','parallel','performance based', 'plug-and-play','premier','premium','principle-centered','proactive','process-centric','progressive','prospective','quality','real-time','reliable','resource maximizing', 'resource-leveling','revolutionary','robust','scalable','seamless','stand-alone','standardized', 'strategic','sustainable','synergistic','tactical','team building','team driven','technically sound','timely','top-line','transparent','turnkey','ubiquitous','user-centric','user friendly', 'value-added','vertical','viral','web-driven']
	nouns = ['alignments','applications','architectures','bandwidth','benefits', 'best practices', 'catalysts for change','channels','clouds','collaboration and idea sharing','communities','content','core competencies','customer service','data','deliverables','e-commerce','functionalities','growth straegies','human capital','ideas','imperatives','information','infrastructures','initiatives','innovation','intellectual capital','interfaces','internal or organic sources','leadership','manufactured products', 'markets','methodologies','metrics','models','niche markets','outside-of-the-box thinking','outsourcing','paradigms','partnerships','products','quality vectors','resources','relationships','results','ROI','scenarios','solutions','systems','schemas','strategy','technologies','users','vector','web services']
	
	sentence = random.choice(intro) + ' ' + random.choice(adverbs)  + ' ' + random.choice(verbs)  + ' ' + random.choice(adjectives)  + ' ' + random.choice(nouns)
	print ("Hi " + username +', ' + sentence)

bullshit()