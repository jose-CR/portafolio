<?php

use Illuminate\Support\Facades\Route;

Route::view('/', 'welcome');

Route::view('dashboard', 'dashboard')
    ->middleware(['auth', 'verified'])
    ->name('dashboard');

Route::view('profile', 'profile')
    ->middleware(['auth'])
    ->name('profile');

Route::group(['middleware' => ['auth', 'verified']], function(){
    Route::view('projects', 'projects')
        ->name('projects');
    
    Route::view('project/create', 'admin.project.project-create')
        ->name('projects.create');
});

require __DIR__.'/auth.php';
