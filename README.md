## Inspiration
Art is cool. AI is cool. That's enough, I guess. 

## What it does
A website with infinite art...all made by an AI! Featuring historical styles such as Impressionism and Neoclassicism. Also with a semi-functional game to guess which art pieces are real and which ones are made by the AI. 

<img src="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_thumbnail_photos/001/441/877/datas/medium.png" alt="image"> 

Devpost Link:
<a href="https://devpost.com/software/picassogan"> https://devpost.com/software/picassogan </a>

## Challenges 
We’ve both always been very interested in AI and have long desired to work with some of the more novel neural network structures. We saw DVHacks as an opportunity to explore modern AI in a more creative fashion and decided to implement one of the most fascinating neural networks: the GAN, generative adversarial network, proposed by Goodfellow in 2014. 

In essence, the GAN has two components: the generator, and the discriminator. The generator tries to generate images of a certain theme given by the dataset (ie. pictures of cars), and the discriminator must be able to distinguish and classify which images it receives are real and from the dataset and which ones are “fake” (the ones made by the generator). By constantly trying to one-up each other, the GAN adopts an “adversarial” approach to AI generation which we realized was amazingly effective.

## Our Project

We decided to create a GAN to generate its own art from various historical movements. Trained on many of the most famous artists, it was able to replicate this art and create its own - this is a great achievement in its own right, considering the complexity of some of the artworks. Each time a user visits the main page, they have the option to select from a variety of artistic styles such as Impressionism or Romanticism, for example. Once choosing a style, a gallery of nine newly generated images is presented. The user can generate as many images as they want by refreshing. Every image seen is brand new and unique; you won't find it anywhere else. 

## What we used

We used pandas and pickle for the data pre-processing and dataset generation. We made our own dataset of various artworks from different styles by taking works from WikiArt. We used Tensorflow for the neural network architecture, matplotlib for visualizing results, and Kaggle/Google Colab for GPU acceleration. The frontend was built with Python, the Dash library, and HTML/CSS.

## Challenges

Initially, the GAN was unable to make coherent art at all, even when the dataset was fully grayscale. Especially in the very limited amount of time we had, any failed training attempts were extremely costly. We initially thought our GAN would never work; however, after revising our GAN structure such that the discriminator & generator losses were separated, we overcame this challenge and our GAN produced amazing results. 

Yet, we know we could have done better given more training time; because we only had less than a day for actual model training, the majority of our generations were done in 64x64 images. Considering the time constraints, however, we are very happy that we were able to not only build the network architecture and train it on various styles but also integrate it with the frontend to provide viewers with an easy and elegant way to view an infinite amount of art.

## Future Work

More training, more styles will give us more and better art to share. We also developed the functionality for a quick game whereby people are given real art and our GAN’s art and must decide which one is the real one. And with more training to come, this game will only get harder…

Of course, selling these artworks may be difficult now, but as our GAN and its generations become more refined and efficient, only time will tell!
