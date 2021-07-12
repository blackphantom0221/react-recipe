from app.models import db, Recipe_Ingredient


def seed_recipe_ingredients():
    a = Recipe_Ingredient(ingredient_id=1, recipe_id=1, amount=1, measurement_id=13)
    b = Recipe_Ingredient(ingredient_id=2, recipe_id=1, amount=2, measurement_id=2)
    c = Recipe_Ingredient(ingredient_id=3, recipe_id=1, amount=1, measurement_id=2)
    d = Recipe_Ingredient(ingredient_id=4, recipe_id=1, amount=1, measurement_id=1)
    e = Recipe_Ingredient(ingredient_id=5, recipe_id=1, amount=3, measurement_id=10)
    f = Recipe_Ingredient(ingredient_id=6, recipe_id=1, amount=8, measurement_id=16)
    g = Recipe_Ingredient(ingredient_id=7, recipe_id=1, amount=1, measurement_id=3)
    h = Recipe_Ingredient(ingredient_id=8, recipe_id=1, amount=2, measurement_id=2)
    i = Recipe_Ingredient(ingredient_id=9, recipe_id=1, amount=2, measurement_id=3)
    j = Recipe_Ingredient(ingredient_id=10, recipe_id=1, amount=1, measurement_id=4)
    k = Recipe_Ingredient(ingredient_id=11, recipe_id=1, amount=1, measurement_id=4)
    l = Recipe_Ingredient(ingredient_id=12, recipe_id=1, amount=1, measurement_id=1)
    m = Recipe_Ingredient(ingredient_id=13, recipe_id=1, amount=1, measurement_id=3)

    n = Recipe_Ingredient(ingredient_id=1, recipe_id=2, amount=2, measurement_id=14)
    o = Recipe_Ingredient(ingredient_id=14, recipe_id=2, amount=4, measurement_id=2)
    p = Recipe_Ingredient(ingredient_id=15, recipe_id=2, amount=1, measurement_id=2)
    q = Recipe_Ingredient(ingredient_id=2, recipe_id=2, amount=1, measurement_id=2)
    r = Recipe_Ingredient(ingredient_id=3, recipe_id=2, amount=1, measurement_id=2)
    s = Recipe_Ingredient(ingredient_id=16, recipe_id=2, amount=2, measurement_id=3)

    t = Recipe_Ingredient(ingredient_id=17, recipe_id=3, amount=1, measurement_id=4)
    u = Recipe_Ingredient(ingredient_id=5, recipe_id=3, amount=2, measurement_id=7)
    v = Recipe_Ingredient(ingredient_id=2, recipe_id=3, amount=1, measurement_id=2)
    w = Recipe_Ingredient(ingredient_id=1, recipe_id=3, amount=1, measurement_id=13)
    x = Recipe_Ingredient(ingredient_id=3, recipe_id=3, amount=1, measurement_id=3)
    y = Recipe_Ingredient(ingredient_id=4, recipe_id=3, amount=1, measurement_id=3)
    z = Recipe_Ingredient(ingredient_id=7, recipe_id=3, amount=1, measurement_id=3)

    aa = Recipe_Ingredient(ingredient_id=18, recipe_id=4, amount=1, measurement_id=13)
    ab = Recipe_Ingredient(ingredient_id=19, recipe_id=4, amount=1, measurement_id=3)
    ac = Recipe_Ingredient(ingredient_id=2, recipe_id=4, amount=1, measurement_id=3)
    ad = Recipe_Ingredient(ingredient_id=3, recipe_id=4, amount=1, measurement_id=3)
    ae = Recipe_Ingredient(ingredient_id=20, recipe_id=4, amount=1, measurement_id=4)

    db.session.add(a)
    db.session.add(b)
    db.session.add(c)
    db.session.add(d)
    db.session.add(e)
    db.session.add(f)
    db.session.add(g)
    db.session.add(h)
    db.session.add(i)
    db.session.add(j)
    db.session.add(k)
    db.session.add(l)
    db.session.add(m)

    db.session.add(n)
    db.session.add(o)
    db.session.add(p)
    db.session.add(q)
    db.session.add(r)
    db.session.add(s)

    db.session.add(t)
    db.session.add(u)
    db.session.add(v)
    db.session.add(w)
    db.session.add(x)
    db.session.add(y)
    db.session.add(z)

    db.session.add(aa)
    db.session.add(ab)
    db.session.add(ac)
    db.session.add(ad)
    db.session.add(ae)

    db.session.commit()


def undo_recipe_ingredients():
    db.session.execute('TRUNCATE recipe_ingredients RESTART IDENTITY CASCADE;')
    db.session.commit()
