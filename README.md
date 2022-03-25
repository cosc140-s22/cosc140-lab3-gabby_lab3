# COSC140 lab 3

## Answers to the five questions at the end of the lab description

1. p1=Product.objects.create(name="stuffed shark", description="soft, but with pointy teeth", price=45.00, minimum_age_appropriate=2, maximum_age_appropriate=43)

2. Product.objects.all()

3. shark=Product.objects.get(id=6)
   shark.price=22.50
   shark.save()

   Product.objects.all()

4. to_del = Product.objects.get(id=6)
   to_del.delete()

   It has id None

5. objects=Product.objects.filter(price__lt=10).filter(name__icontains= 'stuff')

## Lab feedback

 * How long did you spend on this lab? About 1.5hrs

 * What did you think about it?  What was good?  What could be improved?

## Feedback

Once you commit and submit your work to Github, I'll update this section with feedback.

